from typing import Iterator, List
from csv import reader


class Parser:
    def __call__(self, filename) -> Iterator[List[str]]:
        with open(filename, 'r') as f:
            data = reader(f)
        return data