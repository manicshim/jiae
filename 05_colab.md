# 로컬 Python이 없을 때 Google Colab으로 실습 코드 실행하기

작성일: 2026-06-20

## 1. 이 문서의 목적

이 문서는 로컬 PC나 개발환경에서 `python3` 명령어를 사용할 수 없을 때, Google Colab을 이용해 Python 코드를 실행하는 방법을 설명한다.

다음과 같은 상황에서 이 문서를 보면 된다.

| 상황 | 설명 |
| --- | --- |
| `python3 --version` 명령이 안 된다. | PC에 Python이 설치되어 있지 않을 수 있다. |
| 터미널 사용이 어렵다. | 웹브라우저에서 코드를 실행하는 방식이 더 쉽다. |
| 개발환경 설정이 막힌다. | Google Colab은 별도 설치 없이 Python을 실행할 수 있다. |
| 코드가 실제로 동작하는지 보고 싶다. | 코드 셀에 붙여 넣고 실행 결과를 바로 확인할 수 있다. |

핵심은 다음과 같다.

```text
로컬에서 python3 명령어가 안 되면,
Google Colab 웹페이지에서 Python 코드를 붙여 넣고 실행하면 된다.
```

---

## 2. Google Colab이란

Google Colab은 웹브라우저에서 Python 코드를 실행할 수 있는 서비스다.

초보자 입장에서는 다음 장점이 있다.

- Python을 따로 설치하지 않아도 된다.
- 코드 입력 칸에 Python 코드를 붙여 넣고 바로 실행할 수 있다.
- 실행 결과가 코드 바로 아래에 표시된다.
- 간단한 실습과 검증에 적합하다.

---

## 3. Google Colab 접속 방법

웹브라우저를 열고 주소창에 다음 주소를 입력한다.

```text
https://colab.research.google.com
```

접속 후 새 노트북을 만든다.

영문 메뉴라면 다음 순서로 누른다.

```text
File -> New notebook
```

한국어 메뉴라면 다음처럼 보일 수 있다.

```text
파일 -> 새 노트
```

새 노트북이 열리면 코드 입력 칸이 보인다. 이 입력 칸을 `코드 셀`이라고 부른다.

---

## 4. Colab에서 코드 실행하는 방법

코드 셀에 Python 코드를 입력하거나 붙여 넣은 뒤 실행한다.

실행 방법은 두 가지다.

| 방법 | 설명 |
| --- | --- |
| 실행 버튼 클릭 | 코드 셀 왼쪽의 실행 버튼을 누른다. |
| 단축키 사용 | `Shift + Enter`를 누른다. |

초보자는 먼저 아래 테스트 코드를 실행해 본다.

```python
print("Python 실행 테스트")
print("Google Colab에서 정상 실행되었습니다.")
```

정상 실행되면 아래처럼 출력된다.

```text
Python 실행 테스트
Google Colab에서 정상 실행되었습니다.
```

이 결과가 보이면 Colab에서 Python 코드를 실행할 준비가 된 것이다.

---

## 5. 첫 번째 과제 코드 실행 예제

아래 코드는 `img/s1.jpg`, `img/s2.jpg`에 나온 작업 리스크 및 우선순위 분석 과제를 Google Colab에서 바로 실행할 수 있도록 만든 예제다.

Colab 코드 셀에 그대로 붙여 넣고 실행한다.

```python
from datetime import datetime

priority_order = {
    "urgent": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}

tasks = [
    {
        "task_id": "T001",
        "name": "작업A",
        "workload_hours": 8,
        "due_date": "2026-01-30",
        "priority": "high",
    },
    {
        "task_id": "T002",
        "name": "작업B",
        "workload_hours": 12,
        "due_date": "2026-02-05",
        "priority": "medium",
    },
    {
        "task_id": "T003",
        "name": "작업C",
        "workload_hours": 4,
        "due_date": "2026-01-28",
        "priority": "urgent",
    },
    {
        "task_id": "T004",
        "name": "작업D",
        "workload_hours": 10,
        "due_date": "2026-01-27",
        "priority": "high",
    },
    {
        "task_id": "T005",
        "name": "작업E",
        "workload_hours": 6,
        "due_date": "2026-02-10",
        "priority": "low",
    },
]

base_date = datetime.strptime("2026-01-26", "%Y-%m-%d")
analyzed_tasks = []

for task in tasks:
    due_date = datetime.strptime(task["due_date"], "%Y-%m-%d")
    remaining_days = (due_date - base_date).days
    required_days = task["workload_hours"] / 8
    is_risky = remaining_days < required_days

    analyzed_tasks.append(
        {
            **task,
            "remaining_days": remaining_days,
            "required_days": required_days,
            "is_risky": is_risky,
        }
    )

sorted_tasks = sorted(
    analyzed_tasks,
    key=lambda task: (
        priority_order[task["priority"]],
        datetime.strptime(task["due_date"], "%Y-%m-%d"),
    ),
)

risk_tasks = [task for task in analyzed_tasks if task["is_risky"]]

print("=== 작업 리스크 및 우선순위 분석 리포트 ===")
print()
print(f"[위험 작업] {len(risk_tasks)}건")

for task in risk_tasks:
    print(f"작업: {task['name']} ({task['task_id']})")
    print(f"남은 일수: {task['remaining_days']}일 / 소요 일수: {task['required_days']:.1f}일")

print()
print("[작업 우선순위]")
for index, task in enumerate(sorted_tasks, start=1):
    print(f"{index}. {task['name']} ({task['task_id']}) - {task['priority']}, 마감 {task['due_date']}")

print()
print("[요약]")
print(f"전체 작업 수: {len(analyzed_tasks)}건")
print(f"위험 작업 수: {len(risk_tasks)}건")
print(f"정상 작업 수: {len(analyzed_tasks) - len(risk_tasks)}건")
print(f"총 작업 시간: {sum(task['workload_hours'] for task in analyzed_tasks)}시간")
```

