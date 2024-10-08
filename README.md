# 디자인 패턴 예제 코드

이 레포지토리는 디자인 패턴 학습을 목적으로 만들어졌습니다. 코드는 [Refactoring Guru](https://refactoring.guru/ko/design-patterns)에서 제공하는 Python 예제를 쉐도우 코딩 한 것입니다. 이 레포지토리의 코드는 학습과 개인적인 연습 목적으로 작성되었습니다. 

## 포함된 디자인 패턴

이 레포지토리에서는 디자인 패턴을 세 가지 카테고리로 나누어 학습하고 있습니다: 생성 패턴(Creational Patterns), 구조 패턴(Structural Patterns), 행동 패턴(Behavioral Patterns). 각 카테고리에 포함된 패턴들을 아래에 나열하였으며, 완료된 패턴은 체크 표시로 표시되었습니다.

### 생성 패턴 (Creational Patterns)
- [x] **팩토리 메서드 패턴 (Factory Method Pattern)**
- [x] **추상 팩토리 패턴 (Abstract Factory Pattern)**
- [x] **빌더 패턴 (Builder Pattern)**
- [x] **프로토타입 패턴 (Prototype Pattern)**
- [x] **싱글톤 패턴 (Singleton Pattern)**

### 구조 패턴 (Structural Patterns)
- [x] **어댑터 패턴 (Adapter Pattern)**
- [x] **브리지 패턴 (Bridge Pattern)**
- [x] **컴포지트 패턴 (Composite Pattern)**
- [x] **데코레이터 패턴 (Decorator Pattern)**
- [x] **퍼사드 패턴 (Facade Pattern)**
- [x] **플라이웨이트 패턴 (Flyweight Pattern)**
- [x] **프록시 패턴 (Proxy Pattern)**

### 행동 패턴 (Behavioral Patterns)
- [x] **책임 연쇄 패턴 (Chain of Responsibility Pattern)**
- [x] **커맨드 패턴 (Command Pattern)**
- [x] **반복자 패턴 (Iterator Pattern)**
- [x] **중재자 패턴 (Mediator Pattern)**
- [x] **메멘토 패턴 (Memento Pattern)**
- [x] **옵저버 패턴 (Observer Pattern)**
- [x] **상태 패턴 (State Pattern)**
- [x] **전략 패턴 (Strategy Pattern)**
- [x] **템플릿 메서드 패턴 (Template Method Pattern)**
- [x] **방문자 패턴 (Visitor Pattern)**

각 패턴이 완료될 때마다 이 목록에 체크 표시가 추가됩니다. 이 레포지토리는 지속적으로 업데이트되며, 각 패턴의 구현은 해당 이론과 코드 예시를 포함합니다.

## 참고 자료

이 코드는 [Refactoring Guru](https://refactoring.guru/ko/design-patterns)에서 제공하는 디자인 패턴 자료를 바탕으로 작성되었습니다. 보다 자세한 내용은 해당 웹사이트를 참고하시기 바랍니다.

## 사용 방법

코드를 실행하려면, Python(3.7^)이 필요합니다. 각 파일을 독립적으로 실행하여, 디자인 패턴이 어떻게 동작하는지 확인할 수 있습니다.

```bash
python creational_pattern/factory_method.py
python creational_pattern/abstract_factory.py
python creational_pattern/builder.py
python creational_pattern/prototype.py
python creational_pattern/thread_safe_singleton.py
python structural_pattern/adapter.py
python structural_pattern/bridge.py
python structural_pattern/composite.py
python structural_pattern/decorator.py
python structural_pattern/facade.py
python structural_pattern/flyweight.py
python structural_pattern/proxy.py
python behavioral_pattern/chain_of_responsibility.py
python behavioral_pattern/command.py
python behavioral_pattern/iterator.py
python behavioral_pattern/mediator.py
python behavioral_pattern/memento.py
python behavioral_pattern/observer.py
python behavioral_pattern/state.py
python behavioral_pattern/strategy.py
python behavioral_pattern/template_method.py
python behavioral_pattern/visitor.py
