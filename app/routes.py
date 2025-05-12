# Import Flask web framework components
from flask import request, jsonify, Response

# Import application components
from .exporter import TaskExporter  # Metrics recording
from .models import Task  # Data validation model

# Import Prometheus metrics generator
from prometheus_client import generate_latest

# Initialize the metrics exporter as a singleton

exporter = TaskExporter()

def init_routes(app):
    @app.route('/api/tasks', methods=['GET', 'POST'])
    def handle_tasks():
        if request.method == 'GET':
            return jsonify({
                "message": "Send POST requests with task data",
                "example_request": {
                    "tool": "upgrader",
                    "task": "healthcheck",
                    "status": "completed",
                    "duration": 120
                }
            })
            
        # POST request handling
        try:
            data = request.get_json()
            
            if not data:
                return jsonify({
                    "status": "error",
                    "message": "No data provided"
                }), 400 # HTTP 400 Bad Request
                
            task = Task.from_dict(data)
            exporter.process_task(task)
            
            return jsonify({
                "status": "success",
                "message": "Task recorded",
                "data": {
                    "tool": task.tool,
                    "task": task.task,
                    "status": task.status.value,
                    "duration": task.duration
                }
            }), 200 # HTTP 200 OK
            
        except ValueError as e:
            return jsonify({
                "status": "error",
                "message": f"Validation error: {str(e)}"
            }), 400
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": f"Server error: {str(e)}"
            }), 500 # HTTP 500 Internal Server Error

    @app.route('/metrics')
    def metrics():
        return Response(
            generate_latest(),
            mimetype="text/plain"
        )

    @app.route('/')
    def home():
        return jsonify({
            "message": "Teladoc Task Exporter",
            "endpoints": {
                "/api/tasks": "POST task data",
                "/metrics": "Prometheus metrics"
            }
        })
