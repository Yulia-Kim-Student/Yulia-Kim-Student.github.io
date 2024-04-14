from collections.abc import Generator, Iterable
from typing import Optional

def take(iterable: Iterable, *, skip: int = 0, step: int = 1, count: Optional[int] = None) -> Generator:
    if not isinstance(skip, int) or not isinstance(step, int) or (count is not None and not isinstance(count, int)):
        raise TypeError()
    if skip < 0 or (count is not None and count < 0) or step < 1:
        raise ValueError()
    iterator = iter(iterable)
    yielded = 0

    for _ in range(skip):
        next(iterator, None)

    for i in iterator:
        if count is not None and yielded >= count:
            break
        yield i
        for j in range(step - 1):
            next(iterator, None)
        yielded += 1
print(*take(range(100), skip=5, step=5, count=5))
