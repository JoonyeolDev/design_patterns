from __future__ import annotations
from abc import ABC, abstractmethod



class Context:
    """
    Context는 클라이언트가 관심을 가질만한 인터페이스를 정의합니다.
    또한 현재 상태를 나타내는 State 하위 클래스의 인스턴스를 참조합니다.
    """

    _state = None
    """
    Context의 현재 상태를 나타내는 참조입니다.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)
    
    def transition_to(self, state: State):
        """
        Context는 실행 중에 State 객체를 변경할 수 있게 해줍니다.
        """

        print(f"Context: {type(state).__name__}로 상태 전환 중.")
        self._state = state
        self._state.context = self
    
    """
    Context는 일부 동작을 현재의 State 객체에 위임합니다.
    """

    def request1(self):
        self._state.handle1()
    
    def request2(self):
        self._state.handle2()



class State(ABC):
    """
    기본 State 클래스는 모든 구체적인 State가 구현해야 하는 메서드를 선언하며,
    State와 연결된 Context 객체에 대한 참조를 제공합니다.
    이 참조는 States가 Context를 다른 상태로 전황하는 데 사용할 수 있습니다.
    """

    @property
    def context(self) -> Context:
        return self._context
    
    @context.setter
    def context(self, context: Context) -> None:
        self._context = context
    
    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass



"""
구체적인 State Context의 상태와 관련된 다양한 동작을 구현합니다.
"""



class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA가 request1을 처리합니다.")
        print("ConcreteStateA는 Context의 상태를 변경하고자 합니다.")
        self.context.transition_to(ConcreteStateB())
    
    def handle2(self) -> None:
        print("ConcreteStateA가 request2를 처리합니다.")



class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB가 request1을 처리합니다.")
    
    def handle2(self) -> None:
        print("ConcreteStateB가 request2를 처리합니다.")
        print("ConcreteStateB는 Context의 상태를 변경하고자 합니다.")
        self.context.transition_to(ConcreteStateA())



if __name__ == "__main__":
    # 클라이언트 코드

    context = Context(ConcreteStateA())
    context.request1()
    context.request2()

# python behavioral_pattern/state.py
