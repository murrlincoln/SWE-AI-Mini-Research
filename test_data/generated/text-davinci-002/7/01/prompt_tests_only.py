assert range_bitwise_and(1, 1) == 1
  assert range_bitwise_and(2147483647, 2147483647) == 2147483647
  assert range_bitwise_and(1, 2147483647) == 0

def range_bitwise_and(m, n):
  count = 0
  while m != n:
    m >>= 1
    n >>= 1
    count += 1
  return m << count