class SingletonMeta(type):
    """
    싱글톤 클래스는 Python에서 여러 가지 방법으로 구현할 수 있습니다.
    가능한 방법에는 기본 클래스, 데코레이터, 메타클래스 등이 있습니다.
    여기서는 메타클래스를 사용할 것입니다. 이 방법이 이 목적에 가장 적합하기 때문입니다.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        `__init__` 인수의 값 변경은 반환된 인스턴스에 영향을 미치지 않습니다.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        마지막으로, 모든 싱글톤은 인스턴스에서 실행될 수 있는 일부 비즈니스 로직을 정의해야 합니다.
        """
        # ...

if __name__ == "__main__":
    # 클라이언트 코드

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("싱글톤이 작동합니다. 두 변수는 동일한 인스턴스를 가집니다.")
    else:
        print("싱글톤이 실패했습니다. 변수들이 다른 인스턴스를 가지고 있습니다")


# python creational_pattern/singleton.py
