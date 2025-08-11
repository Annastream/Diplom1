# Expected responses for user creation tests


USER_ALREADY_EXISTS = {
    "success": False,
    "message": "User already exists"
}

MISSING_FIELDS_RESPONSE = {
    "success": False,
    "message": "Email, password and name are required fields"
}

# Expected responses for order tests
ORDER_SUCCESS_RESPONSE = {
    "success": True,
    "order": {
        "ingredients": list,
        "_id": str,
        "status": str,
        "name": str,
        "createdAt": str,
        "updatedAt": str
    }
}

ORDER_MISSING_INGREDIENTS = {
    "success": False,
    "message": "Ingredient ids must be provided"
}

# Expected responses for login tests
LOGIN_SUCCESS_RESPONSE = {
    "success": True,
    "accessToken": str,
    "refreshToken": str,
    "user": {
        "email": str,
        "name": str
    }
}

INVALID_CREDENTIALS_RESPONSE = {
    "success": False,
    "message": "email or password are incorrect"
}
# Базовые настройки
BASE_URL = "https://stellarburgers.nomoreparties.site"

ENDPOINTS = {
    "register_user": f"{BASE_URL}/api/auth/register",
    "login": f"{BASE_URL}/api/auth/login",
    "logout": f"{BASE_URL}/api/auth/logout",
    "token": f"{BASE_URL}/api/auth/token",
    "user": f"{BASE_URL}/api/auth/user",
    "orders": f"{BASE_URL}/api/orders"
}

# Тестовые данные
EXISTING_USER = {
    "email": "standuppp@gmail.com",
    "password": "querty135",
    "name": "Untouchable"
}

INVALID_USER = {
    "email": "broken_leg@strange.com",
    "password": "incorrect_password"
}

MISSING_FIELDS_USER = {
    "email": "doitdoit123@google.com",
    "password": "",
    "name": "Myname"
}

INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d",  # Флюоресцентная булка R2-D3
    "61c0c5a71d1f82001bdaaa6f",  # Мясо бессмертных моллюсков Protostomia
    "61c0c5a71d1f82001bdaaa70",  # Говяжий метеорит (отбивная)
    "61c0c5a71d1f82001bdaaa71",  # Биокотлета из марсианской Магнолии
]
