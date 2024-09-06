from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any



class Builder(ABC):
    """
    Builder 인터페이스는 Product 객체의 다양한 부분을 새엇앟는 메서드를 지정합니다.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass



class ConcreteBuilder1(Builder):
    """
    구체적인 Builder 클래스는 Builder 인터페이스를 따르며, 빌드 단계에 대한 구체적인 구현을 제공합니다.
    프로그램은 여러 변형의 Builder를 가질 수 있으며, 각각 다르게 구현될 수 있습니다.
    """

    def __init__(self) -> None:
        """
        새로운 빌더 인스턴스는 이후 조립에 사용될 빈 제품 객체를 포함해야 합니다.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        구체적인 Builder는 결과를 가져오기 위한 고유한 메서드를 제공해야 합니다.
        이는 다양한 유형의 Builder가 동일한 인터페이스를 따르지 않는 완전히 다른 제품을 만들 수 있기 때문입니다.
        따라서 이러한 메서드는 기본 Builder 인터페이스에 선언될 수 없습니다.

        보통 최종 결과를 클라이언트에 반환한 후, 빌더 인스턴스는 또 다른 제품을 생산할 준비가 되어야 합니다.
        그래스 `getProduct` 메서드는 본문 끝에서 reset 메서드를 호출하는 것이 일반적입니다.
        하지만 이 동작은 필수가 아니며, 빌더가 이전 결과를 처리하기 전에 클라이언트 코드로부터
        명시적인 reset 호출을 기다리도록 만들 수도 있습니다.
        """
        product = self._product
        self.reset()
        return product
    
    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")



class Product1():
    """
    Builder 패턴을 사용하는 것은 제품이 매우 복잡하고 광범위한 구성이 필요한 경우에만 의미가 있습니다.

    다른 생성 패턴과 달리, 다양한 구체적인 Builder는 관련이 없는 제품을 생성할 수 있습니다.
    다시 말해, 다양한 Builder의 결과가 항상 동일한 인터페이스를 따르지 않을 수 있습니다.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"제품의 부분들: {', '.join(self.parts)}", end="")



class Director:
    """
    Director는 특정 순서로 빌딩 단계를 실행하는 것만 책임집니다.
    특정 주문이나 구성에 따라 제품을 생산할 때 유용합니다. 엄밀히 말하면, Director 클래스는 필수가 아니며,
    클라이언트가 Builder를 직접 제어할 수도 있습니다.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder
    

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        Director는 클라이언트 코드가 전달하는 모든 Builder 인스턴스와 함께 작동합니다.
        이를 통해 클라이언트 코드는 새로 조립된 제품의 최종 유형을 변경할 수 있습니다.
        """

        self._builder = builder

    """
    Director는 동일한 빌딩 단계를 사용하여 여러 제품 변형을 생성할 수 있습니다.
    """

    def builder_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def builder_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    클라이언트 코드는 Builder 객체를 생성하고, 이를 Director에 전달한 후
    생성 과정을 시작합니다. 최종 결과는 Builder 객체에서 가져옵니다.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("표준 기본 제품: ")
    director.builder_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("표준 전체 기능 제품: ")
    director.builder_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Builder 패턴은 Director 클래스 없이도 사용할 수 있습니다.
    print("사용자 정의 제품: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()

# python creational_pattern/builder.py
