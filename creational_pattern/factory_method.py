from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    Creator 클래스는 Product 클래스의 객체를 반환하는 팩토리 메서드를 선언합니다.
    Creator의 하위 클래스는 보통 이 메서드의 구현을 제공합니다.
    """

    @abstractmethod
    def factory_method(self):
        """
        Creator는 팩토리 메서드의 기본 구현을 제공할 수도 있습니다.
        """
        pass

    def some_operation(self) -> str:
        """
        Creator의 주된 책임은 제품을 생성하는 것이 아니라는 점을 유의하세요.
        보통은 팩토리 메서드가 반환하는 Product 객체에 의존하는 핵심 비즈니스
        로직을 포함하고 있습니다. 하위 클래스는 팩토리 메서드를 재정의하고
        다른 유형의 제품을 반환하여 이 비즈니스 로직을 간접적으로 변경할 수 있습니다.
        """

        # 팩토리 메서드를 호출하여 Product 객체를 생성합니다.
        product = self.factory_method()

        # 이제 product를 사용합니다.
        result = f"Creator: 동일한 Creator의 코드가 {product.operation()}와/과 함께 작동했습니다."

        return result
    


"""
구체적인 Creator 클래스는 팩토리 메서드를 재정의하여 결과로 나오는 제품의 유형을 변경합니다.
"""

class ConcreteCreator1(Creator):
    """
    메서드의 서명이 여전히 추상 제품 유형을 사용하고 있지만,
    실제로는 구체적인 제품이 메서드에서 반환됩니다.
    이렇게 하면 Creator는 구체적인 제품 클래스에 독립적으로 유지될 수 있습니다.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()
    

class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
    

class Product(ABC):
    """
    Product 인터페이스는 모든 구체적인 제품이 구현해야 하는 작업을 선언합니다.
    """

    @abstractmethod
    def operation(self) -> str:
        pass



"""
구체적인 제품 클래스는 Product 인터페이스의 다양한 구현을 제공합니다.
"""

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{ConcreteProduct1의 결과}"
    

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{ConcreteProduct2의 결과}"
    

def client_code(creator: Creator) -> None:
    """
    클라이언트 코드는 구체적인 Creator의 인스턴스와 함께 작동하지만,
    이를 기본 인터페이스를 통해 처리합니다. 클라이언트가 Creator와 기본 인터페이스를 통해
    계속 작동하는 한, 아무 하위 클래스나 전달할 수 있습니다.
    """

    print(f"Client: 나는 Creator의 클래스에 대해 모르지만, 여전히 작동합니다.\n"
          f"{creator.some_operation()}", end="")
    

if __name__=="__main__":
    print("App: ConcreteCreator1로 실행되었습니다.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: ConcreteCreator2로 실행되었습니다.")
    client_code(ConcreteCreator2())

# python creational_pattern/factory_method.py
