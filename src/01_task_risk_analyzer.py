from datetime import datetime


PRIORITY_ORDER = {
    "urgent": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}


# 문자열 날짜를 분석용 datetime 객체로 변환한다.
# 모든 마감일 비교와 정렬은 이 파서 결과를 재사용해 일관성을 유지한다.
def parse_date(date_text):
    return datetime.strptime(date_text, "%Y-%m-%d")


# 일수 표기를 리포트용으로 정리한다.
# 정수는 `3일`처럼 단순하게, 소수는 `1.2일`처럼 한 자리까지 보여준다.
def format_days(value):
    if float(value).is_integer():
        return f"{int(value)}일"
    return f"{value:.1f}일"


# 작업 1건의 리스크 분석 결과와 정렬용 마감일 정보를 함께 만든다.
# 반환값에 분석 결과와 파싱된 마감일을 같이 넣어 중복 파싱을 피한다.
def build_task_analysis(task, base_date):
    due_date = parse_date(task["due_date"])
    remaining_days = (due_date - base_date).days
    required_days = task["workload_hours"] / 8

    return {
        **task,
        "remaining_days": remaining_days,
        "required_days": required_days,
        "is_risky": remaining_days < required_days,
    }, due_date


# 작업 전체를 한 번만 순회해 분석 결과, 정렬 결과, 요약 통계를 생성한다.
# 위험 판정과 우선순위 정렬, 집계가 모두 이 함수에서 일관되게 계산된다.
def analyze_task_risk(tasks, base_date):
    analyzed_tasks = []
    total_workload_hours = 0
    risk_count = 0
    sortable_tasks = []

    for task in tasks:
        analyzed_task, due_date = build_task_analysis(task, base_date)
        analyzed_tasks.append(analyzed_task)
        sortable_tasks.append((due_date, analyzed_task))
        total_workload_hours += analyzed_task["workload_hours"]
        risk_count += int(analyzed_task["is_risky"])

    sorted_tasks = [
        task
        for _, task in sorted(
            sortable_tasks,
            key=lambda item: (PRIORITY_ORDER[item[1]["priority"]], item[0]),
        )
    ]

    summary = {
        "total_count": len(analyzed_tasks),
        "risk_count": risk_count,
        "normal_count": len(analyzed_tasks) - risk_count,
        "total_workload_hours": total_workload_hours,
    }

    return analyzed_tasks, sorted_tasks, summary


# 과제 A의 샘플 입력을 준비하고 Markdown 리포트를 출력한다.
# 결과는 표와 목록만 사용해 문서와 동일한 형식으로 보이게 한다.
def print_task_report():
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

    base_date = parse_date("2026-01-26")
    analyzed_tasks, sorted_tasks, summary = analyze_task_risk(tasks, base_date)
    risk_tasks = [task for task in sorted_tasks if task["is_risky"]]

    print("# 과제 A: 작업 리스크 및 우선순위 분석 리포트")
    print()
    print("| 기준일 | 전체 작업 수 | 위험 작업 수 | 정상 작업 수 | 총 작업 시간 |")
    print("| --- | ---: | ---: | ---: | ---: |")
    print(
        f"| 2026-01-26 | {summary['total_count']}건 | "
        f"{summary['risk_count']}건 | {summary['normal_count']}건 | "
        f"{summary['total_workload_hours']}시간 |"
    )
    print()
    print("## 위험 작업")
    print()
    if risk_tasks:
        print("| 작업 | 남은 일수 | 소요 일수 | 판정 |")
        print("| --- | ---: | ---: | --- |")
        for task in risk_tasks:
            print(
                f"| {task['name']} ({task['task_id']}) | "
                f"{format_days(task['remaining_days'])} | "
                f"{format_days(task['required_days'])} | 위험 |"
            )
    else:
        print("위험 작업 없음")

    print()
    print("## 작업 우선순위")
    print()
    print("| 순위 | 작업 | 우선순위 | 마감일 |")
    print("| ---: | --- | --- | --- |")
    for index, task in enumerate(sorted_tasks, start=1):
        print(
            f"| {index} | {task['name']} ({task['task_id']}) | "
            f"{task['priority']} | {task['due_date']} |"
        )

    print()
    print("## 요약")
    print()
    print(f"- 전체 작업 수: {summary['total_count']}건")
    print(f"- 위험 작업 수: {summary['risk_count']}건")
    print(f"- 정상 작업 수: {summary['normal_count']}건")
    print(f"- 총 작업 시간: {summary['total_workload_hours']}시간")


# 모듈 직접 실행 시 과제 A 리포트 생성을 시작한다.
def main():
    print_task_report()


if __name__ == "__main__":
    main()
