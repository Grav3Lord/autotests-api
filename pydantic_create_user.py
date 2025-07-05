from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """
        Представление пользователя, возвращаемого в ответе API.

        Поля:
            - id: Уникальный идентификатор пользователя.
            - email: Адрес электронной почты пользователя.
            - last_name: Фамилия пользователя.
            - first_name: Имя пользователя.
            - middle_name: Отчество пользователя.
        """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_username(self) -> str:
        """
        Метод получения имени и фамилии пользователя.
        :return: Строчное значение полного имени пользователя в формате: <Имя> <Фамилия>.
        """
        return f"{self.first_name} {self.last_name}"


class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса на создание пользователя.

    Поля:
        - email: Адрес электронной почты пользователя.
        - password: Пароль пользователя.
        - last_name: Фамилия пользователя.
        - first_name: Имя пользователя.
        - middle_name: Отчество пользователя.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа на запрос создания пользователя.

    Поля:
        - user: Объект, содержащий информацию о пользователе.
    """
    user: UserSchema
