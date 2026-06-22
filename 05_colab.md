# Google Colab으로 과제 A/B 실행하기

작성일: 2026-06-21

## 1. 이 문서의 목적

이 문서는 로컬 PC에서 `python3` 명령어를 사용할 수 없을 때, Google Colab으로 과제 A와 과제 B Python 코드를 실행하는 방법을 설명한다.

현재 Python 파일은 다음 두 개로 분리되어 있다.

| 과제 | 문자열 정리 파일 | Python 파일 |
| --- | --- | --- |
| 과제 A | `text/01_assignment_A.md` | `src/01_task_risk_analyzer.py` |
| 과제 B | `text/02_assignment_B.md` | `src/02_operational_kpi_analyzer.py` |

`text/01_assignment_A.md`와 `text/02_assignment_B.md`는 이미지 내용을 문장과 단락 기준으로 옮긴 참고 문서다.

현재 Python 구현은 공통 계산을 재사용하고, Markdown 형식 리포트를 출력하도록 정리되어 있다.

---

## 2. Google Colab 접속

브라우저에서 다음 주소로 접속한다.

```text
https://colab.research.google.com
```

새 노트북을 만든다.

```text
File -> New notebook
```

한국어 화면에서는 다음처럼 보일 수 있다.

```text
파일 -> 새 노트
```

---

## 3. 코드 실행 방법

Colab 코드 셀에 Python 코드를 붙여 넣고 실행한다.

실행 방법은 다음 중 하나를 사용한다.

| 방법 | 설명 |
| --- | --- |
| 실행 버튼 | 코드 셀 왼쪽 실행 버튼 클릭 |
| 단축키 | `Shift + Enter` |

먼저 테스트 코드를 실행해 본다.

```python
print("Google Colab Python 실행 테스트")
print("정상 실행되었습니다.")
```

정상 출력:

```text
Google Colab Python 실행 테스트
정상 실행되었습니다.
```

---

## 4. 과제 A를 Colab에서 실행하는 방법

과제 A 파일은 다음 위치에 있다.

```text
src/01_task_risk_analyzer.py
```

실행 절차:

| 순서 | 작업 |
| --- | --- |
| 1 | `src/01_task_risk_analyzer.py` 파일을 연다. |
| 2 | 파일 전체 내용을 복사한다. |
| 3 | Colab 새 코드 셀에 붙여 넣는다. |
| 4 | `Shift + Enter`로 실행한다. |
| 5 | 출력 제목을 확인한다. |

정상 출력 시작 문구:

```text
# 과제 A: 작업 리스크 및 우선순위 분석 리포트
```

Colab 코드 셀에는 아래 터미널 명령어를 넣지 않는다.

```bash
python3 src/01_task_risk_analyzer.py
```

Colab에서는 Python 코드 자체를 붙여 넣어야 한다.

---

## 5. 과제 B를 Colab에서 실행하는 방법

과제 B 파일은 다음 위치에 있다.

```text
src/02_operational_kpi_analyzer.py
```

실행 절차:

| 순서 | 작업 |
| --- | --- |
| 1 | `src/02_operational_kpi_analyzer.py` 파일을 연다. |
| 2 | 파일 전체 내용을 복사한다. |
| 3 | Colab 새 코드 셀에 붙여 넣는다. |
| 4 | `Shift + Enter`로 실행한다. |
| 5 | 출력 제목을 확인한다. |

정상 출력 시작 문구:

```text
# 과제 B: 통합 운영 대시보드 시스템
```

Colab 코드 셀에는 아래 터미널 명령어를 넣지 않는다.

```bash
python3 src/02_operational_kpi_analyzer.py
```

Colab에서는 Python 코드 자체를 붙여 넣어야 한다.

---

## 6. 로컬 실행과 Colab 실행의 차이

| 구분 | 로컬 실행 | Colab 실행 |
| --- | --- | --- |
| 실행 위치 | 터미널 | 웹브라우저 코드 셀 |
| Python 설치 | 필요 | 별도 설치 불필요 |
| 과제 A 실행 | `python3 src/01_task_risk_analyzer.py` | 파일 내용을 코드 셀에 붙여 넣고 실행 |
| 과제 B 실행 | `python3 src/02_operational_kpi_analyzer.py` | 파일 내용을 코드 셀에 붙여 넣고 실행 |

---

## 7. 성공 기준

과제 A는 다음 문구가 보이면 정상이다.

```text
# 과제 A: 작업 리스크 및 우선순위 분석 리포트
```

과제 B는 다음 문구가 보이면 정상이다.

```text
# 과제 B: 통합 운영 대시보드 시스템
```

두 과제가 각각 정상 출력되면 Colab 실행 검증도 완료된 것이다.
