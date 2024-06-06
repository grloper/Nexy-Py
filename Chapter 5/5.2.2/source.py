numbers = iter(list(range(1, 101)))

while True:
  try:
    # Skip first two numbers
    next(numbers)
    next(numbers)

    # Print current number
    print(next(numbers))

  except StopIteration:
    break
