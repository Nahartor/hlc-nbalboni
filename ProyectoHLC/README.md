# API - HLC
Bienvenido a la guía explicatva de mi proyecto final de HLC.
En este documento explicare brevemente las diferentes partes del código
tales como funciones, objetos y variables.
***

## La base de datos
Esta API realiza consultas, inserciones, modificaciones y borrado de datos sobre una única tabla de una base de datos.
A continuación definiré los requerimientos necesarios para que puedas crear tu propia base de datos, así como qué parámetros necesitas modificar dentro del código de la API para poder conectarte a ella correctamente.
> Nota: la instalación del servidor de bases de datos corre de tu cuenta.

#### Estructura de la base de datos
Se debe crear una base de datos de nombre **instituto**, sobre ella se creará una tabla llamada **asignatura** cuya estructura básica describiré a continuación.
En la base de datos se debe crear un usuario al que concederemos todos los permisos sobre la base de datos **instituto** y permisos de acceso remoto.