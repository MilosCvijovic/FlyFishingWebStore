class ProductNotFoundException(Exception):
    """Exception raised when a product could not be found with the given ID."""
    def __init__(self, message, code):
        self.message = message
        self.code = code
