from clients.api_client import ApiClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict

from httpx import Response
from typing import TypedDict


class UpdateUserRequest(TypedDict):
    """Описание структуры запросов на обновление пользователя"""

    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


# Добавили описание структуры пользователя
class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


# Добавили описание структуры ответа получения пользователя
class GetUserResponseDict(TypedDict):
    """
    Описание структуры ответа получения пользователя.
    """
    user: User


class PrivateUsersClient(ApiClient):
    """
    Клиент для работы с /api/v1/users
    """

    def get_users_me(self) -> Response:
        """
        Метод для получения инфморации о текущем пользователе

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_users_api(self, user_id: str) -> Response:
        """
        Метод для получения информации о пользователе по его id.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequest) -> Response:
        """
        Метод частичного обновления пользователя по его id.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь содержащий email & separated fullname.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод для удаления пользователя по его id.

        :param user_id: Идентификатор пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_users_api(user_id)
        return response.json()


def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))