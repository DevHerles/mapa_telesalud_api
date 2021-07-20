from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware
from middlewares import request_handler

app = FastAPI()
app.middleware("http")(request_handler)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/departments')
def departments():
    file = open('departments.json')
    data = json.load(file)
    return data


@app.get('/api/CentroVacunacionGis/DepartamentoPuntos')
def department_points():
    file = open('department_points.json')
    data = json.load(file)
    return data


@app.get('/api/CentroVacunacionGis/ProvinciasPuntos')
def province_points():
    file = open('province_points.json')
    data = json.load(file)
    return data


@app.get('/api/CentroVacunacionGis/DistritosPuntos')
def district_points():
    file = open('district_points.json')
    data = json.load(file)
    return data


@app.get('/api/CentroVacunacionGis/Puntos')
def points():
    file = open('points.json')
    data = json.load(file)
    return data


@app.get('/')
def index():
    return '(c) MINSA - 2021'
