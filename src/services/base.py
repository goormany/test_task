from src.utils.db_manager import DBManager


class BaseServices:
    def __init__(self, db: DBManager | None = None) -> None:
        self.db = db