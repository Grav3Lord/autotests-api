from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient
from clients.files.files_client import File
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
from clients.users.private_users_client import User


class Course(TypedDict):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User


class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str

class CreateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class CreateCourseResponseDict(TypedDict):
    """
    Описание структуры ответа создания курса.
    """
    course: Course

class UpdateCoursesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(ApiClient):
    """
    Клиент для работы с /api/v1/courses.
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод для получения списка курсов.
        :param query: Словарь, содержащий userId.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get("/api/v1/courses", params=query)

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод для создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для получения курса по его id.
        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request: UpdateCoursesRequestDict) -> Response:
        """
        Метод для точечного изменения курса по его id.
        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод для удаления курса по его id.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        response = self.create_course_api(request)
        return response.json()


def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))