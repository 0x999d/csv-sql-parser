from typing import Optional


class FilterError(BaseException):
    def __init__(self, message: Optional[str] = "Атрибута нет в csv", reason: str = Optional[None]):
        self.message = message
        self.reason = reason
        super().__init__(message)

    def __str__(self) -> str:
        return f"Error {self.message} caused by {self.reason}"