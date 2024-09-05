from __future__ import annotations
from abc import ABC, abstractmethod



class Abstraction:
    """
    Abstraction은 두 개의 클래스 계증 구조 중 "제어" 부분의 인터페이스를 정의합니다.
    이 클래스는 Implementation 계층의 객체에 대한 참조를 유지하며,
    실제 작업은 이 객체에 위임합니다.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: 기본 동작과 함께:\n"
                f"{self.implementation.operation_implementation()}")



class ExtendedAbstraction(Abstraction):
    """
    Implementation 클래스들을 변경하지 않고도 Abstraction을 확장할 수 있습니다.
    """

    def operation(self) -> str:
        return (f"ExtendedAbstraction: 확장된 동작과 함께:\n"
                f"{self.implementation.operation_implementation()}")



class Implementation(ABC):
    """
    Implementation은 모든 구현 클래스들을 위한 인터페이스를 정의합니다.
    이 인터페이스는 Abstraction의 인터페이스와 일치할 필요가 없습니다.
    사실, 두 인터페이스는 완전히 다를 수 있습니다.
    일반적으로 Implementation 인터페이스는 기본적인 작업만 제공하며,
    Abstraction은 이러한 기본 작업을 기반으로 고수준의 작업을 정의합니다.
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass



"""
각 Concrete Implementation은 특정 플랫폼에 해당하며,
그 플랫폼의 API를 사용하여 Implementation 인터페이스를 구현합니다.
"""



class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: 여기 플랫폼 A의 결과입니다."



class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: 여기 플랫폼 B의 결과입니다."



def client_code(abstraction: Abstraction) -> None:
    """
    Abstraction 객체가 특정 Implementation 객체와 연결되는 초기화 단계 외에는,
    클라이언트 코드는 오직 Abstraction 클래스에만 의존해야 합니다.
    이렇게 하면 클라이언트 코드는 모든 추상화-구현 조합을 지원할 수 있습니다.
    """

    # ...

    print(abstraction.operation(), end="")

    # ...



if __name__ == "__main__":
    """
    클라이언트 코드는 미리 구성된 추상화-구현 조합과 함께 작동할 수 있어야 합니다.
    """

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)

# python structural_pattern/bridge.py