from typing import Annotated

from fastapi import Depends

from src.apps.users.enums import UsersProviderEnum
from src.apps.users.repositories.users import UsersRepositoryFactoryImpl, UsersRepositoryFactoryProtocol

from .services import UsersServiceImpl, UsersServiceProtocol
from .use_cases import UsersUseCaseImpl, UsersUseCaseProtocol

# --- repositories ---


def get_users_repository_factory(provider: UsersProviderEnum) -> UsersRepositoryFactoryProtocol:
    return UsersRepositoryFactoryImpl(provider)


UsersRepositoryFactory = Annotated[UsersRepositoryFactoryProtocol, Depends(get_users_repository_factory)]


# --- services ---


def get_users_service(users_repository_factory: UsersRepositoryFactory) -> UsersServiceProtocol:
    return UsersServiceImpl(users_repository_factory)


UsersService = Annotated[UsersServiceProtocol, Depends(get_users_service)]


# --- use_cases ---


def get_users_use_case(users_service: UsersService) -> UsersUseCaseProtocol:
    return UsersUseCaseImpl(users_service)


UsersUseCase = Annotated[UsersUseCaseProtocol, Depends(get_users_use_case)]
