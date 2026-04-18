from app.core.router import ACTIONS
from app.core.logger import log

class TaskExecutor:

    def execute(self, action, params):

        if action not in ACTIONS:
            return {
                "status": "error",
                "message": "Unknown action"
            }

        try:
            result = ACTIONS[action](**params)
            status = "success"
        except Exception as e:
            result = str(e)
            status = "failed"

        log(action, status, result)

        return {
            "status": status,
            "result": result
        }
