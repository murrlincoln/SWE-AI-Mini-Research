def fibonacci(num):
    sequence = [0, 1]
    if num < 2:
        return sequence[:num]
    else:
        for i in range(2, num):
            sequence.append(sequence[i-1] + sequence[i-2])
        return sequence
