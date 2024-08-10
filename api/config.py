from fastapi import FastAPI


scrapapi = FastAPI()




@scrapapi.get("/")
async def test():
    return { "hello" : "world"}