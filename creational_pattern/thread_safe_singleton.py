from threading import Lock, Thread
from typing import Any



class SingletonMeta(type):
    """
    스레드에 안전한 싱글톤 구현입니다.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    이제 싱글톤에 첫 접근 시 스레드를 동기화하는 데 사용될 락 객체를 가지고 있습니다.
    """

    def __call__(cls, *args, **kwargs):
        """
        `__init__` 인수의 값 변경은 반환된 인스턴스에 영향을 미치지 않습니다.
        """
        # 이제 프로그램이 막 시작되었다고 가정해보면, 아직 싱글톤 인스턴스가 없으므로
        # 여러 스레드가 이전 조건문을 동시에 통과하여 거의 동시에 이 지점에 도달할 수 있습니다.
        # 그 중 첫 번째 스레드는 락을 획득하고 계속 진행하는 반면, 나머지 스레드는 여기서 대기합니다.
        with cls._lock:
            # 락을 획득한 첫 번째 스레드는 이 조건문에 도달하여
            # 내부로 들어가 싱글톤 인스턴스를 생성합니다.
            # 락 블록을 벗어나면 락 해제를 기다리고 있던 다른 스레드가 이 섹션에 진입할 수 있습니다.
            # 하지만 싱글톤 필드가 이미 초기화되었기 때문에, 스레드는 새 객체를 생성하지 않습니다.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]



class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
    이 속성을 사용하여 싱글톤이 제대로 작동하는지 증명할 것입니다.
    """

    def __init__(self, value: str) -> None:
        self.value = value
    
    def some_business_logic(self):
        """
        마지막으로, 모든 싱글톤은 인스턴스에서 실행될 수 있는 일부 비즈니스 로직을 정의해야 합니다.
        """



def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)



if __name__ == "__main__":
    # 클라이언트 코드

    print(
        "같은 값이 보이면 싱글톤이 재사용된 것입니다."
        "다른 값이 보이면 두 개의 싱글톤이 생성된 것입니다."
        )
    
    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()

# python creational_pattern/thread_safe_singleton.py
