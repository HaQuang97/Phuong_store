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


class ImageType(Enum):
    IMAGE_TYPE_1 = 1
    IMAGE_TYPE_2 = 2
    IMAGE_TYPE_3 = 3


class OrderStatusType(Enum):
    WAIT_ACCEPT = 1
    ACCEPT = 2
    SUCCESS = 3
