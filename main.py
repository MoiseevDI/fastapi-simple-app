from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/3060stats")
async def root():
    raw = requests.get("https://api.minerstat.com/v2/hardware?type=gpu")
    stat_3060 = {}
    for item in raw.content:
        if item["url"] == "nvidia-gtx-3060":
            stat_3060 = item
    return {"message": stat_3060}
