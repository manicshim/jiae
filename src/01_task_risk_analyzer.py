from datetime import datetime


PRIORITY_ORDER = {
    "urgent": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}


# 문자열 날짜를 datetime 객체로 바꿔 날짜 계산을 할 수 있게 만든다.
def parse_date(date_text):
    return datetime.strptime(date_text, "%Y-%m-%d")


# 일수 값이 정수면 깔끔하게, 소수면 소수점 1자리까지 표시한다.
def format_days(value):
    if value == int(value):
        return f"{int(value)}일"
    return f"{value:.1f}일"


# 작업 목록을 분석해 위험 여부, 우선순위 정렬, 전체 요약 정보를 만든다.
def analyze_task_risk(tasks, base_date):
    analyzed_tasks = []

    for task in tasks:
        due_date = parse_date(task["due_date"])
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
        key=lambda task: (PRIORITY_ORDER[task["priority"]], parse_date(task["due_date"])),
    )

    summary = {
        "total_count": len(analyzed_tasks),
        "risk_count": sum(1 for task in analyzed_tasks if task["is_risky"]),
        "normal_count": sum(1 for task in analyzed_tasks if not task["is_risky"]),
        "total_workload_hours": sum(task["workload_hours"] for task in analyzed_tasks),
    }

    return analyzed_tasks, sorted_tasks, summary


# 과제 A의 입력 데이터를 준비하고 Markdown 형식 리포트로 출력한다.
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
    risk_tasks = [task for task in analyzed_tasks if task["is_risky"]]

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


# 이 파일을 직접 실행했을 때 과제 A 리포트를 출력하는 시작점이다.
def main():
    print_task_report()


if __name__ == "__main__":
    main()
