from typing import List, Tuple

from errors import FilterError
from models import BaseFilter


class OrderByFilter(BaseFilter):
    def __init__(self, lines: List[List[str]], header_line: List[str], target: str):
        self.lines = lines
        self.target = target
        self.header_line = header_line

    def _check(self) -> Tuple[int, str]:
        if self.target.count('=') == 1:
            target_header, target = self.target.split("=")
            if target_header in self.header_line:
                if target in ("asc", "desc"):
                    return self.header_line.index(target_header), target
                else:
                    raise FilterError(
                        "Это действие нельзя использовать",
                        f"Разрешены только asc & desc"
                    )
            else:
                raise FilterError(
                    reason = f"Атрибута {target_header} нет среди {self.header_line}"
                )
        else:
            raise FilterError(
                reason = f"Неккоректный синтаксис в выражении {self.target}"            
            )

    def get(self) -> List[List[str]]:
        index, target = self._check()
        match target:
            case 'asc':
               result = sorted(self.lines)
            case 'desc':
                result = sorted(self.lines, reverse=True)
        return result