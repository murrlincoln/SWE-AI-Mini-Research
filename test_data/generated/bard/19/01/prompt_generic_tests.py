def function(a: int) -> list:
  """Returns a list of all the prime numbers less than or equal to a."""
  primes = []
  for i in range(2, a + 1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
      if i % j == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(i)
  return primes
