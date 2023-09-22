## FLASK 

![Flask-framework](/images/flas-rest-api.jpg)

Flask es un micro-framework de desarrollo web escrito en Python. Se denomina "micro" porque tiene como objetivo mantener el núcleo simple pero extensible. Flask ofrece sugerencias, pero no impone una forma particular de hacer las cosas, lo que ofrece mucha flexibilidad a los desarrolladores. No viene con muchas de las herramientas y bibliotecas incorporadas que otros frameworks ofrecen, pero se puede agregar fácilmente cualquier extensión para mejorar sus funcionalidades.

## Características Principales

* Sencillez y Flexibilidad: Flask es fácil de entender y de empezar. Su API simple y clara permite una rápida integración con otros servicios y bibliotecas de Python.
* Extensibilidad: Aunque Flask viene con un conjunto mínimo de características, se puede extender con "Flask Extensions" que se pueden instalar con facilidad.
* Werkzeug WSGI Toolkit: Flask se basa en el Werkzeug WSGI toolkit y el motor de templates Jinja2, lo cual le otorga mucha capacidad y versatilidad para desarrolladores experimentados.
* Desarrollo de APIs: Flask es muy utilizado para el desarrollo de APIs RESTful. Permite manejar peticiones HTTP y trabajar con múltiples formatos de datos, lo que lo hace ideal para este tipo de proyectos.
* Soporte para Pruebas Unitarias: Flask permite la configuración de pruebas unitarias, lo cual es crucial para el desarrollo de aplicaciones a gran escala.
* Community-Driven: Una de las grandes fortalezas de Flask es su comunidad, que contribuye a un rico ecosistema de extensiones y tutoriales.

## Casos de Uso

* Desarrollo de APIs RESTful
* Sitios web pequeños a medianos
* Aplicaciones Web de una sola página (SPA)
* Prototipos rápidos
* Integración con servicios de almacenamiento en la nube, bases de datos y más.

Flask ha crecido en popularidad debido a su simplicidad y flexibilidad, y es ampliamente utilizado tanto en startups como en grandes corporaciones para una variedad de aplicaciones y proyectos.

## Instalacion de Flask

La instalación de Flask es un proceso relativamente sencillo que puede hacerse utilizando herramientas de administración de paquetes de Python como pip. A continuación, se describe el procedimiento típico para instalar Flask en un sistema que ya tiene Python instalado.

### Prerrequisitos

* Tener [Python](https://www.python.org/downloads/) instalado (versión 3.6 o superior recomendada).
* Tener [pip](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/) instalado (la mayoría de las instalaciones de Python ya incluyen pip).

## Pasos para la Instalacion

1. Abrir la Terminal o CMD: Dependiendo de tu sistema operativo, abre la terminal (Linux/Mac) o el símbolo del sistema (Windows).

2. Crear un Entorno Virtual (Opcional pero recomendado)

```
python -m venv venv

```

*  Activar el entorno virtual:
    * Windows: .\venv\Scripts\activate
    * Mac/Linux: source myenv/bin/activate

* Salir del entorno virtual:
    * deactivate

3. Instalar Flask

```
pip install Flask

```

4. Verificar la Instalacion

```
python -m flask --version

```

5. Correr la aplicacion flask

```
flask run

```