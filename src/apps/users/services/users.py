from typing import Protocol

from src.apps.users.repositories.users import UsersRepositoryFactoryProtocol
from src.apps.users.schemas.users import UserSchema


class UsersServiceProtocol(Protocol):
    async def get_users(self) -> list[UserSchema]:
        ...


class UsersServiceImpl:
    def __init__(self, users_repository_factory: UsersRepositoryFactoryProtocol) -> None:
        self.users_repository_factory = users_repository_factory

    async def get_users(self) -> list[UserSchema]:
        """Получения пользователей

        Тут бывает логика по созданию репозитория или сервиса.

        Returns:
            list[UserSchema]: _description_
        """
        users_repository = await self.users_repository_factory.make()
        return await users_repository.get_users()
