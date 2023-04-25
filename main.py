from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/3060stats")
async def root():
    raw = requests.get("https://minerstat/v2/hardware?type=gpu")
    stat_3060 = {}
    for item in raw.json():
        if item["url"] == "nvidia-rtx-3060":
            stat_3060 = item['specs']
    return stat_3060
