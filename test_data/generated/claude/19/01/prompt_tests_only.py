def fibonacci(num: int) -> List[int]:
	if num == 0:
		return [0]
	sequence = [0, 1]
	if num == 1:
		return sequence
	for i in range(2, num+1):
		next_num = sequence[i-1] + sequence[i-2]
		sequence.append(next_num)
	return sequence
