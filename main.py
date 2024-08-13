import uvicorn

if __name__ == "__main__":
    uvicorn.run("config:scrap_api", host="localhost", port=8001, reload=True)