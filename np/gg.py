from __future__ import annotations
from collections.abc import Callable
from typing import Any, Generic, TypeVar

C = TypeVar('C')

class Property(Generic[C]):
    def __init__(self, getter: Callable[[C], Any] | None = None,
                       setter: Callable[[C, Any], None] | None = None,
                       deleter: Callable[[C], None] | None = None,
                       doc: str | None = None,
                       default_value: Any | None = None):
        self._name = None  # Placeholder for the property value
        self._getter = getter
        self._setter = setter
        self._deleter = deleter
        self._doc = doc
        self._default_value = default_value

        if setter is not None and default_value is not None:
            self._setter(default_value)

    def getter(self, getter: Callable[[C], Any]) -> Property[C]:
        self._getter = getter
        return self

    def setter(self, setter: Callable[[C, Any], None] | None = None, default_value: Any | None = None) -> Property[C] | Callable[[Callable[[C, Any], None]], Property[C]]:
        if setter is None:
            return lambda func: self.setter(func, default_value)
        self._setter = setter
        if default_value is not None:
            self._setter(default_value)
        return self

    def deleter(self, deleter: Callable[[C], None]) -> Property:
        self._deleter = deleter
        return self

    def __get__(self, instance: C, owner: Any) -> Any:
        if self._getter is None:
            raise AttributeError(f"Cannot read {owner.__name__}.{self._name}")
        return self._getter(instance)

    def __set__(self, instance: C, value: Any) -> None:
        if self._setter is None:
            raise AttributeError(f"Cannot set {instance.__class__.__name__}.{self._name}")
        self._setter(instance, value)

    def __delete__(self, instance: C) -> None:
        if self._deleter is None:
            raise AttributeError(f"Cannot delete {instance.__class__.__name__}.{self._name}")
        self._deleter(instance)

    def __set_name__(self, owner: Any, name: str) -> None:
        self._name = name

    def __doc__(self) -> str:
        doc_parts = [
            f"Property '{self._name}' on class {self.__class__.__name__}",
            self._doc,
            f"Getter:\n\n{self._getter.__doc__}" if self._getter else "",
            f"Setter:\n\n{self._setter.__doc__}" if self._setter else "",
            f"Deleter:\n\n{self._deleter.__doc__}" if self._deleter else "",
        ]
        return '\n\n'.join(filter(None, doc_parts))

class Person:
    def __init__(self):
        self._name = None

    @Property()
    def name(self) -> str:
        '''Name of a person, str'''
        return self._name

    @name.setter()
    def name(self, value: str):
        '''Sets the name, must be of type str'''
        self._name = value

    @name.deleter()
    def name(self):
        '''Sets the name to None'''
        self._name = None

p = Person()
print(Person.name.__doc__)

print(p.name)
p.name = 'Petya'
print(p.name)
del p.name
print(p.name)
