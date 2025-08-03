

BASE_URL = "https://stellarburgers.nomoreparties.site"

ENDPOINTS = {
    "register_user": f"{BASE_URL}/api/auth/register",
    "login": f"{BASE_URL}/api/auth/login",
    "logout": f"{BASE_URL}/api/auth/logout",
    "token": f"{BASE_URL}/api/auth/token",
    "user": f"{BASE_URL}/api/auth/user",
    "orders": f"{BASE_URL}/api/orders"
}

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
