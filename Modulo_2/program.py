# Como Crear y activar el Entorno Virtual

# Bash | Consola
# Windows
# py -m venv envmod2
# envmod2\Scripts\activate 

# Resultado: 
# (envmod2) C:\Innovaccion\Launch_X\Modulo_2>

# Paquetes Disponibles en Python (Python Package Index, o PyPi)
# https://pypi.org/

# En Jupiter Notebook un paquete se instala así: !pip install paquete

# Bash | Consola
# pip install python-dateutil

# Que paquetes están instalados en tu entorno virtual: pip freeze
# En Jupiter Notebook sería: !pip freeze
# Salida:
    # (envmod2) C:\Innovaccion\Launch_X\Modulo_2>pip freeze
    # python-dateutil==2.8.2
    # six==1.16.0

# Salir del entorno virtual: deactivate

# Instalar desde la maquina:
# cd <to where the package is on your machine>
# py -m pip install

# Instalar desde Github
# git+https://github.com/your-repo.git

# Instalar desde un archivo comprimido
# python3 -m pip install package.tar.gz
# py -m pip install package.tar.gz



