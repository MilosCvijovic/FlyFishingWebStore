class CartItemNotFoundException(Exception):
    """Exception raised when a rod could not be found with the given brand name."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ShoppingCartNotFoundException(Exception):
    """Exception raised when a rod could not be found with the given brand name."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class OrderNotFoundException(Exception):
    """Exception raised when a rod could not be found with the given brand name."""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class OrderAlreadySentException(Exception):
    """Exception raised when a rod could not be found with the given brand name."""

    def __init__(self, message, code):
        self.message = message
        self.code = code
