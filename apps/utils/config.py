class Config:
    MIN_MEMBER = 500


class AvatarDefault:
    avatar_default = ['avatars/nurse-user01.png', 'avatars/nurse-user02.png', 'avatars/nurse-user03.png',
                      'avatars/nurse-user04.png', 'avatars/nurse-user05.png']


class Region:
    nationwide = '全国対応'


class PasswordRegex:
    password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d!@#$%^&*?]{8,50}$"


class OTPCode:
    otp_string = "0123456789"
    timeout_auth_code = 15


class MailSubject:
    activation = 'ACTIVE'
    forgot_password = 'FORGOTPASSWORD'
