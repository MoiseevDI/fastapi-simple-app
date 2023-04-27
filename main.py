from fastapi import FastAPI
import requests
from pprint import pprint

app = FastAPI()

@app.get("/newssa")
async def root():
    raw = requests.get("http://logic/v1/newsanalyses")
    pprint(raw.json())
    return raw.json()
