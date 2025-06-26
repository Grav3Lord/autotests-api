from httpx import Response
from typing import TypedDict

from clients.api_client import ApiClient

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание нового пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(ApiClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создание нового пользователя.

        :param request: Данные для создания пользователя, включающие email, password и separated fullname.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.post("api/v1/users", json=request)