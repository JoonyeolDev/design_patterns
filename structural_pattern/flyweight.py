import json
from typing import Dict



class Flyweight:
    """
    플라이웨이트는 여러 실제 비즈니스 엔터티에 속하는 공통 상태(내재 상태라고도 함)를 저장합니다.
    플라이웨이트는 메서드 매개변수를 통해 나머지 상태(각 엔터티에 고유한 외재 상태)를 받습니다.
    """

    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        print(f"플라이웨이트: 공유상태 ({json.dumps(self._shared_state)}와 고유상태 ({json.dumps(unique_state)})를 표시 중.)", end="")



class FlyweightFactory:
    """
    플라이웨이트 팩토리는 플라이웨이트 객체르 생성하고 관리합니다.
    플라이웨이트가 적절히 공유되도록 보장합니다.
    클라이언트가 플라이웨이트를 요청할 때, 팩토리는 기존 인스턴스를 반환하거나,
    아직 존재하지 않으면 새 인스턴스를 생성하여 반환합니다.
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        """
        주어진 상태에 대한 플라이웨이트의 문자열 해시를 반환합니다.
        """
        return "_".join(sorted(state))
    
    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """
        주어진 상태로 기존 플라이웨이트를 반환하거나 새로 생성합니다.
        """
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: 플라이웨이트를 찾을 수 없습니다. 새로 생성 중")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: 기존 플라이웨이트 재사용 중.")
        
        return self._flyweights[key]
    
    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: {count}개의 플라이웨이트가 있습니다:")
        print("\n".join(map(str, self._flyweights.keys())), end="")



def add_car_to_police_database(
        factory: FlyweightFactory, plates: str, owner: str,
        brand: str, model: str, color: str
) -> None:
    print("\n\n클라이언트: 경찰 데이터베이스에 차를 추가 중입니다.")
    flyweight = factory.get_flyweight([brand, model, color])
    # 클라이언트 코드는 외재 상태를 저장하거나 계산한 후 플라이웨이트의 메서드로 전달합니다.
    flyweight.operation([plates, owner])



if __name__ == "__main__":
    """
    클라이언트 코드는 보통 애플리케이션의 초기화 단계에서 미리 플라이웨이트를 여러 개 생성합니다.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red"
    )
    
    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red"
    )

    print("\n")

    factory.list_flyweights()

# python structural_pattern/flyweight.py
