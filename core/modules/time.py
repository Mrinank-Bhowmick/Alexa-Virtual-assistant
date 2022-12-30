import datetime


def time(query):
    now = datetime.datetime.now()
    if "time" in query:
        result = f"The time is {now.hour}:{now.minute}"
    elif "date" in query:
        result = f"The date is {now.day}/{now.month}/{now.year}"
    elif "day" in query:
        result = f"The day is {now.strftime('%A')}"
    return result
