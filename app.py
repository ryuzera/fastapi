import uvicorn  # ->> Uvicorn é um servidor ASGI para Python, usado para rodar aplicações web assíncronas, como as construídas com FastAPI. Ele é rápido e eficiente, permitindo que você execute sua aplicação de forma assíncrona e escalável.
from fastapi import FastAPI

app = FastAPI()

@app.get("/saudar/{nome}")
async def saudar(nome: str):
    print(type(nome))
    return {"mensagem": f"Olá, {nome}!"}

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=3001,
        reload=True
    )