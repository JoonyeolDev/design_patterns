from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    추상 팩토리 인터페이스는 서로 다른 추상 제품을 반환하는 일련의 메서드를 선언합니다.
    이 제품들은 하나의 높은 수준의 주제나 개념에 의해 연관된 제품군으로 불립니다.
    하나의 제품군에 속하는 제품들은 보통 서로 협력할 수 있습니다.
    제품군은 여러 가지 변형을 가질 수 있지만, 한 변형의 제품은 다른 변형의 제품과 호환되지 않습니다.
    """

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def craete_product_b(self) -> AbstractProductB:
        pass



class ConcreteFactory1(AbstractFactory):
    """
    구체적인 팩토리는 단일 변형에 속하는 제품군을 생성합니다.
    팩토리는 생성된 제품이 서로 호환된다는 것을 보장합니다.
    구체적인 팩토리 메서드의 서명은 추상 제품을 반환하지만, 
    메서드 내부에서는 구체적인 제품이 인스턴스화됩니다.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def craete_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()



class ConcreteFactory2(AbstractFactory):
    """
    각 구체적인 팩토리는 해당하는 제품 변형을 가지고 있습니다.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()
    
    def craete_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()



class AbstractProductA(ABC):
    """
    제품군의 각 고유한 제품은 기본 인터페이스를 가져야 합니다.
    제품의 모든 변형은 이 인터페이를 구현해야 합니다.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass



"""
구체적인 제품은 해당하는 구체적인 팩토리에 의해 생성됩니다.
"""


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "제품 A1의 결과입니다."



class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "제품 A2의 결과입니다."



class AbstractProductB(ABC):
    """
    여기 또 다른 제품의 기본 인터페이스가 있습니다.
    모든 제품은 서로 상호작용할 수 있지만, 
    동일한 구체적인 변형의 제품끼리만 올바르게 상호작용할 수 있습니다.
    """

    @abstractmethod
    def useful_function_b(self) -> str:
        """
        제품 B는 자체적으로 작업을 수행할 수 있습니다...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        """
        ...하지만 ProductA와도 협력할 수 있습니다.
        추상 팩토리는 생성된 모든 제품이 동일한 변형에 속하고, 따라서 호환 가능하도록 합니다.
        """
        pass


"""
구체적인 제품은 해당하는 구체적인 팩토리에 의해 생성됩니다.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "제품 B1의 결과입니다."
    
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        """
        변형 B1 제품은 변형 A1 제품하고만 올바르게 작동할 수 있습니다.
        그럼에도 불구하고 AbstractProductA의 인스턴스는 어떤 것이든 인수로 받아들일 수 있습니다.
        """
        result = collaborator.useful_function_a()
        return f"B1이 ({result})와 협력한 결과입니다."



class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "제품 B2의 결과입니다."
    
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        """
        변형 B2 제품은 변형 A2 제품하고만 올바르게 작동할 수 있습니다.
        그럼에도 불구하고 AbstractProductA의 인스턴스는 어떤 것이든 인수로 받아들일 수 있습니다.
        """
        result = collaborator.useful_function_a()
        return f"B2 ({result})와 협력한 결과입니다."



def client_code(factory: AbstractFactory) -> None:
    """
    클라이언트 코드는 팩토리 및 제품을 추상 타입인 AbstractFactory와 AbstractProduct를 통해서만 작업합니다.
    이를 통해 클라이언트 코드에 어떤 팩토리나 제품 서브클래스도 전달할 수 있으며, 코드가 깨지지 않습니다.
    """
    product_a = factory.create_product_a()
    product_b = factory.craete_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    클라이언트 코드는 어떤 구체적인 팩토리 클래스와도 작업할 수 있습니다
    """
    print("클라이언트: 첫 번째 팩토리 유형으로 클라이언트 코드를 테스트 중:")
    client_code(ConcreteFactory1())

    print("\n")

    print("클라이언트: 동일한 클라이언트 코드를 두 번째 팩토리 유형으로 테스트 중:")
    client_code(ConcreteFactory2())

# python creational_pattern/abstract_factory.py
