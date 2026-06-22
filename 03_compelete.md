# 실습 코드 분리 생성 및 검증 완료 보고서

작성일: 2026-06-21

## 요청 내용

`img/s1.jpg`, `img/s2.jpg`는 과제 A로 분류하고, `img/s3.jpg`, `img/s4.jpg`, `img/s5.jpg`는 과제 B로 분류한다.

과제별 분기 처리가 필요하므로 다음 두 파일로 구현했다.

| 과제 | 원본 이미지 | 생성 파일 |
| --- | --- | --- |
| 과제 A | `img/s1.jpg`, `img/s2.jpg` | `src/01_task_risk_analyzer.py` |
| 과제 B | `img/s3.jpg`, `img/s4.jpg`, `img/s5.jpg` | `src/02_operational_kpi_analyzer.py` |

이미지 내용은 과제별 문자열 문서로도 정리했다.

| 과제 | 문자열 정리 파일 |
| --- | --- |
| 과제 A | `text/01_assignment_A.md` |
| 과제 B | `text/02_assignment_B.md` |

## 완료 결과

생성된 Python 파일은 다음과 같다.

```text
src/01_task_risk_analyzer.py
src/02_operational_kpi_analyzer.py
```

정정된 진행 문서명은 다음과 같다.

```text
02_progress.md
```

기존 파일명 `02_task.md`는 더 이상 사용하지 않는다.

## 과제 A 반영 내용

과제 A는 작업 리스크 및 우선순위 분석 프로그램이다.

구현 파일:

```text
src/01_task_risk_analyzer.py
```

구현 내용:

- 작업별 남은 일수 계산
- 작업별 예상 소요 일수 계산
- 위험 작업 판정
- `urgent > high > medium > low` 기준 작업 정렬
- 동일 우선순위 내 빠른 마감일 우선 정렬
- Markdown 형식 리포트 출력
- 중복 날짜 파싱을 줄인 분석 로직 적용

대표 출력 시작 문구:

```text
# 과제 A: 작업 리스크 및 우선순위 분석 리포트
```

공식 판정식 기준으로 `작업D(T004)`가 위험 작업으로 계산된다.

## 과제 B 반영 내용

과제 B는 통합 운영 대시보드 시스템이다.

구현 파일:

```text
src/02_operational_kpi_analyzer.py
```

구현 내용:

- 오류율 계산
- 항목 적정성 계산
- 마감 가능성 계산
- 정상 상태 비율 계산
- 종합 점수 계산
- 긴급 대응 필요 이슈 TOP 5 출력
- AI 기반 개선 권고사항 출력
- Markdown 형식 리포트 출력
- 공통 일정 분석 결과 재사용 및 빈 데이터 방어

대표 출력 시작 문구:

```text
# 과제 B: 통합 운영 대시보드 시스템
```

## 실행 검증

문법 검증 명령:

```bash
python3 -m py_compile src/01_task_risk_analyzer.py src/02_operational_kpi_analyzer.py
```

과제 A 실행 명령:

```bash
python3 src/01_task_risk_analyzer.py
```

과제 B 실행 명령:

```bash
python3 src/02_operational_kpi_analyzer.py
```

검증 결과:

- 과제 A 문법 검사 정상
- 과제 B 문법 검사 정상
- 과제 A 실행 정상
- 과제 B 실행 정상

## 갱신된 문서

다음 파일의 참조 내용을 새 구조에 맞춰 갱신했다.

| 파일 | 갱신 내용 |
| --- | --- |
| `README.md` | 과제 A/B 분류, 실행 파일, 실행 명령 정리 |
| `01_report.md` | 이미지별 과제 A/B 분류 추가 |
| `text/01_assignment_A.md` | 과제 A 이미지 내용을 문자열 형태로 정리 |
| `text/02_assignment_B.md` | 과제 B 이미지 내용을 문자열 형태로 정리 |
| `02_progress.md` | 기존 `02_task.md` 역할을 새 파일명으로 정리 |
| `03_compelete.md` | 코드 분리 완료 보고로 재작성 |
| `04_description.md` | 실행 파일명과 검증 명령 갱신 |
| `05_colab.md` | Colab 실행 안내를 과제 A/B 파일 기준으로 갱신 |

## 최종 결론

과제 A와 과제 B는 각각 독립 Python 파일로 분리되었다.

현재 실행 기준은 다음 두 파일이다.

```text
src/01_task_risk_analyzer.py
src/02_operational_kpi_analyzer.py
```

두 파일 모두 공식 판정식과 데이터 기준을 우선하며, 중복 계산을 줄인 형태로 정리되어 있다.

함수 상단 주석도 입력, 계산, 출력 역할이 드러나도록 상세하게 정리했다.
