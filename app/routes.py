from flask import request, jsonify
from app.ai.parser import parse_command
from app.core.executor import TaskExecutor

executor = TaskExecutor()

def register_routes(app):

    @app.route("/command", methods=["POST"])
    def command():
        data = request.json
        user_input = data.get("input")

        parsed = parse_command(user_input)

        result = executor.execute(
            parsed["action"],
            parsed["params"]
        )

        return jsonify({
            "input": user_input,
            "parsed": parsed,
            "result": result
        })
