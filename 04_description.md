# Python 이미지 과제 분리 실습 진행 설명서

작성일: 2026-06-21

## 목차

1. 프롤로그
2. 최종 결과물
3. 과제 A와 과제 B 구분
4. 문서 생성 흐름
5. Python 코드 분리 흐름
6. 실행 및 검증 방법
7. 초보자를 위한 따라 하기 명령어
8. 자주 헷갈리는 부분
9. 최종 완료 기준

---

## 1. 프롤로그

이 문서는 `img` 폴더의 JPG 이미지 5장을 분석한 뒤, 과제 A와 과제 B를 각각 독립 Python 파일로 분리한 과정을 설명한다.

과제 A와 과제 B는 서로 다른 이미지 묶음에서 나온 별도 과제이므로, 최종 구조에서는 두 개의 Python 파일로 나누었다.

이 문서의 목적은 다음과 같다.

| 목적 | 설명 |
| --- | --- |
| 과제 구분 | 어떤 이미지가 과제 A이고 어떤 이미지가 과제 B인지 설명한다. |
| 코드 위치 안내 | 각 과제를 어떤 Python 파일로 실행하는지 설명한다. |
| 검증 방법 안내 | 문법 검사와 실행 검증 명령어를 제시한다. |
| 초보자 안내 | 터미널에서 어떤 순서로 명령어를 입력해야 하는지 정리한다. |

---

## 2. 최종 결과물

최종 폴더 구조의 핵심 파일은 다음과 같다.

```text
.
├── README.md
├── 01_report.md
├── text
│   ├── 01_assignment_A.md
│   └── 02_assignment_B.md
├── 02_progress.md
├── 03_compelete.md
├── 04_description.md
├── 05_colab.md
├── img
│   ├── s1.jpg
│   ├── s2.jpg
│   ├── s3.jpg
│   ├── s4.jpg
│   └── s5.jpg
└── src
    ├── 01_task_risk_analyzer.py
    └── 02_operational_kpi_analyzer.py
```

파일별 역할은 다음과 같다.

| 파일 | 역할 |
| --- | --- |
| `README.md` | 전체 구성 요약 |
| `01_report.md` | 이미지별 상세 분석 보고서 |
| `text/01_assignment_A.md` | 과제 A 이미지 내용을 문자열로 정리한 문서 |
| `text/02_assignment_B.md` | 과제 B 이미지 내용을 문자열로 정리한 문서 |
| `02_progress.md` | 과제별 해야 할 일 정리 |
| `03_compelete.md` | 코드 분리 및 검증 완료 보고서 |
| `04_description.md` | 전체 진행 설명서 |
| `05_colab.md` | Google Colab 대체 실행 안내 |
| `src/01_task_risk_analyzer.py` | 과제 A 실행 코드 |
| `src/02_operational_kpi_analyzer.py` | 과제 B 실행 코드 |

---

## 3. 과제 A와 과제 B 구분

이미지 5장은 다음처럼 두 과제로 나뉜다.

| 과제 | 이미지 | 문자열 파일 | 구현 파일 |
| --- | --- | --- | --- |
| 과제 A | `img/s1.jpg`, `img/s2.jpg` | `text/01_assignment_A.md` | `src/01_task_risk_analyzer.py` |
| 과제 B | `img/s3.jpg`, `img/s4.jpg`, `img/s5.jpg` | `text/02_assignment_B.md` | `src/02_operational_kpi_analyzer.py` |

### 과제 A

과제 A는 작업 리스크 및 우선순위 분석 프로그램이다.

처리 내용은 다음과 같다.

- 작업별 남은 일수 계산
- 작업별 예상 소요 일수 계산
- 위험 작업 판정
- 작업 우선순위 정렬
- 전체 작업 요약 출력
- 중복 날짜 파싱 최소화

대표 출력 제목은 다음과 같다.

```text
# 과제 A: 작업 리스크 및 우선순위 분석 리포트
```

### 과제 B

과제 B는 통합 운영 대시보드 시스템이다.

처리 내용은 다음과 같다.

- 오류율 계산
- 항목 적정성 계산
- 마감 가능성 계산
- 정상 상태 비율 계산
- 종합 점수 계산
- 긴급 대응 필요 이슈 TOP 5 출력
- AI 기반 개선 권고사항 출력
- 공통 일정 분석 재사용과 빈 데이터 방어

대표 출력 제목은 다음과 같다.

```text
# 과제 B: 통합 운영 대시보드 시스템
```

---

## 4. 문서 생성 흐름

문서 흐름은 다음과 같다.

