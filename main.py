from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from engine import MotorInferência

app = FastAPI()
templates = Jinja2Templates(directory="templates")
motor = MotorInferência()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/recomendar", response_class=HTMLResponse)
async def recomendar(request: Request, biotipo: str = Form(...), objetivo: str = Form(...)):
    # Base de Fatos: Estado atual alimentado pelo usuário [cite: 23, 24]
    fatos_usuario = {
        "biotipo": biotipo,
        "objetivo": objetivo
    }
    
    resultados = motor.inferir(fatos_usuario)
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "resultados": resultados,
        "fatos": fatos_usuario
    })