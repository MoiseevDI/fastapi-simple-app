from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("newssa")
async def root():
    raw = requests.get("http://logic/v1alpha/newsanalyses")
    return raw.json()
