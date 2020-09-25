class DB:
  @classmethod
  def connect(cls):
    # Connect to the database
    # Return the connection object
    pass

  @classmethod
  def setup(cls):
    # Execute the structure SQL script
    # Return value does not matter
    pass

  @classmethod
  def seed(cls):
    # Execute the seed SQL script
    # Return value does not matter
    pass

  @classmethod
  def links(cls):
    # Returns a reference to the links interface
    pass

  @classmethod
  def pages(cls):
    # Returns a reference to the pages interface
    pass
