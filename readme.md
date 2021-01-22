# Creación de aplicaciones en odoo
carpeta(en Windows):
C:\Program Files (x86)\Odoo 10\server\odoo\addons  
Crear  carpeta(nombre aplicacion)  
Crear fichero 
~~~
__init__.py
~~~
Luego necesitamos crear el archivo descriptor. Debe contener únicamente un diccionario Python y puede contener alrededor de una docena de atributos, de los cuales solo el atributo name es obligatorio. Son recomendados los atributos description, para una descripción más larga, y author. Ahora agregamos un archivo 

~~~
__manifest__.py:
~~~


~~~
{
    # Creación de aplicaciones en odoo
carpeta(en Windows):
C:\Program Files (x86)\Odoo 10\server\odoo\addons  
Crear  carpeta(nombre aplicacion)  
Crear fichero 

~~~
    __init__.py
~~~

Luego necesitamos crear el archivo descriptor. Debe contener únicamente un diccionario Python y puede contener alrededor de una docena de atributos, de los cuales solo el atributo name es obligatorio. Son recomendados los atributos description, para una descripción más larga, y author. Ahora agregamos un archivo 

~~~
__manifest__.py:
~~~


~~~
{
    'name': 'prue01',
    'description': 'Aplicación ejemplo.',
    'author': 'Autor',
    'depends': ['mail'],
    'application': True
}
~~~


El atributo depends puede tener una lista de otros módulos requeridos. Odoo los instalará automáticamente cuando este módulo sea instalado.

Los modelos describen los objetos de negocio, como una oportunidad, una orden de venta, o un socio (cliente, proveedor, etc). Un modelo tiene una lista de atributos y también puede definir su negocio específico.

Los modelos son implementados usando clases Python derivadas de una plantilla de clase de Odoo. Estos son traducidos directamente a objetos de base de datos, y Odoo se encarga de esto automáticamente cuando el módulo es instalado o actualizado.
Creamos la carpeta models y añadimos el fichero datodato.py:

~~~
#-*- coding: utf-8 -*-
from odoo import models, fields, api

class Dato(models.Model):
    _name = 'prue01.dato'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
~~~

La primera línea es un marcador especial que le dice al interprete de Python que ese archivo es UTF-8, por lo que puede manejar y esperarse caracteres non-ASCII. No usaremos ninguno, pero es mas seguro usarlo.

La segunda línea hace que estén disponibles los modelos y los objetos campos del núcleo de Odoo.

la tercera línea declara nuestro nuevo modelo.    

Todavía, este archivo, no es usado por el módulo. Debemos decirle a Odoo que lo cargue con el módulo en el archivo __init__.py. Editemos el archivo para agregar la siguiente línea:

~~~
from . import models
~~~

En la carpeta models debemos crear un archivo __init__.py , indicando el modelos que debe cargar:

~~~
from . import dato
~~~

Reiniciamos el servidor e instalamos la aplicación.

Ahora podemos revisar el modelo recién creado en el menú Técnico. Ia  a ajustes/Estructura de la Base de Datos/Modelos y buscamos el modelo creado (prue01.dato) en la lista. Luego haga clic en este para ver su definición:

Si no hubo ningún problema, esto nos confirmará que el modelo y nuestros campos fueron creados. Si hizo algunos cambios y no son reflejados, intente reiniciar el servidor, para obligar que todo el código Python sea cargado nuevamente.

También podemos ver algunos campos adicionales que no declaramos. Estos son cinco campos reservados que Odoo agrega automáticamente a cualquier modelo. Son los siguientes: - id: Este es el identificador único para cada registro en un modelo en particular. - create_date y create_uid: Estos nos indican cuando el registro fue creado y quien lo creó, respectivamente. - write_date y write_uid: Estos nos indican cuando fue la última vez que el registro fue modificado y quien lo modificó, respectivamente.

al cual almacenar nuestros datos, hagamos que este disponible en la interfaz con el usuario y la usuaria.
Si no podemos ver nuestro modelo no podemos pasar al siguiente paso.

Todo lo que necesitamos hacer es agregar una opción de menú para abrir el modelo  para que pueda ser usado. Esto es realizado usando un archivo XML. Igual que en el caso de los modelos, algunas personas consideran como una buena practica mantener las definiciones de vistas en en un subdirectorio separado.

Crearemos un directorio llamado views y dentro de el un archivo dato.xml,  este tendrá la declaración de un ítem de menú y la interfaz del modelo:

~~~
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <data>
        <act_window id="prue01_dato_action" name="dato"
                     res_model="prue01.dato" />


        <record id="prue01_dato_view_tree" model="ir.ui.view">
            <field name="name">Lista datos</field>
            <field name="model">prue01.dato</field>
            <field name="arch" type="xml">

                <tree>
                    <field name="codigo" />
                    <field name="marca" />
                </tree>
            </field>
        </record>



        <record id="prue01_dato_view_search" model="ir.ui.view">
            <field name="name">Busqueda datos</field>
            <field name="model">prue01.dato</field>
            <field name="arch" type="xml">
                <search>
                    <field name="codigo" />
                    <field name="marca" />

                </search>
            </field>
        </record>
        <menuitem name="Datos" id="menu_dato" sequence="10" />
        <menuitem name="Inicio" id="menu_inicio" parent="menu_dato" sequence="10"/>
        <menuitem name="Dato" id="menu_datos" action="prue01_dato_action" parent="menu_inicio" sequence="10"/>

    </data>
</odoo>
~~~

La interfaz con el usuario y usuaria, incluidas las opciones del menú y las acciones, son almacenadas en tablas de la base de datos. El archivo XML es un archivo de datos usado para cargar esas definiciones dentro de la base de datos cuando el módulo es instalado o actualizado. Esto es un archivo de datos de Odoo, que describe dos registros para ser agregados a Odoo: - El elemento <act_window> define una Acción de Ventana del lado del cliente para abrir el modelo aplicacion.task definido en el archivo Python, con las vistas de árbol y formulario habilitadas, en ese orden. - El elemento <menuitem> define un ítem de menú bajo el menú Mensajería (identificado por mail.mail_feeds), llamando a la acción action_aplicacion_task, que fue definida anteriormente. el atributo sequence nos deja fijar el orden de las opciones del menú.

Ahora necesitamos decirle al módulo que use el nuevo archivo de datos XML. Esto es hecho en el archivo __manifest__.py usando el atributo data. Este define la lista de archivos que son cargados por el módulo. Agregue este atributo al diccionario del descriptor:

~~~
'data': ['views/dato.xml']
~~~

Se generará un formulario.
