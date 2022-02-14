from random import randint
from typing import List, NamedTuple


Car = NamedTuple('Car', [('id', int), ('name', str), ('price', int), ('speed', int)])

cars: List[Car] = [
    Car(1, 'Audi', randint(1, 100) * 100000, 300),
    Car(2, 'BWM', randint(1, 100) * 100000, 320),
    Car(3, 'Mercedes', randint(1, 100) * 100000, 340),
    Car(4, 'Lada', randint(1, 100), 30),
]