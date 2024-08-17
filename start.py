import uvicorn
import logging


if __name__ == "__main__":
    uvicorn.run("config:scrap_api", host="localhost", port=8001, reload=True)
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename='./logs/app-logs.log')