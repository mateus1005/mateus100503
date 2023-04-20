from datetime import datetime, timedelta
from typing import List

def generate_timetable(days: int, work_days: int, rest_days: int, start_date: datetime) -> List[datetime]:
    timetable = []
    for i in range(days):
        if i % (work_days + rest_days) < work_days:
            timetable.append(start_date)
        start_date += timedelta(days=1)
    return timetable
timetable = generate_timetable(days=5, work_days=2, rest_days=1, start_date=datetime(2020, 1, 30))
print(timetable)