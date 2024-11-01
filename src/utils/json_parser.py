import json

def safe_parse(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        return None