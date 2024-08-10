import uvicorn


if __name__ == "__main__":
    uvicorn.run("config:scrapapi", host="localhost", port=8001, reload=True)