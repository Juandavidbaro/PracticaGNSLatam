# PracticaGNSLatam

Este proyecto es una API RESTful desarrollada con FastAPI que permite crear, consultar y buscar ítems con atributos como nombre, precio, descripción y disponibilidad.

## Cómo ejecutar

### Requisitos
- Python 3.11+
- Docker (opcional)
- Git
- Postman (para pruebas manuales)

## Instalación y ejecución
git clone https://github.com/Juandavidbaro/PracticaGNSLatam.git

cd PRACTICAGNSLATAM

python -m venv venv

source venv/bin/activate   

pip install -r requirements.txt

uvicorn app:app --reload´´´

## ejecución en Docker

docker build -t practica-gns .

docker run -d -p 8000:8000 practica-gns

## Endpoints disponibles

Base URL: http://localhost:8000/items

1. crear un nuevo item:
- Método POST
- Cuerpo (JSON)
{
  "nombre": "Bicicleta",
  "precio": 200000.0,
  "descripcion": "Bicicleta de montaña con suspensión delantera",
  "disponibilidad": true
}

{
  "nombre": "Balón",
  "precio": 40000.0,
  "descripcion": "Balón de fútbol",
  "disponibilidad": true
}

2. Obtener todos los items
- Método GET
- Cuerpo (ninguno)

3. Obtener un item por ID
- Método GET
- Endpoint: /items/{item_id}

Ejemplo:
GET http://localhost:8000/items/a35d4d8f-b6e9-4f21-8e30-67b6e9fc6530

