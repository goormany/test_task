class BaseException(Exception):
    detail = "Неожиданная ошибка"
    
    def __init__(self, *args, **kwargs):
        super().__init__(self.detail, *args, **kwargs)
        
class ObjNotFoundException(BaseException):
    detail = "Объект не найден"

class TeamNotFoundException(ObjNotFoundException):
    detail = "Команда не найдена"