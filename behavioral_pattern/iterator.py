from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any



"""
파이썬에서 이터레이터를 만들기 위해서는 `collections` 모듈의 두 개의 추상 클래스
Iterable, Iterator를 사용할 수 있습니다. 우리는 반복될 객체(컬렉션)에 `__iter__()` 메서드를 구현하고,
이터레이터에는 `__next__()` 메서드를 구현해야 합니다.
"""



class AlphabeticalOrderIterator(Iterator):
    """
    구체적인 이터레이터는 다양한 순회 알고리즘을 구현합니다. 이러한 클래스들은 항상
    현재 순회 위치를 저장합니다
    """

    """
    `_position` 속성은 현재 순회 위치를 저장합니다. 이터레이터는 많은 다른 필드를 가질 수 있으며,
    특히 특정 종류의 컬렉션과 함께 작동할 때는 더욱 그렇습니다.
    """
    _position: int = None

    """
    이 속성은 순회 방향을 나타냅니다.
    """
    _reverse: bool = False
    
    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0
    
    def __next__(self) -> Any:
        """
        __next__() 메서드는 시퀀스에서 다음 항목을 반환해야 합니다. 끝에 도달했을 때,
        그리고 이후 호출에서는 StopIteration 예외를 발생시켜야 합니다.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        
        return value



class WordsCollection(Iterable):
    """
    구체적인 컬렉션은 컬렉션 클래스와 호환되는 새로운 이터레이터 인스턴스를 가져오는
    하나 이상의 메서드를 제공합니다.
    """

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]
    
    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        __iter__() 메서드는 이터레이터 객체 자체를 반환합니다. 기본적으로
        오름차순으로 이터레이터를 반환합니다.
        """
        return AlphabeticalOrderIterator(self)
    
    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, True)
    
    def add_item(self, item: Any) -> None:
        self._collection.append(item)



if __name__ == "__main__":
    # 클라이언트 코드는 프로그램에서 얼마나 간접적으로 구현할지를 결정하는 것에 따라,
    # 구체적인 이터레이터 또는 컬렉션 클래스에 대해 알 수도 있고, 모를 수도 있습니다.
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("직렬 순회:")
    print("\n".join(collection))
    print("")

    print("역순 순회:")
    print("\n".join(collection.get_reverse_iterator()), end="")

# python behavioral_pattern/iterator.py
