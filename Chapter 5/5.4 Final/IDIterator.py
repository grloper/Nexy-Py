
from id_validation import check_id_valid

class IDIterator:
  """
  Iterator class for generating valid Israeli IDs.
  """
  def __init__(self, id=0):
    """
    Initialize the iterator with a starting ID.

    Args:
        id (int): The starting ID. Must be an integer between 0 and 999999999.
    """
    if not isinstance(id, int) or id < 0 or id > 999999999:
      raise ValueError("id must be an integer between 0 and 999999999")
    self._id = id  # Use single underscore for consistency

  def __iter__(self):
    return self  # Return the iterator object

  def __next__(self):
    """
    Returns the next valid ID.

    Returns:
        int: The next valid Israeli ID number.

    Raises:
        StopIteration: If the ID exceeds the maximum limit.
    """
    while True:
      if self._id > 999999999:
        raise StopIteration  # Stop iteration if ID exceeds the upper limit
      self._id += 1  # Directly increment self._id
      if check_id_valid(self._id):  # Use self._id for validation
        return self._id  # Return the valid ID