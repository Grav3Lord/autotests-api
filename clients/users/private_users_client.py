from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema

from httpx import Response

from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema


class PrivateUsersClient(APIClient):
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

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод частичного обновления пользователя по его id.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь содержащий email & separated fullname.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            f"/api/v1/users/{user_id}",
            json=request.model_dump(by_alias=True)
        )

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод для удаления пользователя по его id.

        :param user_id: Идентификатор пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_users_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))