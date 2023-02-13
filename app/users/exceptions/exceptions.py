class EmployeeNotFoundException(Exception):
    """Exception raised when an employee could not be found with the given ID."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class EmployeeTypeNotFoundException(Exception):
    """Exception raised when an employee type could not be found with the given ID."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class EmployeeTypeExistsException(Exception):
    """Exception raised when an employee type already exists with the given name."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserInvalidPassword(Exception):
    """Exception raised when a user attempts to log in with an invalid password."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotSuperUser(Exception):
    """Exception raised when a user does not have superuser privileges."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CustomerNotFoundException(Exception):
    """Exception raised when a customer could not be found with the given ID."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CustomerExistsException(Exception):
    """Exception raised when a customer already exists with the given ID."""
    def __init__(self, message, code):
        self.message = message
        self.code = code

