from itertools import tee
from typing import Iterator, Tuple, TypeVar

T = TypeVar('T')


def iterate_pairwise(thing: [T]) -> Iterator[Tuple[T, T]]:
    a, b = tee(thing)
    next(b, None)
    return zip(a, b)
