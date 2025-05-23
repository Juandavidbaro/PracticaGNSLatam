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

