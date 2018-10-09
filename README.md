# Desarrollo Web

## RESTful APIs; Servicios Web

### ISC School & CodeNoSchool

#### Curso completo

##### Easy and Free Learning


# Introducción

Bienvenid@ a otro curso de desarrollo web de la mano de ISC & CodeNoSchool.

Desarrollar APIs basadas en REST se ha vuelto bastante popular en los últimos años, prácticamente interactuamos con ellas día a día al navegar por Internet. Es por está razón que en este curso aprenderás a saber qué implican, cómo construirlas, consumirlas (utilizarlas), y todo ello de la manera más simple.

Actualmente existen diferentes conjuntos de herramientas que nos ayudan a desarrollar APIs basadas en REST, por ejemplo, uno de los conjuntos de desarrollo más populares en estos días está conformado por: Express/Node JS (Javascript). Durante este curso sí que verás demostraciones con este conjunto de desarrollo basado en Javascript e incluso algunos otros, sin embargo, principalmente utilizaremos Flask, el cual es un framework de desarrollo web basado en el lenguaje de programación Python; es minimalista, y nos permite aprender observar, practicar y comprender cada uno de los temas del curso.

¿Te animas? Esperamos que sí. Aquí te dejamos los requisitos previos que necesitas para tomar este curso completo y gratuito que te ayudara a adentrarte en el mundo del Desarrollo Web, y además respondemos algunas de las dudas frecuentes.

## Requisitos (para tomar el curso)

* **Ninguno! \***

¿No nos crees? Bueno, te contamos la verdad.

* Fundamentos de programación.
* Fundamentos de bases de datos

\* Algo importante a tener en cuenta es que la razón por la cual consideramos que no necesitas conocimientos previos para iniciar este curso es que los vídeos estarán preparados para dejarte sin ninguna duda, permitirte avanzar sin importar qué, y que al final puedas reforzar conocimientos y aprender cosas nuevas.

## Preguntas frecuentes (FAQ)

* ¿De qué trata el curso?
  + El área en la que aprenderemos cosas nuevas será Desarrollo Web.
  + Existen diferentes enfoques de desarrollo en esta área, nosotros utilizaremos el principio REST para crear APIs
  + Crear, implementar, distribuir, modificar y consumir APIs; nuestras, de otras personas y/o empresas.

* ¿Qué herramientas se utilizarán durante el curso?
  + Principalmente el framework de Flask, basado en Python.
  + Se harán demostraciones con otro conjunto de herramientas, por ejemplo, Express/Node (Javascript), y algunos otros.

* ¿Qué herramientas necesito instalar?
  * En realidad ninguna, puedes seguir el curso solamente mirando los vídeo-tutoriales.
  * Si quieres crear tus propios proyectos a la par del curso entonces necesitarás al menos *:
    * Python (versión 3.>)
    * Editor de código
    * Navegador web (actual)
  
  \* Puedes obtener más información acerca de la instalación de herramientas y configuración de entorno en el vídeo-tutorial del curso que se ha preparado para ello.

* No sé utilizar las tecnologías/herramientas de este curso, ¿qué puedo hacer?
  * Recuerda que nos esforzamos por hacer que cada vídeo sea completamente claro, y además las tecnologías/herramientas que elegimos para este curso están preparadas para que cualquier persona pueda aprender aún si no las conoce previamente.

* ¿Qué otros curso de desarrollo web hay disponibles?
  * Puedes seguir el curso de Flask, el cual es completo y gratuito. Son 25 vídeos a tu disposición para que aprendas muchas cosas más.

### Demostración (Flask/Python)

Te mostramos un ejemplo para que veas lo sencillo que es crear tu primera aplicación con Flask/Python, las cuales serán nuestras herramientas principales para este curso.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  
    return "Hello World!"
    
if __name__ == "__main__":
    app.run()
