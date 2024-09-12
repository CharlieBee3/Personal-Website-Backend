# here write the fastapi code
# to run 'poetry run python etc. etc.' 
# make sure you develop with --reload 

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}



    