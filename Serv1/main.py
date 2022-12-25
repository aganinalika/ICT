from fastapi import FastAPI
import requests
import os
import datetime
import uvicorn

app_p1 = FastAPI(openapi_url=f"/api/v1/project1/openapi.json", docs_url="/api/v1/project1/docs")

@app_p1.get("/")
def root():
    return {"message": "Hello world"}

       
if __name__ == "__main__":
    uvicorn.run("app:app_p1", host='0.0.0.0', port=80, reload=True)