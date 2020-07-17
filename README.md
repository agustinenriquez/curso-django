# curso-django

Cada clase tiene un branch asignado.

Instalacion:

    git clone https://github.com/m0tz/curso-django/
    virtualenv -p python3.8 env
    git checkout clase1
    pip install -r requirements.txt
    code .

En VSCODE:

    Seleccionar el manage.py (puede que el instellisense tarde en cargar por ser la primera vez).
    Apretar F5 (comando para levantar django)
    Si aparece el mensaje:
        Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
    Entonces:
        Control + Shift + P y escribir interpreter
        Seleccionar Python: select interpreter
        Seleccionar:
            Python 3.8.2 64bit ('env', venv)
            ./env/bin/python
    Apretar F5

    Si no funciona crear una carpeta en el root llamada .vscode
    Ahi crear un archivo llamado launch.json
    Debe tener este contenido:
        {
            "configurations": [
                {
                    "name": "Python: Django",
                    "type": "python",
                    "request": "launch",
                    "program": "${workspaceFolder}/manage.py",
                    "args": [
                        "runserver",
                        "--noreload"
                    ],
                    "django": true
                }
            ]
        }
    Apretar F5

    Deberias ver en terminal (si no ves una terminal anda a Terminal -> nueva terminal)

    Output:
        System check identified no issues (0 silenced).
        July 17, 2020 - 17:15:26
        Django version 3.0.8, using settings 'tienda.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CONTROL-C.

Deberias tener el tree asi:

![alt text](https://github.com/m0tz/curso-django/blob/clase2/img/tree.png?raw=true)
