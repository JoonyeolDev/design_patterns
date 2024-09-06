class Target:
    """
    Target은 클라이언트 코드에서 사용되는 도메인 전용 인터페이스를 정의합니다.
    """

    def request(self) -> str:
        return "Target: 기본 타겟의 동작입니다."



class Adaptee:
    """
    Adaptee는 유용한 동작을 포함하고 있지만, 그 인터페이스가 기존 클라이언트 코드와 호환되지 않습니다.
    Adaptee는 클라이언트 코드가 이를 사용하기 전에 약간의 적응이 필요합니다.
    """

    def specific_request(self) -> str:
        return "동행 한별특 의eetpadA"



class Adapter(Target, Adaptee):
    """
    Adapter는 다중 상속을 통해 Adaptee의 인터페이스를 Target의 인터페이스와 호환되도록 만듭니다.
    """

    def request(self) -> str:
        return f"Adaptor: (번역됨) {self.specific_request()[::-1]}"



def client_code(target: Target) -> None:
    """
    클라이언트 코드는 Target 인터페이스를 따르는 모든 클래스를 지원합니다.
    """

    print(target.request(), end="")



if __name__ == "__main__":
    print("클라이언트: 나는 Target 객체들과 잘 작동할 수 있습니다:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("클라이언트: Adaptee 클래스는 이상한 인터페이스를 가지고 있습니다.\n"
          f"Adaptee: {adaptee.specific_request()}", end="\n\n")
    
    print("클라이언트: Adapter를 통해 그것과 작동할 수 있습니다:")
    adapter = Adapter()
    client_code(adapter)

# python structural_pattern/adapter_inheritance.py
