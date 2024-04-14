from __future__ import annotations
from collections.abc import Iterable, Iterator

class stack_chain:
    def __init__(self, *iterables: Iterable):
        self.iterables = list(iterables)

    def __iter__(self) -> Iterator:
        return self.StackChainIterator(self)

    def __iadd__(self, iterable: Iterable) -> stack_chain:
        self.iterables.insert(0, iterable)
        return self

    class StackChainIterator:
        def __init__(self, stack_chain_obj: stack_chain):
            self.stack_chain_obj = stack_chain_obj
            self.current_iterable = None
            self.iterable_index = 0

        def __iter__(self):
            return self

        def __next__(self):
            # Переходим к следующему итерируемому объекту, если текущий исчерпан или изменился список
            while self.current_iterable is None or self.iterable_index < len(self.stack_chain_obj.iterables):
                if self.iterable_index >= len(self.stack_chain_obj.iterables):
                    raise StopIteration
                self.current_iterable = iter(self.stack_chain_obj.iterables[self.iterable_index])
                self.iterable_index += 1

                try:
                    return next(self.current_iterable)
                except StopIteration:
                    self.current_iterable = None

            raise StopIteration
a = stack_chain(range(3))
for i in a:
    a += [i - 1] * i
    print(i, end=' ')