from __future__ import annotations
from collections.abc import Iterable, Iterator

class stack_chain:

    def __init__(self, *iterables: Iterable):
        self.iterables = list(iterables)

    def __iter__(self) -> Iterator:
        return self.Iterator(self)

    def __iadd__(self, iterable: Iterable) -> stack_chain:
        self.iterables.insert(0, iterable)
        return self

    class Iterator:
        def __init__(self, object: stack_chain):
            self.object = object
            self.curr_iter = iter(self.object.iterables.pop()) if self.object.iterables else None

        def __iter__(self):
            return self

        def __next__(self):
            if self.curr_iter is None:
                raise StopIteration
            try:
                return next(self.curr_iter)
            except StopIteration:
                if not self.object.iterables:
                    raise
                self.curr_iter = iter(self.object.iterables.pop())
                return self.__next__()


# print(*stack_chain(range(3), range(2, -1, -1), (i * i for i in range(3))))
a = stack_chain(range(3))
for i in a:
    a += [i - 1] * i
    print(i, end=' ')

