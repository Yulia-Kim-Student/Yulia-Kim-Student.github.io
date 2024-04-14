from __future__ import annotations
from typing import Union, Iterable, List
import random


class CardStack:
    values: List[int]

    def __init__(self, val: Union[int, Iterable[int], None] = None):
        """If val is None values is an empty list
         If val is int fills values with val random integers between -100 and 100
         If val is Iterable[int] fills values from val
      """

        self.values = []
        if val is not None:
            if type(val) == eval('int'):
                self.values = [random.randint(-100, 100) for i in range(val)]
            else:
                self.values = list(val)

    def shuffled(self) -> CardStack:
        """Returns a new CardStack instance with shuffled values"""
        new_values = self.values.copy()
        random.shuffle(new_values)
        return CardStack(new_values)

    def combine(self, other: CardStack) -> CardStack:
        """Returns a new CardStack instance with self and other values combined one after another
         [1, 2, 3], [4, 5, 6, 7] -> [1, 4, 2, 5, 3, 6, 7]
      """
        new_values = []
        if len(self.values) <= len(other.values):
            start = len(self.values)
            end = other.values[start:]
        else:
            start = len(other.values)
            end = self.values[start:]
        for i in range(start):
            new_values.append(self.values[i])
            new_values.append(other.values[i])
        new_values += end

        return CardStack(new_values)

    def add(self, value: int) -> None:
        """Adds a new value on top of the stack"""
        self.values.append(value)

    def __len__(self) -> int:
        """Returns the size of the stack"""
        return len(self.values)


# Описание интерфейса использует аннотации типов, в частности, Union, List и Iterable.

stack = CardStack([1, 2, 3, 4, 5])
stack_2 = stack.combine(CardStack([6, 7, 8]))

print(stack_2.values)
