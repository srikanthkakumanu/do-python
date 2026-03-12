import pendulum

# 1. Basic Date/Time Creation
print("=== Basic Date/Time Creation ===")

# Current date/time in UTC
now = pendulum.now()
print(f"Current UTC time: {now}")

# Current date/time in local timezone
now_local = pendulum.now('local')
print(f"Current local time: {now_local}")

# Create specific date/time
dt = pendulum.datetime(2024, 3, 13, 10, 30, 0)
print(f"Specific datetime: {dt}")

# Create date only
date = pendulum.date(2024, 3, 13)
print(f"Date only: {date}")

# Create time only
time = pendulum.time(14, 30, 45)
print(f"Time only: {time}")

print()

# 2. Parsing Date/Time Strings
print("=== Parsing Date/Time Strings ===")

# Parse ISO format
parsed_iso = pendulum.parse('2024-03-13T14:30:45+00:00')
print(f"Parsed ISO: {parsed_iso}")

# Parse common formats
parsed_ymd = pendulum.parse('2024-03-13')
print(f"Parsed YYYY-MM-DD: {parsed_ymd}")

parsed_human = pendulum.parse('2024/03/13 14:30:45')
print(f"Parsed YYYY/MM/DD HH:mm:ss: {parsed_human}")

print()

# 3. Date/Time Arithmetic
print("=== Date/Time Arithmetic ===")

dt = pendulum.datetime(2024, 3, 13, 10, 0, 0)

# Add time
future = dt.add(hours=2, minutes=30)
print(f"Add 2h 30m: {future}")

# Subtract time
past = dt.subtract(days=1, hours=5)
print(f"Subtract 1d 5h: {past}")

# Add weeks
week_later = dt.add(weeks=1)
print(f"Add 1 week: {week_later}")

print()

# 4. Timezone Handling
print("=== Timezone Handling ===")

# Create UTC datetime
utc_dt = pendulum.datetime(2024, 3, 13, 12, 0, 0, tz='UTC')
print(f"UTC time: {utc_dt}")

# Convert to different timezone
ny_dt = utc_dt.in_timezone('America/New_York')
print(f"New York time: {ny_dt}")

tokyo_dt = utc_dt.in_timezone('Asia/Tokyo')
print(f"Tokyo time: {tokyo_dt}")

# Set timezone (changes interpretation)
dt_naive = pendulum.datetime(2024, 3, 13, 12, 0, 0)
dt_eastern = dt_naive.set(tz='US/Eastern')
print(f"Set to Eastern: {dt_eastern}")

print()

# 5. Formatting
print("=== Formatting ===")

dt = pendulum.datetime(2024, 3, 13, 14, 30, 45, tz='UTC')

# ISO format
print(f"ISO format: {dt.to_iso8601_string()}")

# Custom format
print(f"Custom format: {dt.format('dddd, MMMM Do YYYY, h:mm:ss a')}")

# Date only format
print(f"Date format: {dt.format('YYYY-MM-DD')}")

# Time only format
print(f"Time format: {dt.format('HH:mm:ss')}")

print()

# 6. Durations and Periods
print("=== Durations and Periods ===")

# Duration (time span)
duration = pendulum.duration(hours=2, minutes=30)
print(f"Duration: {duration}")

# Calculate difference
start = pendulum.datetime(2024, 3, 13, 10, 0, 0)
end = pendulum.datetime(2024, 3, 13, 12, 45, 0)
diff = end - start
print(f"Time difference: {diff}")
print(f"Time difference in hours: {diff.total_hours()}")

# Working with intervals
interval = pendulum.duration(hours=1, minutes=30)
future_interval = start + interval
print(f"Start + 1.5h interval: {future_interval}")

# Check if datetime is within range
check_dt = pendulum.datetime(2024, 3, 13, 11, 0, 0)
is_within = start <= check_dt <= end
print(f"Is {check_dt} between start and end? {is_within}")

print()

# 7. Common Operations
print("=== Common Operations ===")

dt = pendulum.datetime(2024, 3, 13, 14, 30, 45)

# Get components
print(f"Year: {dt.year}, Month: {dt.month}, Day: {dt.day}")
print(f"Hour: {dt.hour}, Minute: {dt.minute}, Second: {dt.second}")

# Day of week (0=Monday, 6=Sunday)
print(f"Day of week: {dt.day_of_week} ({dt.format('dddd')})")

# Day of year
print(f"Day of year: {dt.day_of_year}")

# Is leap year?
print(f"Is leap year? {dt.is_leap_year()}")

# Start/end of period
print(f"Start of day: {dt.start_of('day')}")
print(f"End of month: {dt.end_of('month')}")
print(f"Start of week: {dt.start_of('week')}")

print()

# 8. Comparisons
print("=== Comparisons ===")

dt1 = pendulum.datetime(2024, 3, 13, 10, 0, 0)
dt2 = pendulum.datetime(2024, 3, 13, 12, 0, 0)
dt3 = pendulum.datetime(2024, 3, 14, 10, 0, 0)

print(f"dt1 < dt2: {dt1 < dt2}")
print(f"dt2 == dt3: {dt2 == dt3}")
print(f"dt2 is between dt1 and dt3: {dt1 <= dt2 <= dt3}")

# Age calculation
birth_date = pendulum.datetime(1990, 5, 15, 10, 12, 45 )
age = now.diff(birth_date).in_years()
print(f"Age: {age} years")