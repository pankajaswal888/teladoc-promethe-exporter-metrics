# Teladoc Task Exporter

A Flask application that receives task statuses and exposes them as Prometheus metrics.

## Features
- REST API endpoint for task submission
- Prometheus metrics endpoint
- Docker container



### Prerequisites
- Python 3.9
- Docker


### Running Locally
1. Clone the repository:
   git clone https://github.com/pankajaswal888/teladoc-task-exporter.git
   cd teladoc-task-exporter


2. Set up virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3.Run the application

export FLASK_APP=app
export FLASK_ENV=development
flask run --port=5002

Running with Docker

docker-compose up --build


API  :

http://localhost:5002/api/tasks

Metrics: http://localhost:5002/metrics

Prometheus UI - using docker-compose : http://localhost:9090

API CURL : 


curl -X POST -H "Content-Type: application/json" -d '{
    "tool": "upgrader",
    "task": "healthcheck",
    "status": "completed",
    "duration": 120
}' http://localhost:5002/api/tasks


# To view metrics
curl http://localhost:5002/metrics

