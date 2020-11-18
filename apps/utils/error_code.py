class Error:
    code = "code"
    message = "message"


class ErrorCode:
    not_error = {
        Error.code: 0,
        Error.message: "Successful"
    }
    unknown_error = {
        Error.code: 1,
        Error.message: "Unknown Error"
    }
    error_json_parser = {
        Error.code: 2,
        Error.message: "Can't parse data please check data"
    }
    wrong_email = {
        Error.code: 3,
        Error.message: 'Wrong email format',
    }
    not_exist_email = {
        Error.code: 3,
        Error.message: 'Email not found',
    }
    account_has_exist = {
        Error.code: 4,
        Error.message: 'Email exist in server'
    }
    not_found_record = {
        Error.code: 5,
        Error.message: 'Not found record'
    }
    error_not_auth = {
        Error.code: 6,
        Error.message: "Need login to using this function"
    }
    invalid_auth = {
        Error.code: 7,
        Error.message: "Invalid auth"
    }
    birthday_invalid_format = {
        Error.code: 8,
        Error.message: "birthday invalid format",
    }
    birthday_invalid_date = {
        Error.code: 9,
        Error.message: "Birth day error",
    }
    line_error_server = {
        Error.code: 10,
        Error.message: 'Can\'t not connect line serrver',
    }
    login_via_line_error = {
        Error.code: 11,
        Error.message: 'Login with line error',
    }
    link_invalid = {
        Error.code: 12,
        Error.message: 'Invalid link',
    }
    password_invalid = {
        Error.code: 13,
        Error.message: 'Password invalid'
    }
