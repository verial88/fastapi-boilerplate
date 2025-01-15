from enum import StrEnum, auto


class UsersProviderEnum(StrEnum):
    postges = auto()
    redis = auto()
