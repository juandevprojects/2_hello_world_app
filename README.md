Este es una app hello world estructurada con el adamiaje necesario python para poder configurar CI/CD en distintas nubes o en contenedores.

1- Necesitaré un archivo python que contenga todo el código necesario para resolver el problema que queramos que resuelva. En este caso se llamará `hello_world.py`.

2- Será necesario un archivo python de testing que pruebe que el problema que desea resolver sea siempre resulto aunque se cambie el código en `hello_world.py`, el archivo de testing será `test_hello_world.py`

3- Necesitaremos un archivo `requirements.txt` que contenga todos los paquetes python necesarios para poder desarrollarar, testear y hacer contro de calidad del modelo. Para poder replicarlo en cualquier máquina

4- Ahora empieza la configuración del CI/CD (DevOps puro y duro) con la configuración de los comandos de las distintas etapas del pipeline devops deseado, se declaran en el archivo `Makefile` y se ejecutan en los archivos `.yml` correspondientes a los workflows ya sea de github actions o los archivos de configuración puros y duros de cada nube que hospede este código fuente.

5- Configuración del `Makefile`: constará de 4 etapas básicas y que son las mínimas para considerar el mínimo control de calidad DevOps.

    5.1- `install:` para instalar todas las dependencias (paquetes python) necesarias para ejecutar la app

    5.2- `lint`: Analyzes your code for errors, potential bugs, code smells, and enforces coding standards. It checks for things like unused variables, incorrect imports, and adherence to PEP8 style, and can warn about problematic code patterns.

    5.3- `format`: Automatically reformats your code to follow a consistent style (PEP8). It does not check for errors or code quality, but ensures your code layout (indentation, spacing, line length, etc.) is uniform.

    5.4- `test`: Ejecuta los tests necesarios para asegurar que cualquier modificación en el código no rompa la solución del problema que se desea resolver.







