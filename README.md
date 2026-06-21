# Python 이미지 과제 실습 정리

## 개요

이 프로젝트는 `img` 폴더의 JPG 이미지 5장을 분석해 과제 요구사항을 정리하고, 과제 A와 과제 B를 각각 독립 실행 가능한 Python 실습 코드로 분리한 결과물이다.

## 과제 구분

| 과제 | 원본 이미지 | Python 파일 | 목적 |
| --- | --- | --- | --- |
| 과제 A | `img/s1.jpg`, `img/s2.jpg` | `src/01_task_risk_analyzer.py` | 작업 리스크 분석, 우선순위 정렬, 요약 출력 |
| 과제 B | `img/s3.jpg`, `img/s4.jpg`, `img/s5.jpg` | `src/02_operational_kpi_analyzer.py` | 운영 KPI 계산, 긴급 이슈 TOP 5, 개선 권고사항 출력 |

## 파일 구성

| 경로 | 내용 |
| --- | --- |
| `img/s1.jpg` ~ `img/s5.jpg` | 원본 과제 이미지 |
| `01_report.md` | 이미지별 상세 분석 보고서 |
| `text/01_assignment_A.md` | 과제 A 이미지 내용을 문자열로 정리한 문서 |
| `text/02_assignment_B.md` | 과제 B 이미지 내용을 문자열로 정리한 문서 |
| `02_progress.md` | 이미지 분석을 바탕으로 정리한 해야 할 일 |
| `src/01_task_risk_analyzer.py` | 과제 A 실행 코드 |
| `src/02_operational_kpi_analyzer.py` | 과제 B 실행 코드 |
| `03_compelete.md` | 코드 생성 및 검증 완료 보고서 |
| `04_description.md` | 전체 진행 과정을 초보자용으로 설명한 문서 |
| `05_colab.md` | 로컬 Python이 없을 때 Google Colab으로 실행하는 방법 |
| `README.md` | 전체 파일을 간단히 안내하는 문서 |

## 읽는 순서

```text
01_report.md
-> text/01_assignment_A.md
-> text/02_assignment_B.md
-> 02_progress.md
-> src/01_task_risk_analyzer.py
-> src/02_operational_kpi_analyzer.py
-> 03_compelete.md
-> 04_description.md
-> 05_colab.md
```

## 실행 방법

과제 A 실행:

```bash
python3 src/01_task_risk_analyzer.py
```

과제 B 실행:

```bash
python3 src/02_operational_kpi_analyzer.py
```

문법 검증:

```bash
python3 -m py_compile src/01_task_risk_analyzer.py src/02_operational_kpi_analyzer.py
```

## 정상 출력 기준

과제 A는 다음 제목으로 시작한다.

```text
# 과제 A: 작업 리스크 및 우선순위 분석 리포트
```

과제 B는 다음 제목으로 시작한다.

```text
# 과제 B: 통합 운영 대시보드 시스템
```

## 참고

로컬 환경에서 `python3` 명령어를 사용할 수 없다면 `05_colab.md`를 참고해 Google Colab에서 코드를 실행하면 된다.

`img/s2.jpg`의 예시 출력에는 `작업C`가 위험 작업으로 표시되지만, 공식 판정식 기준으로는 위험 작업이 아니다. 따라서 과제 A 코드는 공식 기준을 우선해 `작업D`만 위험 작업으로 처리한다.
