from typing import List, Tuple

from errors import FilterError
from models import BaseFilter


class AggregateFilter(BaseFilter):
    
    ALLOWED_ACTIONS = 'max', 'min', 'avg'

    def __init__(self, lines: List[List[str]], header_line: List[str], target: str):
        self.lines = lines
        self.target = target
        self.header_line = header_line

        self.ACTION_ROUTER = {
        'max': max,
        'min': min,
        'avg': self._avg
    }

    def _check(self) -> Tuple[int, str]:
        if self.target.count('=') == 1:
            target_header, target = self.target.split("=")
            if target_header in self.header_line:
                if target in self.ALLOWED_ACTIONS:
                    return self.header_line.index(target_header), target
                else:
                    raise FilterError(
                        "Это действие нельзя использовать",
                        f"Разрешены только {self.ALLOWED_ACTIONS}"
                    )
            else:
                raise FilterError(
                    reason = f"Атрибута {target_header} нет среди {self.header_line}"
                )
        else:
            raise FilterError(
                reason = f"Неккоректный синтаксис в выражении {self.target}"            
            )

    @staticmethod
    def _avg(obj: List[int]) -> int:
        return round(sum(obj) / len(obj), 2)

    def get(self) -> Tuple[List[List[str]], List[str]]:
        index, target = self._check()
        buff = []
        for line in self.lines:
            buff.append(int(line[index]) if line[index].isdigit else len(line[index]))
        if len(buff) > 0:
            return [[str(self.ACTION_ROUTER.get(target)(buff))]], [target]
        return [], [target]