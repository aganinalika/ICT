from fastapi import FastAPI
import uvicorn

app_p2 = FastAPI()

@app_p2.get("/")
def root():
    response = requests.get(url)
    response_value = response.json()
    return f"{response_value}"

if __name__ == "__main__":
    uvicorn.run("app:app_p2", host='0.0.0.0', port=80, reload=True)