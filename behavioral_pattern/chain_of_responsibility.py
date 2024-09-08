from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional



class Handler(ABC):
    """
    Handler 인터페이스는 핸들러 체인을 구축하는 메서드를 선언합니다.
    또한 요청을 처리하는 메서드도 선언합니다.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass



class AbstractHandler(Handler):
    """
    기본 체인 동작은 기본 핸들러 클래스 내에서 구현될 수 있습니다.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # 여기서 핸들러를 반환하면 다음과 같이 핸들러를 편리하게 연결할 수 있습니다.
        # monkey.set_next(squirrel).set_next(dog)
        return handler
    
    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None



"""
모든 구체적인 핸들러는 요청을 처리하거나 체인의 다음 핸들러로 요청을 전달합니다.
"""



class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"원숭이: 내가 {request}를 먹을게"
        return super().handle(request)



class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"다람쥐: 내가 {request}를 먹을게"
        return super().handle(request)



class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"강아지: 내가 {request}를 먹을게"
        return super().handle(request)



def client_code(handler: Handler) -> None:
    """
    클라이언트 코든느 보통 단일 행들러와 작업할 수 있도록 설계됩니다.
    대부분의 경우, 클라이언트는 핸들러가 체인의 일부라는 사실을 알지 못합니다.
    """

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\n클라이언트: 누가 {food}를 먹고 싶나요?")
        result = handler.handle(food)
        if result:
            print(f"    {result}", end="")
        else:
            print(f"    {food}는 그대로 남겨졌습니다.", end="")



if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # 클라이언트는 체인의 첫 번째 핸들러가 아닌 어느 핸들러에도 요청을 보낼 수 있어야 합니다.
    print("체인: 원숭이 > 다람쥐 > 강아지")
    client_code(monkey)
    print("\n")

    print("서브체인: 다람쥐 > 강아지")
    client_code(squirrel)

# python behavioral_pattern/chain_of_responsibility.py