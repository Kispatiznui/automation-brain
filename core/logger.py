import datetime

def log(action, status, result):
    print({
        "time": str(datetime.datetime.now()),
        "action": action,
        "status": status,
        "result": result
    })
