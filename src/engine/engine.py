from typing import Union, Dict, List

from funcs import *
from errors import FilterError
from parser import Parser

from prettytable import PrettyTable
from csv import reader


parser = Parser()

class Engine:

    ACTION_ROUTER = {
        "aggregate": AggregateFilter,
        "order_by": OrderByFilter
    }

    def __init__(self, **kwargs: Dict[str, Union[str, None]]):
        self.filename = kwargs.pop("file")
        self.kwargs = kwargs
        self.lines = []
        self.header_line = []
        self.parse()

    def start(self) -> None:
        if any(value is not None for value in self.kwargs.values()):
            if self.kwargs.get('aggregate') and self.kwargs.get('order_by'):
                raise FilterError("Эти операторы нельзя использовавть вместе",
                            "--aggregate и --order-by нельзя использовать вместе")
            where_target = self.kwargs.pop('where')
            if where_target:
                filter = WhereFilter(self.lines, self.header_line, where_target)
                self.lines = filter.get()
            for key in self.kwargs.keys():
                if not self.kwargs.get(key) is None:
                    filter = self.ACTION_ROUTER[key](
                        self.lines,
                        self.header_line,
                        self.kwargs.get(key)
                    )
                    data = filter.get()
                    if isinstance(data, tuple):
                        self.lines, self.header_line = data
                    else:
                        self.lines = data
        table = self.pretty_print(self.header_line, self.lines)
        print(table)

    @staticmethod
    def pretty_print(header: List[str], lines: List[List[str]]) -> str:
        table = PrettyTable()
        table.field_names = header
        for line in lines:
            table.add_row(line)
        return table

    def parse(self) -> None:
        with open(self.filename, 'r') as f:
            lines = list(reader(f))
        self.header_line = lines[0]
        self.lines = lines[1:]