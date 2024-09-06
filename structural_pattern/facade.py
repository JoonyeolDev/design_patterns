from __future__ import annotations



class Facade:
    """
    Facade 클래스는 하나 이상의 서브시스템의 복잡한 로직에 대한 간단한 인터페이스를 제공합니다.
    Facade는 클라이언트 요청을 적절한 서브시스템 객체에 위임하며,
    이들의 생명 주기를 관리하는 책임도 맡고 있습니다.
    이를 통해 클라이언트는 서브시스템의 복잡성에서 벗어날 수 있습니다.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        애플리케이션의 요구에 따라, Facade는 기존 서브시스템 객체를 받거나
        Facade가 스스로 이를 생성하도록 강제할 수 있습니다.
        """

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()
    
    def operation(self) -> str:
        """
        Facade의 메서드는 서브시스템의 복잡한 기능을 위한 단축 방법을 제공합니다.
        하지만 클라이언트는 서브시스템의 일부 기능만을 사용할 수 있습니다.
        """

        results = []
        results.append("Facade가 서브시스템을 초기화합니다:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade가 서브시스템에 작업을 수행하도록 지시합니다:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)



class Subsystem1:
    """
    서브시스템은 Facade나 클라이언트로부터 직접 요청을 받을 수 있습니다.
    서브시스템의 입장에서는 Facade도 단순한 클라이언트일 뿐이며,
    서브시스템의 일부가 아닙니다.
    """

    def operation1(self) -> str:
        return "Subsystem1: 준비 완료"
    
    # ...

    def operation_n(self) -> str:
        return "Subsystem1: 출발"



class Subsystem2:
    """
    일부 Facade는 동시에 여러 서브시스템과 함께 작동할 수 있습니다.
    """

    def operation1(self) -> str:
        return "Subsystem2: 준비 완료"
    
    # ...

    def operation_z(self) -> str:
        return "Subsystem2: 출발"



def client_code(facade: Facade) -> None:
    """
    클라이언트 코드는 Facade가 제공하는 간단한 인터페이스를 통해 복잡한 서스시스템과 작업합니다.
    Facade가 서브시스템의 생명 주기를 관리할 때, 클라이언트는 서브시스템의 존재조차 알지 못할 수도 있습니다.
    이러한 접근 방식은 복잡성을 제어할 수 있게 해줍니다.
    """

    print(facade.operation(), end="")



if __name__ == "__main__":
    # 클라이언트 코드가 이미 서브시스템 객체를 일부 생성한 상태일 수 있습니다.
    # 이 경우 Facade가 새 인스턴스를 생성하는 대신 이 객체들로 Facade를 초기화하는 것이 좋습니다.
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)

# python structural_pattern/facade.py
