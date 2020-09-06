import json
from pathlib import Path
from typing import Optional


def checkSwitch(funcName: str):
    file = Path('.') / 'nana' / 'plugins' / 'switch' / 'switch.json'
    with open(file, 'r') as f:
        data = json.load(f)
    
    if data[funcName] == "on":
        return True

def checkNoob(user: int, group: Optional[int] = None):
    fileU = Path('.') / 'nana' / 'plugins' / 'noobList' / 'noobList.json'
    fileG = Path('.') / 'nana' / 'plugins' / 'noobList' / 'noobGroup.json'
    try:
        with open(fileU, 'r') as f:
            dataU = json.load(f)
    except:
        dataU = {}

    try:
        with open(fileG, 'r') as f:
            dataG = json.load(f)
    except:
        dataG = {}

    if str(user) not in dataU.keys():
        if group:
            if str(group) not in dataG.keys():
                return True
        else:
            return True
    else:
        pass