1) Ejecutar [pip install pipenv] para instalar pipenv
2) Ejecuta [python -m pipenv install emoji] para instalar el paquete de forma virtual, en este caso requests
3) Para ejecutar el emoji_file.py

    * python -m pipenv shell
    * python .\emoji_file.py

    Tambien funciona

    * python -m pipenv run python .\emoji_file.py

    RESULTADO ==> Python es 🔥

Esto debido a que la librería emoji se instaló unicamente en el espacio virtual