```

**¿Acaso no es sencillo? Así que no te preocupes, solamente concentrate en aprender y dejanos el resto.**

# Temario del curso:

> **"No analizaremos los temas a fondo, pero tampoco a la ligera sino simplemente lo que resulte necesario."** - Jessy K. Martz

### Sección | ¡Vamos a comenzar!

- [x] Introducción
- [x] Primeras aplicaciones web
- [x] Entorno de trabajo

### Sección | Teoría básica

- [x] Rutas (URI, URL, URN, Endpoints)
- [ ] HTTP/REST (Peticiones/Respuestas)
- [x] JSON

### Sección | HTTP/REST (Métodos/Verbos)

- [x] Método GET
- [x] Método POST
- [x] Método PUT
- [x] Método DELETE

### Sección | Base de datos

- [x] Bases de datos SQL (MySQL, SQLite, PostgreSQL)
- [x] MongoDB (Made Simple)
- [x] Hojas de cálculo

### Sección | Consumir/Utilizar APIs

- [x] ¿Cómo consumir una REST API?
- [x] APIs públicas (Servicios básicos y desarrollo)
- [x] APIs restringidas (Autenticación)

### Sección | RESTful APIs

- [ ] Integrar aplicación web con una RESTful API (Flask/Python)
- [ ] Integrar aplicación web con una RESTful API (Express/Node JS)
- [ ] Single Web Pages /w RESTful API (Final App)
- [ ] FINAL DE CURSO

## Resumen de Curso

Sabemos que a veces se necesitará información de primera mano, es por ello que te damos una breve descripción del contenido de cada vídeo para que si estás buscando algo en particular lo puedas encontrar tan rápido como sea posible.

### 1 |  Introducción

#### Sacar el máximo provecho del curso

Siempre buscamos que puedas beneficiarte de toda la información, por ello te explicamos una de las posibles maneras que puedes emplear para sacar el máximo provecho de la información que se ofrecerá a lo largo de todo el curso.

### 2 |  Primeras aplicaciones web

#### Crea tus dos primeras aplicaciones web

Crearemos dos aplicaciones web que harán exactamente lo mismo, pero utilizaremos dos distintos conjuntos de herramientas para crearlas. Por un lado tenemos a Flask/Python, y por el otro a Express/Node JS. El propósito es mostrarte lo sencillo que es crear aplicaciones web con estás herramientas, y además el hecho de que aprender las bases de desarrollo web te ayudará a trabajar en diferentes proyectos sin importar el conjunto de herramientas que utilices.

### 3 | Entorno de Trabajo

#### Instalaciones y Configuraciones

Después de ver lo sencillo que será trabajar en este curso y si así lo decides, puedes crear tus propios proyectos a la par del curso. Para eso necesitarás instalar y configurar algunas cosas, aquí te vamos a mostrar cómo.

Haremos dos vídeos para dejar tu entorno bien preparado:

* Windows (Aplica para la mayoría de sus versiones).
* Unix/GNU Linux (Todo el que se parezca a Ubuntu, ArchLinux, MAC OS, CentOS, y muchos otros).

### 4 |  Rutas
#### URLs, parámetros, argumentos, endpoints

Preparar rutas para tu aplicación web, en este caso siendo más específicos, para tu RESTful API es algo vital. Es por ello que te explicamos algunos de los conceptos básicos.

### 5 | HTTP/REST

#### Protocolos; peticiones y respuestas

Para que una aplicación web funcione se debe elegir que reglas de desarrollo, comunicación, y diseño se deben seguir. Para este curso utilizaremos las bases HTTP/REST, por eso es importante que conozcas qué implica cada uno los términos.

### 6 | JSON Python/Flask

#### Intercambio de datos a través de JSON

Existen diferentes maneras de intercambiar datos a través de una aplicación web. Cuando nos referimos a RESTful APIs se suelen utilizar formatos rápidos, ligeros y legibles. JSON es uno de los formatos más populares que cumple con las características antes mencionadas, por eso aprenderás cómo entenderlos.

## Tema | Métodos/Verbos del protocolo HTTP

Aquí aprenderás a utilizar cada uno de los métodos/verbos del protocolo HTTP bajo el contexto RESTful a través de tu API. Formando así una RESTful API Web Application with Flask.

* ### 7 | GET

	#### Conseguir recursos

* ### 8 | POST
    
	#### Crear recursos

* ### 9 | PUT
    
	#### Modificar recursos

* ### 10 | DELETE
  
	#### Eliminar recursos
    
## Tema | Bases de Datos

* ### 11 | Base de Datos SQL (SQLite, MySQL, PostgreSQL)

	#### Persistencia de Datos
	
	El movimiento que se genere en nuestra aplicación traerá consigo distintos datos que en muchas ocasiones utilizaremos después, así que debemos almacenarlos en algún lugar, y ese lugar es una base de datos. Aquí conocerás algunas ideas que te ayudarán a integrar una base de datos y administrar el manejo de los datos.

* ### 12 | Base de datos MongoDB

	#### Familiar integración con una RESTAPI

	Las REST API por lo general utilizan el formato JSON para el intercambio de datos, cuya estructura es bastante parecida a estructuras de otros lenguajes de programación, entre ellos Javascript y es la sintaxís de este lenguaje la que es bastante parecida a las estructuras de datos que se manejan en MongoDB. Es por ello que integrar estas dos tecnologías es de lo más familiar y lo más común hoy en día.

* ### 13 | Hojas de cálculo

	#### Operaciones concretas
	
	Una opción más para administrar y realizar operaciones con los datos de tu aplicación es hacer uso de una hoja de cálculo. Te daremos ideas para que conozcas dónde puedes implementarlas junto con tu aplicación.

## Tema | Consumir APIs

* ### 14 | ¿Cómo hacerlo? Casos más comunes

	#### Webhooks, aplicaciones web, híbridas, y multiplataforma
	
	Una de las ventajas de construir RESTful APIs es que nos permiten consumir los diferentes servicios que ofrecen. Esto nos facilita el de hecho crear otro tipo de aplicaciones de manera rápida para ofrecer otro tipo de servicios y experiencias personalizadas. Te mostraremos los casos más comunes.

* ### 15 | Servicios básicos y desarrollo

	#### REST APIs básicas
	
	Aprende a consumir diferentes APIs públicas las cuales ofrecen servicios básicos y no requiren de ningún tipo de autenticación. También hay diferentes herramientas que nos ayudarán a continuar con nuestro desarrollo.

* ### 16 | Servicios privados

	#### Autenticación y grandes servicios de REST APIs
	
	Conoce diferentes REST APIs de grandes empresas. Te damos una guía acerca de cómo encontralas, y utilizarlas en tus propios proyectos.

## Tema | RESTful APIs

Casi llegamos al final de nuestro curso, esperamos que hayas aprendido muchas cosas nuevas.

Para reafirmar todo lo que has aprendido te presentaremos una serie de demostraciones para que observes los diferentes casos de uso, desarrollo e integración de aplicaciones web a través de diferentes servicios, tecnologías y herramientas.

* ### 17 | Express/Node JS (Javascript)

	#### Creación de un Sitio Web
	
	Crea tu propio sitio web dinamico consumiendo recursos de una REST API.
    
* ### 18 | Flask/Python

	#### Creación de un Webhook
	
	Crea un webhook para que logres manipular los recursos de una REST API a tu propia necesidad.
    
* ### 19 | Single Web Pages /w RESTful API

	#### Aplicaciones Finales; #free
	
	Consume una REST API a través de una Single Web Page creada con VueJS, la característica principal de esta, es que no utiliza una tecnología backed por sí misma.

## FINAL DE CURSO

#### Información final importante

Te damos más información para que puedas sacarle el máximo provecho a todo lo que has aprendido durante el curso. Te brindamos consejos, resolvemos las dudas más comunes y te comentamos con qué temas podrías continuar para que sigas avanzando en tu aprendizaje.

## Informaci�n adicional sobre el Curso

Lista de Reproducción del Curso: https://www.youtube.com/playlist?list=PLBO4apWPK7b6tRI_B1MQGZfvI6c3ViQd-

Repositorio del curso (GitHub): https://github.com/codenoschool/restapis-course

ISC School

CodeNoSchool

Darkz Sites Company

SUERTE!

Enlaces de interés

ISC School: https://www.youtube.com/channel/UC50fQ-3Lwj2UaAlDMsSG7Kw

CodeNoSchool: https://www.youtube.com/c/CodeNoSchool

Twitter: https://twitter.com/codenoschool

Blog (Blogger): https://codenoschool.blogspot.mx/

Blog (Vivaldi): https://codenoschool.vivaldi.net/
