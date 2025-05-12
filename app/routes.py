from flask import request, jsonify
from .exporter import TaskExporter
from .models import Task
from prometheus_client import generate_latest
from flask import Response

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
                }), 400
                
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
            }), 200
            
        except ValueError as e:
            return jsonify({
                "status": "error",
                "message": f"Validation error: {str(e)}"
            }), 400
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": f"Server error: {str(e)}"
            }), 500

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
