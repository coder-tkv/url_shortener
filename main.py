from fastapi import FastAPI

app = FastAPI()

@app.post('/short_url')
async def generate_short_url():
    return ...

@app.get('/{slug}')
async def redirect_to_url(slug: str):
    return ... # redirect
