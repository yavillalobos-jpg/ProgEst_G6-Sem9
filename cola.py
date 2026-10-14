"""Implementación de una cola (queue) con capacidad limitada.

Cada elemento es un diccionario con el formato:
    {"type": "text" | "photo", "value": <texto o imagen en base64>}
"""

from collections import deque


class QueueFullError(Exception):
    """Se intentó encolar en una cola llena."""


class QueueEmptyError(Exception):
    """Se intentó leer o desencolar en una cola vacía."""


class Queue:
    """Cola FIFO (primero en entrar, primero en salir) con capacidad máxima."""

    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("La capacidad debe ser mayor a 0.")
        self.capacity = capacity
        self._items: deque[dict] = deque()

    def __len__(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return not self._items

    def is_full(self) -> bool:
        return len(self._items) == self.capacity

    def enqueue(self, item: dict) -> None:
        """Agrega un elemento al final de la cola."""
        if self.is_full():
            raise QueueFullError("La cola está llena.")
        self._items.append(item)

    def dequeue(self) -> dict:
        """Quita y devuelve el elemento del frente de la cola."""
        if self.is_empty():
            raise QueueEmptyError("La cola está vacía.")
        return self._items.popleft()

    def peek(self) -> dict:
        """Devuelve el elemento del frente sin quitarlo."""
        if self.is_empty():
            raise QueueEmptyError("La cola está vacía.")
        return self._items[0]

    def to_list(self) -> list[dict]:
        """Elementos del frente hacia el final (para mostrarlos en pantalla)."""
        return list(self._items)