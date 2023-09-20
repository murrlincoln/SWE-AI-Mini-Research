def test_4():
 input = 4
 assert function(input) == 4
def Fizz_Buzz(num):

    # Condition for FizzBuzz
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"

    # Condition for fizz
    elif num % 3 == 0:
        return "Fizz"

    # Condition for buzz
    elif num % 5 == 0:
        return "Buzz"

    else:
        return num