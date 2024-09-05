from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List



class Component(ABC):
    """
    기본 Component 클래스는 단순 및 복합 객체의 공통 작업을 선언합니다.
    """

    @property
    def parent(self) -> Component:
        return self._parent
    
    @parent.setter
    def parent(self, parent: Component):
        """
        선택적으로, 기본 Component는 트리 구조에서 부모를 설정하고
        접근하는 인터페이스를 선언할 수 있습니다.
        이 메서드에 대한 기본 구현을 제공할 수도 있습니다.
        """
        self._parent = parent
    
    """
    어떤 경우에는 자식 관리 작업을 기본 Component 클래스에 정의하는 것이 유리할 수 있습니다.
    이렇게 하면 클라이언트 코드가 객체 트리를 조립할 때
    구체적인 컴포넌트 클래스를 노출하지 않아도 됩니다.
    단점은 이러한 메서드가 리프 수준의 컴포넌트에서는 비어 있게 된다는 것입니다.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        클라이언트 코드가 컴포넌트가 자식을 가질 수 있는지 여부를 확인할 수 있도록 하는 메서드를 제공합니다.
        """
        return False
    
    @abstractmethod
    def operation(self) -> str:
        """
        기본 Component는 기본 동작을 구현하거나,
        이 메서드를 추상 메서드로 선언하여 구체적인 클래스에 맡길 수 있습니다.
        """
        pass



class Leaf(Component):
    """
    Leaf 클래스는 구성(composition)의 끝 객체를 나타냅니다. 리프는 자식을 가질 수 없습니다.
    
    일반적으로 Leaf 객체가 실제 작업을 수행하고, Composite 객체는 하위 컴포넌에 작업을 위임합니다.
    """

    def operation(self) -> str:
        return "Leaf"



class Composite(Component):
    """
    Composite 클래스는 자식을 가질 수 있는 복잡한 컴포넌트를 나타냅니다.
    Composite 객체는 일반적으로 실제 작업을 자식들에게 위임하고, 결과를 합산합니다.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    """
    복합 객체는 자식 목록에 다른 컴포넌트(단순 또는 복합)를 추가하거나 제거할 수 있습니다.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self
    
    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True
    
    def operation(self) -> str:
        """
        Composite는 특정 방식으로 주 작업을 수행합니다.
        자식들은 재귀적으로 순회하면서 그들의 결과를 수집하고 합산합니다.
        Composite의 자식들이 이 호출을 그들의 자식들에게 전달하므로,
        결과적으로 전체 객체 트리가 순회됩니다.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"



def client_code(component: Component) -> None:
    """
    클라이언트 코드는 기본 인터페이스를 통해 모든 컴포넌트와 함께 작동합니다.
    """
    print(f"결과: {component.operation()}", end="")



def client_code2(component1: Component, component2: Component) -> None:
    """
    자식 관리 작업이 기본 Component 클래스에 선언되어 있기 때문에,
    클라이언트 코드는 구체적인 클래스에 의존하지 않고, 단순 또는 복합 컴포넌트와 함께 작업할 수 있습니다.
    """

    if component1.is_composite():
        component1.add(component2)
    
    print(f"결과: {component1.operation()}", end="")



if __name__ == "__main__":
    # 이렇게 하면 클라이언트 코드는 단순한 리프 컴포넌트를 지원할 수 있습니다.
    simple = Leaf()
    print("클라이언트: 나는 단순한 컴포넌트를 가지고 있습니다:")
    client_code(simple)
    print("\n")

    # ...그리고 복잡한 Composite도 지원할 수 있습니다.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("클라이언트: 이제 복합 트리를 가지고 있습니다:")
    client_code(tree)
    print("\n")

    print("클라이언트: 트리를 관리할 때 컴포넌트 클래스를 확인할 필요가 없습니다:")
    client_code2(tree, simple)

# python structural_pattern/composite.py
