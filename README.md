# Flask-REST-Guide
 'Introducción al Desarrollo Web con Python y Flask'. Aquí aprenderás los fundamentos de la construcción de una API RESTful utilizando el micro-framework Flask de Python. Este material es ideal para desarrolladores principiantes o intermedios que buscan adentrarse en el mundo de las APIs y el desarrollo web con Python.

![Flask Guide](/images/flask-libraries.jpg)

## Definicion de API

Una API (Interfaz de Programacion de Aplicaciones) es un conjunto de reglas y protocolos que permiten que diferentes programas o sistemas se comuniquen entre si. 
Se puede pensar en una API como un menu en un Restaurante. El menu ofrece una lista de platillos que se pueden ordenar, junto con una descripcion de cada platillo. Cuando especificamos que platillo se desea, la cocina (El sistema) prepara el platillo y lo sirve. De esta manera el menu actua como una interfaz entre los deseos del cliente y la cocina
que prepara los platillos.

![Restaurant-rest-api](/images/rest-api-restaurant.jpg)

## Ejemplo de la vida Real

Un ejemplo cotidiano podria ser el uso de una aplicacion de transporte como Uber. Uber utiliza diversas APIs para funcionar

![Uber](/images/uber-rest-api.jpg)

* Una para determinar la ubicacion del usuario (geolocalización) 
* Otra para procesar pagos (API de pasarela de pago)
* Otra para enviar notificaciones ( Mensajes )

Asi como esto todos los sitemas interactuan a travez de sus respectivas APIs para proporcionar el servicio que experimentan los usuarios. 

## API REST

REST ( Representational State Transfer ) es un estilo arquitectonico que se utiliza comunmente para desarrollar servicios web. La arquitectura REST es 
stateless, lo que significa que cada solicitud del cliente al servidor debe contener toda la informacion necesaria para comprender y procesar la solicitud 

![Rest-api](/images/rest-api-working.jpg)

## Principios REST

* Stateless: Cada petición del cliente al servidor debe contener toda la información necesaria para entender y procesar la petición. No se guarda ningún estado en el servidor entre peticiones sucesivas.

* Client-Server: REST sigue el modelo cliente-servidor, donde el cliente y el servidor son entidades separadas que se comunican a través de una red.

* Cacheable: Las respuestas del servidor pueden ser explícitamente marcadas como cacheables o no cacheables. Esto ayuda a mejorar la eficiencia y la escalabilidad. Cuando una respuesta es "cacheable", significa que el cliente (o algún intermediario entre el cliente y el servidor, como un proxy de caché) puede guardar localmente una copia de la respuesta. De esta forma, futuras peticiones idénticas pueden ser respondidas desde la caché en lugar de ser enviadas al servidor, mejorando así la eficiencia y la velocidad de la aplicación.

* Uniform Interface: REST utiliza un conjunto de convenciones y estándares (como HTTP, URLs y MIME types) para facilitar la interacción entre el cliente y el servidor

## HTTP ( Protocolo de transferencia de hpertexto )

Http es un protocolo que permite la transferencia de datos a travez de la web. Actua como un protocolo de peticion-respuesta en el modelo cliente-servidor. Los navegadores web actuan como clientes que hacen solicitudes, y los servidores web actuan como servidores que procesan esas solicitudes y devuelven una respuesta. 

### Metodos HTTP:

* GET: Solicita una representación del recurso.
* POST: Envía datos para ser procesados por el recurso identificado.
* PUT: Actualiza un recurso existente o crea uno nuevo si no existe.
* DELETE: Elimina el recurso especificado.

### Body 

En una peticion http, el cuerpo o "body" es la parte del mensaje donde se almacenan los datos que se enviaran al servidor. No todas las peticiones http tienen un cuerpo; generalmente, los metodos como GET y HEAD no lo utilizan, mientras que POST y PUT si. En una API REST, cuando se envian datos en formato JSON, el cuerpo de la peticion podria verse algo asi:

```json
{
  "nombre": "John",
  "apellido": "Doe",
  "edad": 30
}

```

## URLs ( Localizadores uniformes de recursos )

Uan URL ( uniform Resource Locator ) es una direccion que identifica un recurso particular en la web. Esta compuesta por varios elementos, como el protocolo http o https, el nombre de dominio, la ruta del recurso, parametros y mas. 

Ejemplo:

```
https://www.example.com/path?name=value

```

1. https es el protocolo
2. www.example.com es el nombre de dominio
3. /path es la ruta
4. name=value es un parámetro.

## MIME Types (Tipos de MIME)

MIME (Multipurpose Internet Mail Extensions) es un estándar que indica el tipo de contenido que se está transmitiendo. Se utiliza tanto en el correo electrónico como en la transferencia de documentos por la web. Los tipos MIME se especifican en la cabecera HTTP Content-Type para informar al cliente sobre el tipo de datos del cuerpo del mensaje. Algunos ejemplos comunes son:

* text/plain: texto sin formato.
* text/html: documento HTML.
* application/json: datos en formato JSON.
* image/png: imagen en formato PNG.

En el contexto de las APIs, especialmente las APIs REST, estos elementos son fundamentales para el funcionamiento y la interoperabilidad de diferentes sistemas. HTTP dicta cómo se realizan las solicitudes y respuestas, las URLs identifican dónde se deben realizar esas solicitudes, y los tipos MIME indican el formato en que los datos son enviados y recibidos.

## Códigos de estado HTTP

Los códigos de estado HTTP se utilizan para indicar el resultado de la operación solicitada. Estos códigos de estado son una parte esencial del protocolo HTTP y son muy importantes para la implementación y el consumo de APIs, incluidas las APIs REST. Ayudan a los clientes a entender el resultado de la petición que han realizado. Aquí hay algunas clases comunes y ejemplos de códigos de estado:

### Respuestas informativas (100–199)

* 100 Continue: El servidor ha recibido los encabezados de la petición, y el cliente debería continuar con el envío del cuerpo.

### Respuestas exitosas (200–299)
 
* 200 OK: La petición fue exitosa, y el servidor ha devuelto los datos solicitados.
* 201 Created: La petición fue exitosa y se ha creado un nuevo recurso.

### Redirecciones (300–399)

* 302 Found: El recurso se encuentra temporalmente en otra URL.

### Errores del cliente (400–499)

* 400 Bad Request: La petición es inválida o no puede ser procesada por el servidor.
* 401 Unauthorized: Se requiere autenticación para acceder al recurso.
* 403 Forbidden: El cliente no tiene permisos para acceder al recurso.
* 404 Not Found: El recurso solicitado no se encuentra en el servidor.

### Errores del servidor (500–599)

* 500 Internal Server Error: Un error ocurrió en el servidor y no se pudo completar la petición.
* 502 Bad Gateway: Un servidor proxy recibió una respuesta inválida de un servidor en una cadena de servidores.
