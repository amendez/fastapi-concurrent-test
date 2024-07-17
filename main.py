from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()

async def fetch_data(client, url):
    response = await client.get(url, timeout=20.0)
    return response.json()

@app.get("/")
async def hello_world():
    urls = [
        "https://httpbin.org/delay/10",
        "https://httpbin.org/delay/10",
        "https://httpbin.org/delay/10",
        "https://httpbin.org/delay/10",
        "https://httpbin.org/delay/10",
        "https://httpbin.org/delay/10",
    ]

    async with httpx.AsyncClient() as client:
        tasks = [fetch_data(client, url) for url in urls]
        results = await asyncio.gather(*tasks)

    return {"message": "Hello, World!", "results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)