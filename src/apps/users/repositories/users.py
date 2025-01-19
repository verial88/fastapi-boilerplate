from typing import Protocol, Type

from src.apps.users.enums import UsersProviderEnum
from src.apps.users.exceptions import PermissionForUserDeniedError
from src.apps.users.schemas.users import UserSchema


class UsersRepositoryProtocol(Protocol):
    async def get_users(self) -> list[UserSchema]:
        ...


class UsersRepositoryFactoryProtocol(Protocol):
    async def make(self) -> UsersRepositoryProtocol:
        ...


class UsersRepositoryImpl:
    async def get_users(self) -> list[UserSchema]:
        return [
            UserSchema(
                email='rshmelev@mail.ru',
                username='rshmelev',
                last_name='shmelev',
                first_name='roman',
            )
        ]


class UsersRepositoryRedisImpl:
    async def get_users(self) -> list[UserSchema]:
        raise PermissionForUserDeniedError()
        return [
            UserSchema(
                email='yrii@mail.ru',
                username='yriigg',
                last_name='gg',
                first_name='yrii',
            )
        ]


class UsersRepositoryFactoryImpl:
    def __init__(self, provider: UsersProviderEnum) -> None:
        self.provider = provider

    async def make(self) -> UsersRepositoryProtocol:
        providers_mapper: dict[UsersProviderEnum, Type[UsersRepositoryImpl | UsersRepositoryRedisImpl]] = {
            UsersProviderEnum.postgres: UsersRepositoryImpl,
            UsersProviderEnum.redis: UsersRepositoryRedisImpl,
        }
        return providers_mapper.get(self.provider, UsersRepositoryImpl)()
