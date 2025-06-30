from httpx import Response

from typing import TypedDict

from clients.api_client import ApiClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class Exercise(TypedDict):
    """
    Описание структуры задания
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения заданий
    """
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа для получения задания.
    """
    exercise: Exercise


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов.
    """
    courseId: str


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа для создания задания.
    """
    exercise: Exercise


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа для обновления задания.
    """
    exercise: Exercise


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на изменение курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(ApiClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод для получения списка упражнений.
        :param query: Словарь, содержащий courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получения упражнения по его id.
        :param exercise_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод для создания упражнения.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод для точечного изменения упражнения.
        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления упражнения
        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создания экземпляра ExercisesClient c уже настроенным HTTPX-клиентом.
    :param user: Словарь, содержащий username и password.
    :return: Готовый к использованию ExercisesClient.
    """
    client = get_private_http_client(user)
    return ExercisesClient(client)