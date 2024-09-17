from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List



class Component(ABC):
    """
    Component 인터페이스는 `accept` 메서드를 선언하며, 이 메서드는 기본 방문자 인터페이스를
    인자로 받아야 합니다.
    """

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass



class ConcreteComponentA(Component):
    """
    각 구체적위 Component `accept` 메서드를 구현해야 하며, 이 메서드는 컴포넌트 클래스에 해당하는
    방문자의 메서드를 호출해야 합니다.
    """

    def accept(self, visitor: Visitor) -> None:
        """
        구체적인 컴포넌트는 기본 클래스나 인터페이스에 존재하지 않는 특별한 메서드를 가질 수 있습니다.
        방문자는 컴포넌트의 구체적인 클래스를 알고 있기 때문에 이러한 메서드를 사용할 수 있습니다.
        """
        return "A"



class ConcreteComponentB(Component):
    """
    동일한 방식으로: visitConcreteComponentB => ConcreteComponentB
    """

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_b(self)
    
    def special_method_of_concrete_component_b(self) -> str:
        return "B"



class Visitor(ABC):
    """
    Visitor 인터페이스는 컴포넌트 클래스에 해당하는일련의 방문 메서드를 선언합니다.
    방문 메서드의 시그니처는 방문자가 현재 처리 중인 컴포넌트의 정확한 클래스를 식별할 수 있게 해줍니다.
    """

    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass



"""
Concrete Visitor들은 같은 알고리즘의 여러 버전을 구현하며, 이는 모든 구체적인 컴포넌트 클래스와
작동할 수 있습니다.

Visitor 패턴의 가장 큰 장점은 복잡한 객체 구조(예: Composite 트리)를 사용할 때 경험할 수 있습니다.
이 경우, 구조의 다양한 객체들에서 방문자의 메서드를 실행하는 동안 알고리즘의 중간 상태를 저장하는 것이
유용할 수 있습니다.
"""



class ConcretreVisitor1(Visitor):
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")
    
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")



class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")



def client_code(components: List[Component], visitor: Visitor) -> None:
    """
    클라이언트 코드는 구체적인 클래스들을 알아내지 않고도 임의의 요소 집합에서 방문자 작업을 실행할 수 있습니다.
    `accept` 메서드는 방문자 객체의 적절한 작업을 호출하도록 지시합니다
    """

    # ...
    for component in components:
        component.accept(visitor)
    # ...



if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("클라이언트 코드는 기본 Visitor 인터페이스를 통해 모든 방문자와 함께 작동합니다:")
    visitor1 = ConcretreVisitor1()
    client_code(components, visitor1)

    print("클라이언트 코드는 다른 유형의 방문자와도 동일하게 작동할 수 있습니다:")
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)

# python behavioral_pattern/visitor.py
