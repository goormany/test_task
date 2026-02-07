from fastapi import HTTPException

class BaseHTTPException(HTTPException):
    detail = "Неожиданная ошибка"
    status_code = 500
    
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class TeamNotFoundHTTPException(BaseHTTPException):
    detail = "Не найдена команда"
    status_code = 404