
import json
from datetime import datetime


def log(msg:str):
    try:
        data = json.loads(msg)
        print(json.dumps(data, indent=2))

    except:
        print(msg)


# def log(*values: object):
#     now = datetime.now()
#     log_time = now.strftime("%Y-%m-%d %H:%M:%S")
#     print(log_time, values)
