class Component:
    """
    기본 Component 인터페이스는 데코레이터에 의해 변경될 수 있는 작업을 정의하빈다.
    """

    def operation(self) -> str:
        pass



class ConcreteComponent(Component):
    """
    ConcreteComponent는 작업의 기본 구현을 제공합니다.
    이러한 클래스의 여러 변형이 있을 수 있습니다.
    """

    def operation(self) -> str:
        return "ConcreteCompnent"



class Decorator(Component):
    """
    기본 데코레이터 클래스는 다른 컴포넌트들과 동일한 인터페이스를 따릅니다.
    이 클래스의 주요 목적은 모든 구체적인 데코레이터에 대한 래핑 인터페이스를 정의하는 것입니다.
    래핑 코드의 기본 구현에는 래핑된 컴포넌트를 저장하기 위한 필드와 이를 초기화하는 방법이 포함될 수 있습니다.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
        데코레이터는 모든 작업을 래핑된 컴포넌트에 위임합니다.
        """
        return self._component
    
    def operation(self) -> str:
        return self._component.operation()



class ConcreteDecoratorA(Decorator):
    """
    구체적인 데코레이터는 래핑된 객체를 호출하고 그 결과를 수정합니다.
    """

    def operation(self) -> str:
        """
        데코레이터는 래핑된 객체를 직접 호출하는 대신 부모의 구현을 호출할 수 있습니다.
        이 접근 방식은 데코레이터 클래스의 확장을 단순하게 만듭니다.
        """
        return f"ConcreteDecoratorA({self.component.operation()})"



class ConcreteDecoratorB(Decorator):
    """
    데코레이터는 래핑된 객체를 호출하기 전이나 후에 그들의 동작을 실행할 수 있습니다.
    """

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"



def client_code(component: Component) -> None:
    """
    클라이언트 코드는 Component 인터페이스를 사용하여 모든 객체와 작업을 수행합니다.
    이를 통해 구체적인 컴포넌트 클래스에 의존하지 않게 됩니다.
    """

    print(f"결과: {component.operation()}", end="")



if __name__ == "__main__":
    # 이렇게 하면 클라이언트 코드는 단순한 컴포넌트도 지원할 수 있습니다.
    simple = ConcreteComponent()
    print("클라이언트: 단순한 컴포넌트를 가지고 있습니다.")
    client_code(simple)
    print("\n")

    # ...그리고 데코레이터된 컴포넌트도 지원할 수 있습니다.
    # 데코레이터가 단순한 컴포넌트뿐만 아니라 다른 데코레이터도 래핑할 수 있다는 점에 주목하세요.
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("클라이언트: 이제 데코레이터된 컴포넌트를 가지고 있습니다:")
    client_code(decorator2)

# python structural_pattern/decorator.py
