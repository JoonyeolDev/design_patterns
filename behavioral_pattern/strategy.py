from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List



class Context():
    """
    Context는 클라이언트가 관심을 가질만한 인터페이스를 정의합니다.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        일반적으로 Context는 생성자를 통해 전량을 받지만,
        실행 중에 전략을 변경할 수 있는 세터도 제공합니다.
        """
        self._strategy = strategy
    
    @property
    def strategy(self) -> Strategy:
        """
        Context는 하나의 Strategy 객체에 대한 참조를 유지합니다.
        Context는 구체적인 전략 클래스에 대해 알지 못합니다.
        Context는 Strategy 인터페이스를 통해 모든 전략을 처리해야 합니다.
        """
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Context는 실행 중에 Strategy 객체를 교체할 수 있도록 허용합니다.
        """
        self._strategy = strategy
    
    def do_some_business_logic(self) -> None:
        """
        Context는 자체적으로 여러 알고리즘 버전을 구현하는 대신
        일부 작업을 Startegy 객체에 위임합니다.
        """

        # ...

        print("Context: 전략을 사용하여 데이터를 정렬 중입니다(어떻게 정렬할지는 모릅니다).")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        # ...



class Strategy(ABC):
    """
    Strategy 인터페이스는 알고리즘의 모든 지원 버전에 공통된 작업을 선언합니다.
    Context는 이 인터페이스를 사용하여 구체적인 전략에 정의된 알고리즘을 호출합니다.
    """
    
    @abstractmethod
    def do_algorithm(self, data: List) -> List:
        pass



"""
구체적인 전략들은 기본 Strategy 인터페이스를 따르며 알고리즘을 구현합니다.
이 인터페이스 덕분에 구체적인 전략들은 Context에서 서로 교체될 수 있습니다.
"""



class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)



class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))



if __name__ == "__main__":
    # 클라이언트 코드는 구체적인 전략을 선택하고 이를 Context에 전달합니다.
    # 클라이언트는 적절한 선택을 하기 위해 전략 간의 차이를 알고 있어야 합니다.

    context = Context(ConcreteStrategyA())
    print("클라이언트: 전략이 일반 정렬로 설정되었습니다.")
    context.do_some_business_logic()
    
    print("\n클라이언트: 전략이 역순 정렬로 설정되었습니다.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()

# python behavioral_pattern/strategy.py