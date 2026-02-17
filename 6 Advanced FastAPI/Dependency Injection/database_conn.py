from fastapi import FastAPI ,Depends

app = FastAPI()



# dependency function
def get_db():
    db = {"conn":"mock database connection"}
    try:
        yield db
    finally:
        db.close()



#  endpoint
@app.get('/home')
def home(db = Depends(get_db)):
    return {"db_statues":db['conn']}
