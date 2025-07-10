from typing import List, Tuple, Union

from errors import FilterError
from models import BaseFilter


class WhereFilter(BaseFilter):

    ALLOWED_ACTIONS = ">", "<", "<=", ">=", "="
    
    def __init__(self, lines: List[List[str]], header_line: List[str], target: str):
        self.lines = lines
        self.target = target
        self.header_line = header_line

    def advanced_check_operaionts(self) -> Union[str, bool]:
        counter = 0
        for action in self.ALLOWED_ACTIONS:
            if action in self.target:
                index = self.target.index(action)
                if action in ("<", ">") and not self.target[index + 1] == "=" \
                                                    or action in ("<=", ">="):
                    counter += 1
                    result = action
                if action == "=" and not self.target[index - 1] in ("<", ">"):
                    counter += 1
                    result = action
        if counter == 1:
            return result
        else:
            return False

    def _check(self) -> Tuple[int, str, str]:
        result = self.advanced_check_operaionts()
        if result:
            target_header, target_value = self.target.split(result)
            if target_header in self.header_line:
                return self.header_line.index(target_header), target_value, result
            else:
                raise FilterError(
                    f"Атрибута {target_header} нет среди {self.header_line}"            
            )
        else:
            raise FilterError(
                "Нет действий, или их слишком много для оператора where",
                f"Проверка на действия оператора where вернула {result}"
            )
    
    def get(self) -> List[List[str]]:
        index, target_value, action = self._check()
        buff = []
        for line in self.lines:
            match action:
                case ">":
                    if line[index] > target_value:
                        buff.append(line)
                case "<":
                    if line[index] < target_value:
                        buff.append(line)
                case "<=":
                    if line[index] <= target_value:
                        buff.append(line)
                case ">=":
                    if line[index] >= target_value:
                        buff.append(line)
                case "=":
                    if line[index] == target_value:
                        buff.append(line)
        return buff