from datetime import datetime, timedelta

target_date = datetime(2023, 8, 25)
current_date = datetime.now()

delta = target_date - current_date
print(delta.days)