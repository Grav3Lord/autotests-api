from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict

class UpdateUserRequest(TypedDict):
    """Описание структуры запросов на обновление пользователя"""

    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(ApiClient):
    """
    Клиент для работы с /api/v1/users
    """

    def get_get_users_me(self) -> Response:
        """
        Метод для получения инфморации о текущем пользователе

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_get_users_api(self, user_id: str) -> Response:
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