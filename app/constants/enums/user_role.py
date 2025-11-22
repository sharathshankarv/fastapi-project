from enum import Enum

class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"
    SUPPLIER = "supplier"
    EMPLOYEE = "employee"