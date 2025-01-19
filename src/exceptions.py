"""
Модуль, содержащий глобальные обработчики исключений.
"""

from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.exception_handlers import http_exception_handler

from src.core.exceptions import (
    ModelAlreadyExistsError,
    PermissionDeniedError,
    SortingFieldNotFoundError,
    ValidationError,
)


async def permission_denied_error_handler(request: Request, error: PermissionDeniedError) -> Response:
    """
    Обработчик ошибки, возникающей при недостатке прав для выполнения действия.
    """
    return await http_exception_handler(request, HTTPException(status.HTTP_403_FORBIDDEN, error.message))


async def model_already_exists_error_handler(request: Request, error: ModelAlreadyExistsError) -> Response:
    """
    Обработчик ошибки, возникающей при попытке создать модель с существующим уникальным полем.
    """
    return await http_exception_handler(
        request,
        HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                'field': error.field,
                'message': error.message,
            },
        ),
    )


async def sorting_field_not_fount_error_handler(request: Request, error: SortingFieldNotFoundError) -> Response:
    """
    Обработчик ошибки, возникающей при невозможности найти поле для сортировки.
    """
    return await http_exception_handler(request, HTTPException(status.HTTP_400_BAD_REQUEST, error.message))


async def validation_error_handler(request: Request, error: ValidationError) -> Response:
    """
    Обработчик ошибки валидации.
    """
    return await http_exception_handler(
        request,
        HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                'field': error.field,
                'message': error.message,
            },
        ),
    )


def apply_exceptions_handlers(app: FastAPI) -> FastAPI:
    """
    Применяем глобальные обработчики исключений.
    """
    app.exception_handler(PermissionDeniedError)(permission_denied_error_handler)
    app.exception_handler(ModelAlreadyExistsError)(model_already_exists_error_handler)
    app.exception_handler(SortingFieldNotFoundError)(sorting_field_not_fount_error_handler)
    app.exception_handler(ValidationError)(validation_error_handler)
    return app
