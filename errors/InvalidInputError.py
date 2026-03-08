class InvalidInputError(Exception):
    """Exception raised for invalid input
      Attributes:
          expression -- input expression that caused the error
          message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

