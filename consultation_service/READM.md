# Consultation Service

_Este servicio fue implementado usando librerias netamente provistas por python, se realizo bajo estandares de codificación como PEP8, para eto se uso la libreria black. Se hizo la distribucion de funcionalidades entre unas clases controladoras y las clases de modelo._

_Para efectos de agilidad del servicio se implemento cache en una funcionalidad de consulta a la base de datos, para la implementacion de cache se hizo uso de la libreria cachetools._

_Los test unitarios fueron realizados con la libreria unittest, realizando un buen porcentaje de pruebas de los escenarios y flujos principales._

_Se hizo uso del patron singleton para que siempre hubiera una y solo una conexion abierta. De la cual el sistema provisionara de cursores con los cuales efectuar transacciones en la base de datos._

_Este proyecto fue desarrollado en un ambiente Linux (Ubuntu) razon por la cual las siguientes anotaciones pueden tener diferencias entre sistemas operativos_

__Nota:__

_Para la ejecucion del proyecto se deben ajustar las variables de entorno que estan en el archivo env_variables.sh con la siguiente instruccion:_

`source env_variables.sh`

_Para la ejecucion de los test unitarios se realizara de la siguiente forma_

`python -m unittest`
