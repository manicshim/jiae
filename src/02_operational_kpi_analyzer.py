from datetime import datetime


# 문자열 날짜를 datetime 객체로 바꿔 마감일 계산에 사용한다.
def parse_date(date_text):
    return datetime.strptime(date_text, "%Y-%m-%d")


# 여러 데이터셋을 기반으로 오류율, 적정성, 마감 가능성 등 KPI를 계산한다.
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


# 현재값과 목표값을 비교해 KPI 상태를 정상, 주의, 위험으로 분류한다.
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


# KPI와 원본 데이터를 검사해 대응이 필요한 이슈를 점수순 TOP 5로 뽑는다.
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


# 목표에 미달한 KPI를 기준으로 개선 액션, 예상 효과, 우선순위를 만든다.
def create_recommendations(kpis):
    recommendations = []

    if kpis["error_rate"] > 5:
        recommendations.append(
            {
                "title": "오류율 개선",
                "action": "오류가 집중된 시간대의 처리 로직과 데이터 수집 경로를 점검한다.",
                "effect": "오류율 5% 이하 회복",
                "priority": "높음",
            }
        )

    if kpis["item_suitability"] < 100:
        recommendations.append(
            {
                "title": "항목 적정성 개선",
                "action": "기준 미달 항목을 즉시 보충하고 최소 보유량 알림을 설정한다.",
                "effect": "항목 적정성 100% 달성",
                "priority": "높음",
            }
        )

    if kpis["deadline_possibility"] < 95:
        recommendations.append(
            {
                "title": "마감 가능성 개선",
                "action": "urgent/high 작업을 먼저 배정하고 지연 위험 작업의 담당 시간을 확보한다.",
                "effect": "마감 가능성 95% 이상 회복",
                "priority": "높음",
            }
        )

    if kpis["normal_status_rate"] < 90:
        recommendations.append(
            {
                "title": "정상 상태율 개선",
                "action": "warning 상태의 측정값을 즉시 점검하고 임계치 초과 원인을 분석한다.",
                "effect": "정상 상태율 90% 이상 회복",
                "priority": "중간",
            }
        )

    return recommendations


# 과제 B의 입력 데이터를 준비하고 KPI/이슈/권고사항 리포트를 출력한다.
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

    print("# 과제 B: 통합 운영 대시보드 시스템")
    print()
    print(f"- 기준일: {dashboard_data['date']}")
    print()
    print("## 핵심 운영 지표 (KPI)")
    print()
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
    print("## 긴급 대응 필요 이슈 TOP 5")
    print()
    for index, issue in enumerate(issues, start=1):
        print(f"{index}. **[{issue['level']}] {issue['title']}**")
        print(f"   - 내용: {issue['detail']}")
        print(f"   - 조치: {issue['action']}")

    print()
    print("## AI 기반 개선 권고사항")
    print()
    for index, recommendation in enumerate(recommendations, start=1):
        print(f"{index}. **{recommendation['title']}**")
        print(f"   - 개선 액션: {recommendation['action']}")
        print(f"   - 예상 효과: {recommendation['effect']}")
        print(f"   - 우선순위: {recommendation['priority']}")


# 이 파일을 직접 실행했을 때 과제 B 리포트를 출력하는 시작점이다.
def main():
    print_dashboard_report()


if __name__ == "__main__":
    main()
