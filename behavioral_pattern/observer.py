from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List



class Subject(ABC):
    """
    Subject 인터페이스는 구독자를 관리하는 메서드 집합을 선언합니다.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        구독자를 Subject에 연결합니다.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        구독자를 Subject에서 분리합니다.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        이벤트에 대해 모든 구독자에게 알립니다.
        """
        pass



class ConcreteSubject(Subject):
    """
    Subject는 중요한 상태를 가지고 있으며, 그 상태가 변경될 때 구독자에게 알립니다.
    """

    _state: int = None
    """
    간단함을 위해, Subject의 상태는 구독자들에게 중요한 내용으로 이 변수에 저장됩니다.
    """

    _observers: List[Observer] = []
    """
    구독자 목록입니다. 실제 상황에서는 구독자 목록을 더 세분화하여 저장할 수 있습니다 (이벤트 유형별로 분류 등).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: 구독자가 연결되었습니다.")
        self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    """
    구독 관리 메서드입니다.
    """

    def notify(self) -> None:
        """
        각 구독자에게 업데이트를 트리거합니다.
        """

        print("Subject: 구독자에게 알림을 보내는 중...")
        for observer in self._observers:
            observer.update(self)
    
    def some_business_logic(self) -> None:
        """
        일반적으로 구독 로직은 Subject가 할 수 있는 일의 일부분일 뿐입니다.
        Subject는 중요한 비즈니스 로직을 가지고 있으며, 중요한 일이 일어날 때마다 알림 메서드를 호출합니다.
        """

        print("\nSubject: 중요한 작업을 하고 있습니다.")
        self._state = randrange(0, 10)

        print(f"Subject: 내 상태가 {self._state}로 변경되었습니다.")
        self.notify()



class Observer(ABC):
    """
    Observer 인터페이스는 Subject가 사용하는 업데이트 메서드를 선언합니다.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Subject로부터 업데이트를 받습니다.
        """
        pass



"""
Concrete Observers는 연결된 Subject에서 발행된 업데이트에 반응합니다.
"""



class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: 이벤트에 반응했습니다.")



class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: 이벤트에 반응했습니다.")



if __name__ == "__main__":
    # 클라이언트 코드

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()

# python behavioral_pattern/observer.py
