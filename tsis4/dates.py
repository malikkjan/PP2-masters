#Exercise 1
from datetime import datetime, timedelta
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Five days ago from current date:", five_days_ago)

#Exercise 2
from datetime import datetime, timedelta
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", current_date)
print("Tomorrow:", tomorrow)

#Exercise 3
from datetime import datetime
current_datetime = datetime.now()
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)
print("Datetime without microseconds:", current_datetime_without_microseconds)

#Exercise 4
from datetime import datetime
date1 = datetime(2024, 2, 20, 12, 0, 0)
date2 = datetime(2024, 2, 22, 12, 0, 0)
difference_seconds = (date2 - date1).total_seconds()
print("Difference in seconds:", difference_seconds)