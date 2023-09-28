import re

def function(a: str) -> bool:
    return bool(re.match(r'[\w\.-]+@[\w\.-]+\.\w+', a))
