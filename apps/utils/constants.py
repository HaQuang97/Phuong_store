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
    INIT = 0
    PAYMENT_SUCCESS = 1
    PAYMENT_FAIL = 2
    DELIVERING = 3
    COMPLETED = 4
    REFUND = 5


class PaymentStatusType(Enum):
    SUCCESS = 1
    FAILURE = 2


class AuthType(Enum):
    ACTIVATION = 1
    FORGOT_PASSWORD = 2
