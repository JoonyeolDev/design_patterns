from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters



class Originator:
    """
    Originator는 시간이 지남에 따라 변경될 수 있는 중요한 상태를 저장합니다.
    또한 상태를 메멘토에 저장하는 메서드와 메멘토로부터 상태를 복원하는 메서드를 정의합니다.
    """

    _state = None
    """
    간단함을 위해, Originator의 상태는 단일 변수에 저장됩니다.
    """

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: 내 초기 상태는 {self._state}입니다.")
    
    def do_something(self) -> None:
        """
        Originator의 비즈니스 로직은 내부 상태에 영향을 줄 수 있습니다.
        따라서 클라이언트는 비즈니스 로직의 메서드를 실행하기 전에 save() 메서드를 통해 상태를 백업해야 합니다.
        """

        print("Originator: 중요한 작업을 하고 있습니다.")
        self._state = self._generate_random_string(30)
        print(f"Originator: 내 상태가 다음으로 변경되었습니다: {self._state}")
    
    @staticmethod
    def _generate_random_string(length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))
    
    def save(self) -> Memento:
        """
        현재 상태를 메멘토에 저장합니다.
        """

        return ConcreteMemento(self._state)
    
    def restore(self, memento: Memento) -> None:
        """
        Originator의 상태를 메멘토 객체에서 복원합니다.
        """

        self._state = memento.get_state()
        print(f"Originator: 내 상태가 다음으로 변경되었습니다: {self._state}")



class Memento(ABC):
    """
    Memento 인터페이스는 메멘토의 메타데이터(생성 날짜 또는 이름 등)를 검색할 수 있는 방법을 제공합니다.
    그러나 Originator의 상태는 노출되지 않습니다.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass



class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]
    
    def get_state(self) -> str:
        """
        Originator가 상태를 복원할 때 이 메서드를 사용합니다.
        """
        return self._state
    
    def get_name(self) -> str:
        """
        나머지 메서드는 Carekater가 메타데이터를 표시하는 데 사용됩니다.
        """
        return f"{self._date} / ({self._state[:9]}...)"

    def get_date(self) -> str:
        return self._date



class Caretaker:
    """
    Caretaker는 Concrete Memento 클래스에 의존하지 않습니다.
    따라서 메멘도에 저장된 Originator의 상태에 접근할 수 없습니다.
    Coretaker는 기본 Memento 인터페이스를 통해 모든 메멘토와 작업합니다.
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator
    
    def backup(self) -> None:
        print("\nCaretaker: Originator의 상태를 저장 중...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return
        
        memento = self._mementos.pop()
        print(f"Caretaker: 상태를 복원 중: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()
    
    def show_history(self) -> None:
        print("Caretaker: 메멘토 목록입니다:")
        for memento in self._mementos:
            print(memento.get_name())



if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\n클라이언트: 이제 롤백하겠습니다.\n")
    caretaker.undo()

    print("\n클라이언트: 한 번 더 롤백합니다.\n")
    caretaker.undo()

# python behavioral_pattern/memento.py