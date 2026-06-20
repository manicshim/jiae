from datetime import datetime


PRIORITY_ORDER = {
    "urgent": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}


def parse_date(date_text):
    return datetime.strptime(date_text, "%Y-%m-%d")


def format_days(value):
    if value == int(value):
        return f"{int(value)}일"
    return f"{value:.1f}일"


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

    print("=== 작업 리스크 및 우선순위 분석 리포트 ===")
    print()
    print(f"[위험 작업] {len(risk_tasks)}건")
    if risk_tasks:
        for task in risk_tasks:
            print(f"작업: {task['name']} ({task['task_id']})")
            print(
                "남은 일수: "
                f"{format_days(task['remaining_days'])} / "
                f"소요 일수: {format_days(task['required_days'])}"
            )
    else:
        print("위험 작업 없음")

    print()
    print("[작업 우선순위]")
    for index, task in enumerate(sorted_tasks, start=1):
        print(
            f"{index}. {task['name']} ({task['task_id']}) - "
            f"{task['priority']}, 마감 {task['due_date']}"
        )

    print()
    print("[요약]")
    print(f"전체 작업 수: {summary['total_count']}건")
    print(f"위험 작업 수: {summary['risk_count']}건")
    print(f"정상 작업 수: {summary['normal_count']}건")
    print(f"총 작업 시간: {summary['total_workload_hours']}시간")


def calculate_dashboard_kpis(data):
    total_count = sum(item["total"] for item in data["dataset1"])
    error_count = sum(item["errors"] for item in data["dataset1"])
    error_rate = error_count / total_count * 100

    suitable_items = [
        item
        for item in data["dataset2"]
        if item["min_required"] <= item["current"] <= item["max_allowed"]
    ]
    item_suitability = len(suitable_items) / len(data["dataset2"]) * 100

    base_date = parse_date(data["date"])
    possible_tasks = []
    for task in data["dataset3"]:
        remaining_days = (parse_date(task["due_date"]) - base_date).days
        required_days = task["workload_hours"] / 8
        if remaining_days >= required_days:
            possible_tasks.append(task)
    deadline_possibility = len(possible_tasks) / len(data["dataset3"]) * 100

    normal_status_count = sum(1 for item in data["dataset4"] if item["status"] == "normal")
    normal_status_rate = normal_status_count / len(data["dataset4"]) * 100

    error_score = max(0, 100 - max(0, error_rate - 5) * 10)
    total_score = (
        error_score + item_suitability + deadline_possibility + normal_status_rate
    ) / 4

    return {
        "error_rate": error_rate,
        "item_suitability": item_suitability,
        "deadline_possibility": deadline_possibility,
        "normal_status_rate": normal_status_rate,
        "total_score": total_score,
    }


def grade_status(current, target, mode):
    if mode == "under":
        if current <= target:
            return "정상"
        if current <= target * 1.2:
            return "주의"
        return "위험"

    if current >= target:
        return "정상"
    if current >= target * 0.8:
        return "주의"
    return "위험"


def find_dashboard_issues(data, kpis):
    issues = []

    if kpis["error_rate"] > 5:
        issues.append(
            {
                "score": 90,
                "level": "크리티컬",
                "title": "오류율 목표 초과",
                "detail": f"현재 오류율 {kpis['error_rate']:.1f}%, 목표 5.0%",
                "action": "오류 발생 시간대를 우선 점검",
            }
        )

    for item in data["dataset2"]:
        if item["current"] < item["min_required"]:
            days_left = item["current"] / item["daily_usage"]
            issues.append(
                {
                    "score": 88,
                    "level": "중요",
                    "title": "항목 부족",
                    "detail": f"{item['name']}: 기준 미달, {days_left:.1f}일 후 소진 예상",
                    "action": "보충 필요",
                }
            )

    base_date = parse_date(data["date"])
    for task in data["dataset3"]:
        remaining_days = (parse_date(task["due_date"]) - base_date).days
        required_days = task["workload_hours"] / 8
        if remaining_days < required_days or task["priority"] == "urgent":
            issues.append(
                {
                    "score": 95 if task["priority"] == "urgent" else 85,
                    "level": "크리티컬",
                    "title": "작업 일정 지연 위험",
                    "detail": (
                        f"{task['task_id']}: 마감 {remaining_days}일 전, "
                        f"소요 {required_days:.1f}일"
                    ),
                    "action": "우선 처리 필요",
                }
            )

    warning_count = sum(1 for item in data["dataset4"] if item["status"] != "normal")
    if warning_count:
        issues.append(
            {
                "score": 92,
                "level": "크리티컬",
                "title": "비정상 데이터 감지",
                "detail": "value1/value2/value3 급변 또는 warning 상태 감지",
                "action": "즉시 점검",
            }
        )

    if kpis["total_score"] < 90:
        issues.append(
            {
                "score": 80,
                "level": "중요",
                "title": "종합 점수 목표 미달",
                "detail": f"현재 종합 점수 {kpis['total_score']:.1f}점, 목표 90점",
                "action": "미달 KPI별 개선 계획 수립",
            }
        )

    return sorted(issues, key=lambda issue: issue["score"], reverse=True)[:5]


