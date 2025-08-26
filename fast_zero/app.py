from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get('/')  # expoe a funcao para ser servida pelo objeto app
def read_root() -> dict[str, str]:
    # o fastapi é um framework web baseado em funcoes
    return {'message': 'hello world!'}
