from __future__ import annotations
from abc import ABC, abstractmethod



class Command(ABC):
    """
    Command 인터페이스는 명령을 실행하는 메서드를 선언합니다.
    """

    @abstractmethod
    def execute(self) -> None:
        pass



class SimpleCommand(Command):
    """
    일부 명령은 자체적으로 간단한 작업을 구현할 수 있습니다.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload
    
    def execute(self) -> None:
        print(f"SimpleCommand: 저는 간단한 작업을 할 수 있습니다. 예를 들어 ({self._payload}) 출력하기")



class ComplexCommand(Command):
    """
    그러나 일부 명령은 "수신자"라고 불리는 다른 객체에 더 복잡한 작업을 위임할 수 있습니다.
    """

    def __init__(self, receiver: Receiver, a:str, b:str) -> None:
        """
        복잡한 명령은 하나 이상의 수신자 객체와 함께 생성자를 통해 컨텍스트 데이터를 받을 수 있습니다.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        명령은 수신자의 메서드에 위임할 수 있습니다.
        """

        print("ComplexCommand: 복잡한 작업은 수신자 객체에 의해 수행되어야 합니다.", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)



class Receiver:
    """
    Receiver 클래스는 중요한 비즈니스 로직을 포함하고 있습니다. 요청을 수행하는 데 필요한 모든 종류의 작업을
    수행하는 방법을 알고 있습니다. 사실, 어떤 클래스도 수신자가 될 수 있습니다.
    """

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: ({a}) 작업 중.", end="")
    
    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: ({b}) 작업 중.", end="")



class Invoker:
    """
    Invoker는 하나 이상의 명령과 관련이 있습니다. Invoker는 명령에 요청을 보냅니다.
    """

    _on_start = None
    _on_finish = None

    """
    명령을 초기화합니다.
    """

    def set_on_start(self, command: Command):
        self._on_start = command
    
    def set_on_finish(self, command: Command):
        self._on_finish = command
    
    def do_something_important(self) -> None:
        """
        Invoker는 구체적인 명령이나 수신자 클래스에 의존하지 않습니다.
        Inveker는 명령을 실행하여 간접적으로 수신자에게 요청을 전달합니다.
        """

        print("Invoker: 제가 시작하기 전에 무언가를 하길 원하는 사람이 있나요?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()
        
        print("Invoker: ...작업을 수행 중...")

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()



if __name__ == "__main__":
    """
    클라이언트 코드는 Invoker에 어떤 명령이든 파라미터로 설정할 수 있습니다.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("안녕하세요!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "이메일 보내기", "보고서 저장"
    ))
    invoker.do_something_important()

# python behavioral_pattern/command.py