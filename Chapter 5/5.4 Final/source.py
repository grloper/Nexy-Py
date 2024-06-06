from IDIterator import IDIterator
from id_validation import check_id_valid 

def choose_method(id, method):
  """
  Selects and executes the chosen method (iterator or generator) for generating IDs.

  Args:
      id (int): The starting ID.
      method (str): "it" for iterator, "gen" for generator.

  Returns:
      None
  """
  if method == 'it':
    id_iter = IDIterator(id)  # Create an iterator instance
    for _ in range(10):
      print(next(id_iter))  # Print the next ID from the iterator
  elif method == 'gen':
    id_gen = id_generator(id)  # Create a generator instance
    for _ in range(10):
      print(next(id_gen))  # Print the next ID from the generator
  else:
    print("Invalid input")  # Handle invalid method input

def id_generator(id):
  """
  Generate a valid id using a generator.

  Args:
      id (int): The starting ID.

  Yields:
      int: A valid Israeli ID number.
  """
  while True:
    if id == 999999999:
      break  # Stop generation if ID reaches the upper limit
    if check_id_valid(id):  # Yield ID if it is valid
      yield id
    id += 1  # Increment ID for the next iteration

def main():
  """
  Prompts the user for starting ID and method (iterator or generator),
  then calls the choose_method function to handle ID generation.
  """
  _id = int(input("Enter the id: "))  # Prompt for starting ID
  gen_or_it = input("Generator or Iterator? (gen/it)? ").lower()  # Prompt for method
  choose_method(_id, gen_or_it)  # Call choose_method with user inputs

if __name__ == "__main__":
  main()  # Execute main if this script is run directly
