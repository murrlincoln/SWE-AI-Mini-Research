def function(a: str) -> str:
    for char in a:
        if a.count(char) == 2:
            return char
