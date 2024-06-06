def check_id_valid(id_number):
  """
  Checks if the given ID number is a valid Israeli ID number.

  Args:
      id_number (int): The ID number to check.

  Returns:
      bool: True if the ID number is valid, False otherwise.
  """

  if not isinstance(id_number, int) or len(str(id_number)) != 9:
    return False

  # Convert ID number to string and split into digits
  digits = [int(d) for d in str(id_number)]

  # Multiply digits by 1 or 2 based on position
  weighted_digits = [d * (2 if i % 2 else 1) for i, d in enumerate(digits)]

  # Add digits of numbers greater than 9
  for i, d in enumerate(weighted_digits):
    if d > 9:
      weighted_digits[i] = d // 10 + d % 10

  # Sum the weighted digits
  sum_weighted_digits = sum(weighted_digits)

  # Check if the sum is divisible by 10
  return sum_weighted_digits % 10 == 0
