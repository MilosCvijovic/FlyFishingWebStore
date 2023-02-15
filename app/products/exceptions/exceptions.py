class ProductTypeNotFoundException(Exception):
    """Exception raised when a product could not be found with the given ID."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class RodNotFoundException(Exception):
    """Exception raised when a rod could not be found with the given brand name."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ReelNotFoundException(Exception):
    """Exception raised when a rod could not be found with the given brand name."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class LineNotFoundException(Exception):
    """Exception raised when a rod could not be found with the given brand name."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class FlyNotFoundException(Exception):
    """Exception raised when a rod could not be found with the given brand name."""
    def __init__(self, message, code):
        self.message = message
        self.code = code
