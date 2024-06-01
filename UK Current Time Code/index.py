import pytz
from datetime import datetime

# UK timezone set karna
uk_timezone = pytz.timezone('Europe/London')

# Current time fetch karna aur UK timezone mein convert karna
uk_time = datetime.now(uk_timezone)

# UK ka current time print karna
print("UK ka current time hai:", uk_time.strftime('%Y-%m-%d %H:%M:%S'))
