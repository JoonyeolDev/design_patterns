from __future__ import annotations
from abc import ABC



class Mediator(ABC):
    """
    Mediator 인터페이스는 컴포넌트들이 다양한 이벤트에 대해 중재자에게 알릴 때 사용되는 메서드를 선언합니다.
    중재자는 이러한 이벤트에 반응하고, 다른 컴포넌트로 작업을 전달할 수 있습니다.
    """

    def notify(self, sender: object, event: str) -> None:
        pass



class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("중재자가 A에 반응하고 다음 작업을 실행합니다:")
            self._component2.do_c()
        elif event == "D":
            print("중재자가 D에 반응하고 다음 작업을 시작합니다:")
            self._component1.do_b()
            self._component2.do_c()



class BaseComponent:
    """
    Base Component는 컴포넌트 객체 내부에 중재자의 인스턴스를 저장하는 기본 기능을 제공합니다.
    """

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator
    
    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator



"""
구체적인 컴포넌트들은 다양한 기능을 구현합니다. 이들은 다른 컴포넌트에 의존하지 않으며,
구체적인 중재자 클래스에도 의존하지 않습니다.
"""



class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1이 A를 실행합니다.")
        self.mediator.notify(self, "A")
    
    def do_b(self) -> None:
        print("Component 1이 B를 실행합니다.")
        self.mediator.notify(self, "B")



class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2가 c를 실행합니다.")
        self.mediator.notify(self, "C")
    
    def do_d(self) -> None:
        print("Component 2가 D를 실행합니다.")
        self.mediator.notify(self, "D")



if __name__ == "__main__":
    # 클라이언트 코드
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("클라이언트가 A 작업을 트리거합니다.")
    c1.do_a()

    print("\n", end="")

    print("클라이언트가 D 작업을 트리거합니다.")
    c2.do_d()

# python behavioral_pattern/mediator.py
