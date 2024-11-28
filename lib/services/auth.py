import bcrypt

PLACEHOLDER_USERNAME = "admin"
PLACEHOLDER_PASSWORD_HASH = b'$2b$12$EULT1/ZezvBbxsu7snAfA.beZ1cy65NtZ9uFZKmgN5IdezA/5tYvG'


class AuthService():
    """ Placeholder Auth Service """

    @staticmethod
    def authenticate(username: str, password: str):
        password_bytes: bytes = password.encode("utf-8")
        return username == PLACEHOLDER_USERNAME and bcrypt.checkpw(password_bytes, PLACEHOLDER_PASSWORD_HASH)
