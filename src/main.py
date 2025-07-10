from argparse import ArgumentParser
from engine import Engine


parser = ArgumentParser()

parser.add_argument('--file', required=True, help='Путь к csv файлу')
parser.add_argument('--where', help='where оператор, пример --where Age>=25')
parser.add_argument('--aggregate', help='aggregate оператор, пример --aggregate Age=avg')
parser.add_argument('--order-by', help='order by оператор, пример --order-by Age=asc')


args = vars(parser.parse_args())
engine = Engine(**args)
engine.start()