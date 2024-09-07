from abc import ABC, abstractmethod



class Subject(ABC):
    """
    Subject 인터페이스는 RealSubject와 Proxy 모두를 위한 공통 작업을 선언합니다.
    그 작업은 매우 느리거나 민감할 수 있습니다 - 예: 입력 데이터를 수정하는 것.
    Proxy는 RealSubject의 코드를 변경하지 않고 이러한 문제를 해결할 수 있습니다.
    """

    def request(self) -> None:
        print("RealSubject: 요청을 처리 중입니다.")



class RealSubject(Subject):
    """
    RealSubject는 핵심 비즈니스 로직을 포함합니다. 일반적으로 RealSubject는 유용한 작업을 수행할 수 있으며,
    그 작업은 매우 느리거나 민감할 수 있습니다 - 예: 입력 데이터를 수정하는 것.
    Proxy는 RealSubject의 코드를 변경하지 않고 이러한 문제를 해결할 수 있습니다.
    """

    def request(self) -> None:
        print("RealSubject: 요청을 처리 중입니다.")



class Proxy(Subject):
    """
    Proxy는 RealSubject와 동일한 인터페이스를 가지고 있습니다.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        Proxy 패턴의 가장 일반적인 응용은 지연 로딩, 캐싱, 접근 제어, 로깅 등입니다.
        Proxy는 이러한 작업 중 하나를 수행한 다음, 그 결과에 따라
        연결된 RealSubject 객체의 동일한 메서드로 실행을 넘길 수 있습니다.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()
    
    def check_access(self) -> bool:
        print("Proxy: 시제 요청을 실행하기 전에 접근 권한을 확인 중입니다.")
        return True
    
    def log_access(self) -> None:
        print("Proxy: 요청 시간 로깅 중.", end="")



def client_code(subject: Subject) -> None:
    """
    클라이언트 코드는 실제 주체와 프록시 모두를 지원하기 위해 Subject 인터페이스를 통해 모든 객체와 작업해야 합니다.
    하지만 현실에서는 클라이언트가 대부분 직접 RealSubject와 작업합니다.
    이 경우 패턴을 더 쉽게 구현하려면 프록시가 RealSubject 클래스에서 확장될 수 있습니다.
    """

    # ...

    subject.request()

    # ...



if __name__ == "__main__":
    print("클라이언트: RealSubject와 함께 클라이언트 코드를 실행합니다:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("클라이언트: 동일한 클라이언트 코드는 Proxy와 함께 실행합니다:")
    proxy = Proxy(real_subject)
    client_code(proxy)

# python structural_pattern/proxy.py
