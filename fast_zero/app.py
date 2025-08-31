from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app: FastAPI = FastAPI()


# expoe a funcao para ser servida pelo objeto app
@app.get('/', status_code=200, response_model=Message)
def read_root() -> dict[str, str]:
    # o fastapi é um framework web baseado em funcoes
    return {'message': 'hello world!'}


@app.get('/teste-html', response_class=HTMLResponse)
async def exercicio_aula_2():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nosso Ola mundo</title>
</head>
<body>
<h1>Olá Mundo</h1>
</body>
</html>
    """
