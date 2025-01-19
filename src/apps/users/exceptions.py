from src.core.exceptions import PermissionDeniedError


class PermissionForUserDeniedError(PermissionDeniedError):
    message = 'Для этого пользователя недостаточно прав на чтение'
