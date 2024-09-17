from abc import ABC, abstractmethod



class AbstractClass(ABC):
    """
    추상 클래스는 템플릿 메서드를 정의하며, 이 메서드는 보통 추상적인 기본 연산에 대한 호출로 구성된
    알고리즘의 골격을 포함합니다.
    구체적인 서브클래스는 이 연산들을 구현해야 하지만, 템플릿 메서드 자체는 그대로 유지됩니다.
    """

    def template_method(self) -> None:
        """
        템플릿 메서드는 알고리즘의 골격을 정의합니다.
        """

        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()
    
    # 이러한 연산들은 이미 구현되어 있습니다.

    def base_operation1(self) -> None:
        print("AbstractClass: 주요 작업을 수행하고 있습니다.")
    
    def base_operation2(self) -> None:
        print("AbstractClass: 하지만 몇 가지 연산은 서브클래스가 재정의할 수 있습니다.")
    
    def base_operation3(self) -> None:
        print("AbstractClass: 하지만 주요 작업은 제가 하고 있습니다.")

    # 이러한 연산들은 서브클래스에서 구현해야 합니다.

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    # 이러한 것은 "훅"입니다. 서브클래스에서 재정의할 수 있지만, 필수는 아닙니다.
    # 훅은 이미 기본 (비어 있는) 구현을 가지고 있습니다. 혹은 알고리즘의 중요한
    # 위치에서 추가적인 확장 지점을 제공합니다.

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass



class ConcreteClass1(AbstractClass):
    """
    구체적인 클래스는 기본 클래스의 모든 추상 연산을 구현해야 합니다.
    또한 기본 구현이 있는 일부 연산을 재정의할 수 있습니다.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass1: Operation1을 구현했습니다.")
    
    def required_operations2(self) -> None:
        print("ConcreteClass1: Operation2를 구현했습니다.")



class ConcreteClass2(AbstractClass):
    """
    일반적으로 구체적인 클래스는 기본 클래스의 일부 연산만 재정의합니다.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass2: Operation1을 구현했습니다.")
    
    def required_operations2(self) -> None:
        print("ConcreteClass2: Operation2를 구현했습니다.")
    
    def hook1(self) -> None:
        print("ConcreteClass2: Hook1을 재정의했습니다.")



def client_code(abstract_class: AbstractClass) -> None:
    """
    클라이언트 코드는 템플릿 메서드를 호출하여 알고리즘을 실행합니다.
    클라이언트 코드는 객체의 구체적인 클래스를 알 필요가 없으며,
    기본 클래스의 인터페이스를 통해서만 작업합니다.
    """

    # ...
    abstract_class.template_method()
    # ...



if __name__ == "__main__":
    print("클라이언트 코드는 동일한 서브클래스와 함께 작동할 수 있습니다:")
    client_code(ConcreteClass1())

    print("\n클라이언트 코드는 다른 서브클래스와 함께 작동할 수 있습니다:")
    client_code(ConcreteClass2())

# python behavioral_pattern/template_method.py
