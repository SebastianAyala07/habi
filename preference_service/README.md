## Like Service 👍
---

__Servicio teorico de likes__

_Para el servicio de likes se tuvo en cuenta que ya contamos con un microservicio que administra propiedades razon por la cual dentro del microservicio "Like service" se implementan entidades tales como usuario y el historial de likes por usuario al cual van ligados los idetificadores de la propiedad el usuario y la fecha de modificacion (Fecha en la que se dio like o se quito)_

_Esto a su vez como se ve en el diagrama estaria conectado al backend del microservicio en en cual estaria toda la logica de negocio, en este caso la gestion, administracion e historico de likes._

_El microservicio "Like service" a su vez estara expuesto para poder ser utilzado por un servicio externo o por un cliente, en el caso del diagrama es utilizado por un API que maneja los diferentes servicios en pro de un cliente._