def create_recommendations(kpis):
    recommendations = []

    if kpis["error_rate"] > 5:
        recommendations.append(
            "오류율 개선: 오류가 집중된 시간대의 처리 로직과 데이터 수집 경로를 점검한다. "
            "예상 효과: 오류율 5% 이하 회복. 우선순위: 높음"
        )

    if kpis["item_suitability"] < 100:
        recommendations.append(
            "항목 적정성 개선: 기준 미달 항목을 즉시 보충하고 최소 보유량 알림을 설정한다. "
            "예상 효과: 항목 적정성 100% 달성. 우선순위: 높음"
        )

    if kpis["deadline_possibility"] < 95:
        recommendations.append(
            "마감 가능성 개선: urgent/high 작업을 먼저 배정하고 지연 위험 작업의 담당 시간을 확보한다. "
            "예상 효과: 마감 가능성 95% 이상 회복. 우선순위: 높음"
        )

    if kpis["normal_status_rate"] < 90:
        recommendations.append(
            "정상 상태율 개선: warning 상태의 측정값을 즉시 점검하고 임계치 초과 원인을 분석한다. "
            "예상 효과: 정상 상태율 90% 이상 회복. 우선순위: 중간"
        )

    return recommendations


def print_dashboard_report():
    dashboard_data = {
        "dataset1": [
            {"hour": 0, "total": 120, "errors": 5},
            {"hour": 1, "total": 115, "errors": 3},
            {"hour": 2, "total": 118, "errors": 8},
            {"hour": 3, "total": 125, "errors": 15},
            {"hour": 4, "total": 122, "errors": 4},
            {"hour": 5, "total": 130, "errors": 6},
        ],
        "dataset2": [
            {
                "id": "I001",
                "name": "항목1",
                "current": 50,
                "min_required": 100,
                "max_allowed": 500,
                "daily_usage": 15,
            },
            {
                "id": "I002",
                "name": "항목2",
                "current": 5000,
                "min_required": 1000,
                "max_allowed": 8000,
                "daily_usage": 200,
            },
        ],
        "dataset3": [
            {
                "task_id": "T001",
                "name": "작업A",
                "due_date": "2026-01-30",
                "priority": "high",
                "workload_hours": 8,
            },
            {
                "task_id": "T003",
                "name": "작업C",
                "due_date": "2026-01-28",
                "priority": "urgent",
                "workload_hours": 4,
            },
        ],
        "dataset4": [
            {
                "time": "03:00",
                "value1": 95,
                "value2": 4.2,
                "value3": 6.1,
                "status": "warning",
            },
            {
                "time": "04:00",
                "value1": 88,
                "value2": 3.5,
                "value3": 5.8,
                "status": "normal",
            },
        ],
        "date": "2026-01-26",
    }

    kpis = calculate_dashboard_kpis(dashboard_data)
    issues = find_dashboard_issues(dashboard_data, kpis)
    recommendations = create_recommendations(kpis)

    print()
    print("=" * 60)
    print()
    print("| 통합 운영 대시보드 시스템 |")
    print(f"| {dashboard_data['date']} |")
    print()
    print("[핵심 운영 지표 (KPI)]")
    print("| 지표 | 현재값 | 목표값 | 상태 |")
    print("| --- | ---: | ---: | --- |")
    print(
        f"| 오류율 | {kpis['error_rate']:.1f}% | 5.0% | "
        f"{grade_status(kpis['error_rate'], 5, 'under')} |"
    )
    print(
        f"| 항목 적정성 | {kpis['item_suitability']:.1f}% | 100% | "
        f"{grade_status(kpis['item_suitability'], 100, 'over')} |"
    )
    print(
        f"| 마감 가능성 | {kpis['deadline_possibility']:.1f}% | 95.0% | "
        f"{grade_status(kpis['deadline_possibility'], 95, 'over')} |"
    )
    print(
        f"| 정상 상태율 | {kpis['normal_status_rate']:.1f}% | 90.0% | "
        f"{grade_status(kpis['normal_status_rate'], 90, 'over')} |"
    )
    print(
        f"| 종합 점수 | {kpis['total_score']:.1f}점 | 90점 | "
        f"{grade_status(kpis['total_score'], 90, 'over')} |"
    )

    print()
    print("[긴급 대응 필요 이슈] TOP 5")
    for index, issue in enumerate(issues, start=1):
        print(f"{index}. [{issue['level']}] {issue['title']}")
        print(f"- {issue['detail']}")
        print(f"- 조치: {issue['action']}")

    print()
    print("[AI 기반 개선 권고사항]")
    for index, recommendation in enumerate(recommendations, start=1):
        print(f"{index}. {recommendation}")


def main():
    print_task_report()
    print_dashboard_report()


if __name__ == "__main__":
    main()
