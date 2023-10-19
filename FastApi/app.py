from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
from GetPrediction import predModel


app = FastAPI()

templates = Jinja2Templates(directory="templates")



class ValidateData(BaseModel):
    model:str
    preg:float
    plas:float
    pres:float
    skin:float
    test:float
    mass:float
    pedi:float
    age:float



@app.get('/project1/predict')
def home(request:Request):
    data=None
    return templates.TemplateResponse('index.html', {"data":data, 'request':request})

@app.get('/api/v1/project1/predict')
def predict(model:str, preg:float, plas:float, pres:float, skin:float, test:float, mass:float, pedi:float, age:float):
    data =  {
        'model':model,
        'preg':preg,
        'plas':plas,
        'pres':pres,
        'skin':skin,
        'test':test,
        'mass':mass,
        'pedi':pedi,
        'age': age
    }
    #d = ValidateData(**data)
    return predModel(data)
@app.get('/api/v1/project2/predict')
def predict():
    return {'status': 200, "message": "coming soon"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)