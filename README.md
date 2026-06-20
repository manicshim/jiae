# Python 이미지 과제 실습 정리

## 개요

이 프로젝트는 `img` 폴더의 JPG 이미지 5장을 분석해 과제 요구사항을 정리하고, 해당 요구사항을 Python 실습 코드로 구현한 결과물이다.

이미지는 두 가지 과제를 담고 있다.

1. 작업 리스크 및 우선순위 분석
2. 통합 운영 대시보드 KPI 분석

## 파일 구성

| 경로 | 내용 |
| --- | --- |
| `img/s1.jpg` ~ `img/s5.jpg` | 원본 과제 이미지 |
| `01_report.md` | 이미지별 상세 분석 보고서 |
| `02_task.md` | 이미지 분석을 바탕으로 정리한 해야 할 일 |
| `src/practice.py` | 실제 실행 가능한 Python 실습 코드 |
| `03_compelete.md` | 코드 생성 및 검증 완료 보고서 |
| `04_description.md` | 전체 진행 과정을 초보자용으로 설명한 문서 |
| `05_colab.md` | 로컬 Python이 없을 때 Google Colab으로 실행하는 방법 |
| `README.md` | 전체 파일을 간단히 안내하는 문서 |

## 읽는 순서

처음 보는 경우 아래 순서로 보면 흐름을 빠르게 파악할 수 있다.

```text
01_report.md
-> 02_task.md
-> src/practice.py
-> 03_compelete.md
-> 04_description.md
-> 05_colab.md
```

간단히 실행만 확인하려면 `src/practice.py`와 아래 실행 방법만 보면 된다.

## 실행 방법

프로젝트 폴더에서 다음 명령어를 실행한다.

```bash
python3 -m py_compile src/practice.py
python3 src/practice.py
```

정상 실행되면 다음 두 리포트가 출력된다.

```text
=== 작업 리스크 및 우선순위 분석 리포트 ===
```

```text
| 통합 운영 대시보드 시스템 |
```

## 참고

로컬 환경에서 `python3` 명령어를 사용할 수 없다면 `05_colab.md`를 참고해 Google Colab에서 코드를 실행하면 된다.

`img/s2.jpg`의 예시 출력에는 `작업C`가 위험 작업으로 표시되지만, 공식 판정식 기준으로는 위험 작업이 아니다. 따라서 `src/practice.py`는 공식 기준을 우선해 `작업D`만 위험 작업으로 처리한다.
