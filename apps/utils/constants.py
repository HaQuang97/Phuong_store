from enum import Enum


class GenderType(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3


class Error:
    Code = "code"
    Message = "message"


class UserStatus(Enum):
    ACTIVE = 1
    POLICY_VIOLATION = 2