정상 실행되면 다음과 비슷한 결과가 나온다.

```text
=== 작업 리스크 및 우선순위 분석 리포트 ===

[위험 작업] 1건
작업: 작업D (T004)
남은 일수: 1일 / 소요 일수: 1.2일

[작업 우선순위]
1. 작업C (T003) - urgent, 마감 2026-01-28
2. 작업D (T004) - high, 마감 2026-01-27
3. 작업A (T001) - high, 마감 2026-01-30
4. 작업B (T002) - medium, 마감 2026-02-05
5. 작업E (T005) - low, 마감 2026-02-10
```

---

## 6. 전체 실습 파일을 Colab에서 실행하는 방법

이미 만들어진 전체 실습 파일은 다음 위치에 있다.

```text
src/practice.py
```

로컬에서 Python 명령어를 사용할 수 없다면, 이 파일의 내용을 Google Colab으로 옮겨 실행하면 된다.

절차는 다음과 같다.

| 순서 | 작업 |
| --- | --- |
| 1 | `src/practice.py` 파일을 연다. |
| 2 | 파일 전체 내용을 복사한다. |
| 3 | Google Colab 새 노트북을 연다. |
| 4 | 코드 셀에 복사한 코드를 붙여 넣는다. |
| 5 | `Shift + Enter`를 눌러 실행한다. |
| 6 | 결과 출력이 정상인지 확인한다. |

Colab에서는 아래 명령어를 코드 셀에 입력하지 않는다.

```bash
python3 src/practice.py
```

위 명령어는 터미널에서 사용하는 명령어다.

Colab에서는 Python 코드 자체를 코드 셀에 붙여 넣고 실행해야 한다.

---

## 7. Colab 실행 성공 기준

Colab에서 전체 실습 코드가 정상 실행되면 아래 두 문구가 모두 출력된다.

첫 번째 리포트 시작 문구:

```text
=== 작업 리스크 및 우선순위 분석 리포트 ===
```

두 번째 리포트 시작 문구:

```text
| 통합 운영 대시보드 시스템 |
```

이 두 문구가 모두 보이면 다음 내용이 정상 처리된 것이다.

- 작업 리스크 분석
- 작업 우선순위 정렬
- 작업 요약 출력
- 대시보드 KPI 계산
- 긴급 대응 필요 이슈 TOP 5 출력
- AI 기반 개선 권고사항 출력

---

## 8. 로컬 실행과 Colab 실행의 차이

| 구분 | 로컬 실행 | Google Colab 실행 |
| --- | --- | --- |
| 실행 위치 | 내 PC 터미널 | 웹브라우저 |
| Python 설치 | 필요함 | 별도 설치 불필요 |
| 실행 방식 | `python3 src/practice.py` | 코드 셀에 붙여 넣고 실행 |
| 결과 확인 | 터미널 출력 | 코드 셀 아래 출력 |
| 추천 상황 | 개발환경이 준비되어 있을 때 | Python 설치가 어렵거나 빠르게 확인할 때 |

---

## 9. 자주 하는 실수

### 9.1 Colab 코드 셀에 터미널 명령어를 입력하는 경우

아래 명령어는 터미널용이다.

```bash
python3 src/practice.py
```

Colab 코드 셀에는 이 명령어를 넣는 것이 아니라 Python 코드를 넣어야 한다.

### 9.2 코드 일부만 복사하는 경우

`src/practice.py` 전체를 실행하려면 파일 내용을 처음부터 끝까지 모두 복사해야 한다.

일부 함수만 복사하면 다음과 같은 오류가 날 수 있다.

```text
NameError: name 'main' is not defined
```

또는 다음 오류가 날 수 있다.

```text
NameError: name 'parse_date' is not defined
```

이 오류는 필요한 함수가 코드 셀에 없다는 뜻이다.

### 9.3 들여쓰기가 깨지는 경우

Python은 들여쓰기가 중요하다.

정상 예시는 다음과 같다.

```python
if True:
    print("정상")
```

오류 예시는 다음과 같다.

```python
if True:
print("오류")
```

Colab에 붙여 넣은 뒤 들여쓰기가 깨졌다면 원본 코드에서 다시 복사해 붙여 넣는 것이 좋다.

---

## 10. 결론

로컬 PC에서 Python 명령어가 실행되지 않아도 실습을 포기할 필요는 없다.

Google Colab을 사용하면 웹브라우저에서 Python 코드를 붙여 넣고 바로 실행할 수 있다.

이 실습에서는 다음 두 가지 방식 중 하나를 선택하면 된다.

| 방법 | 사용 조건 |
| --- | --- |
| 로컬 실행 | Python이 설치되어 있고 터미널 사용이 가능할 때 |
| Google Colab 실행 | Python 설치가 어렵거나 웹에서 바로 결과를 확인하고 싶을 때 |

최종적으로는 어떤 방식을 사용하든 아래 두 리포트가 출력되면 실습이 정상 완료된 것이다.

```text
=== 작업 리스크 및 우선순위 분석 리포트 ===
```

```text
| 통합 운영 대시보드 시스템 |
```
