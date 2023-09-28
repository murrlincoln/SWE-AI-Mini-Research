def function(a: int) -> str:
    if a % 3 == 0 and a % 5 == 0:
        return 'FizzBuzz'
    elif a % 3 == 0:
        return 'Fizz'
    elif a % 5 == 0:
        return 'Buzz'
    else:
        return str(a)
