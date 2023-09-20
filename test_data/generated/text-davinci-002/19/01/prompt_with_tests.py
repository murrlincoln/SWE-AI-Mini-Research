def fibonacci(num): 
    if num<0: 
        print("Incorrect input") 
    elif num==1: 
        return [0]
    elif num==2: 
        return [0,1]
    else: 
        fib = [0,1]
        for i in range(2,num): 
            fib.append(fib[i-1]+fib[i-2])
        return fib