```text
이미지 확인
-> 01_report.md 작성
-> text/01_assignment_A.md, text/02_assignment_B.md 작성
-> 02_progress.md 작성
-> Python 파일 분리
-> 03_compelete.md 완료 보고
-> 04_description.md 진행 설명
-> 05_colab.md Colab 보충 안내
```

기존에는 해야 할 일 문서가 `02_task.md`라는 이름으로 작성되었지만, 현재는 다음 이름으로 정정되었다.

```text
02_progress.md
```

---

## 5. Python 코드 분리 흐름

실행 파일은 다음 두 개다.

```text
src/01_task_risk_analyzer.py
src/02_operational_kpi_analyzer.py
```

구성 기준은 다음과 같다.

| 기준 | 설명 |
| --- | --- |
| 과제 A | 작업 리스크 분석 전용 파일로 실행 |
| 과제 B | 운영 KPI 분석 전용 파일로 실행 |
| 실행 방식 | 과제별로 필요한 파일만 실행 |
| 구분 방식 | 파일명으로 과제 구분 |

---

## 6. 실행 및 검증 방법

### Python 설치 확인

```bash
python3 --version
```

### 문법 검사

```bash
python3 -m py_compile src/01_task_risk_analyzer.py src/02_operational_kpi_analyzer.py
```

정상이라면 아무 메시지 없이 종료된다.

### 과제 A 실행

```bash
python3 src/01_task_risk_analyzer.py
```

정상 출력 시작 문구:

```text
# 과제 A: 작업 리스크 및 우선순위 분석 리포트
```

### 과제 B 실행

```bash
python3 src/02_operational_kpi_analyzer.py
```

정상 출력 시작 문구:

```text
# 과제 B: 통합 운영 대시보드 시스템
```

실행 결과는 모두 Markdown 리포트 형식이며, 공식 판정식과 KPI 계산식을 기준으로 출력된다.
함수별 상단 주석도 처리 흐름이 보이도록 상세하게 정리했다.

---

## 7. 초보자를 위한 따라 하기 명령어

프로젝트 폴더로 이동한다.

```bash
cd /home/username/python/sample
```

이미지와 문서를 확인한다.

```bash
ls img
ls README.md 01_report.md 02_progress.md 03_compelete.md 04_description.md 05_colab.md
ls text/01_assignment_A.md text/02_assignment_B.md
```

Python 파일을 확인한다.

```bash
ls src/01_task_risk_analyzer.py src/02_operational_kpi_analyzer.py
```

문법 검사를 실행한다.

```bash
python3 -m py_compile src/01_task_risk_analyzer.py src/02_operational_kpi_analyzer.py
```

과제 A를 실행한다.

```bash
python3 src/01_task_risk_analyzer.py
```

과제 B를 실행한다.

```bash
python3 src/02_operational_kpi_analyzer.py
```

---

## 8. 자주 헷갈리는 부분

### 어떤 파일을 실행해야 하는가

현재 실행 파일은 다음 두 개다.

```text
src/01_task_risk_analyzer.py
src/02_operational_kpi_analyzer.py
```

### `02_task.md`가 없는 것이 맞는가

맞다. 파일명은 `02_progress.md`로 정정되었다.

### Colab에서는 어떻게 실행하는가

로컬에서 Python 실행이 어렵다면 `05_colab.md`를 참고한다. Colab에서는 터미널 명령어가 아니라 Python 코드 내용을 코드 셀에 붙여 넣고 실행한다.

---

## 9. 최종 완료 기준

아래 조건이 모두 만족되면 완료 상태다.

| 완료 조건 | 확인 방법 |
| --- | --- |
| 과제 A 이미지가 있다. | `ls img/s1.jpg img/s2.jpg` |
| 과제 B 이미지가 있다. | `ls img/s3.jpg img/s4.jpg img/s5.jpg` |
| 과제 A 문자열 파일이 있다. | `ls text/01_assignment_A.md` |
| 과제 B 문자열 파일이 있다. | `ls text/02_assignment_B.md` |
| 진행 문서가 있다. | `ls 02_progress.md` |
| 과제 A 코드가 있다. | `ls src/01_task_risk_analyzer.py` |
| 과제 B 코드가 있다. | `ls src/02_operational_kpi_analyzer.py` |
| 문법 검사가 통과한다. | `python3 -m py_compile src/01_task_risk_analyzer.py src/02_operational_kpi_analyzer.py` |
| 과제 A가 실행된다. | `python3 src/01_task_risk_analyzer.py` |
| 과제 B가 실행된다. | `python3 src/02_operational_kpi_analyzer.py` |
