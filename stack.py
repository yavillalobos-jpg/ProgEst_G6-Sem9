"""Implementación de una pila (stack) con capacidad limitada.

Cada elemento es un diccionario con el formato:
    {"type": "text" | "photo", "value": <texto o imagen en base64>}
"""


class StackFullError(Exception):
    """Se intentó apilar en una pila llena."""


class StackEmptyError(Exception):
    """Se intentó leer o desapilar en una pila vacía."""


class Stack:
    """Pila LIFO con capacidad máxima."""

    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("La capacidad debe ser mayor a 0.")
        self.capacity = capacity
        self._items: list[dict] = []

    def __len__(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return not self._items

    def is_full(self) -> bool:
        return len(self._items) == self.capacity

    def push(self, item: dict) -> None:
        if self.is_full():
            raise StackFullError("La pila está llena.")
        self._items.append(item)

    def pop(self) -> dict:
        if self.is_empty():
            raise StackEmptyError("La pila está vacía.")
        return self._items.pop()

    def peek(self) -> dict:
        if self.is_empty():
            raise StackEmptyError("La pila está vacía.")
        return self._items[-1]

    def to_list(self) -> list[dict]:
        """Elementos del tope hacia la base (para mostrarlos en pantalla)."""
        return list(reversed(self._items))