from datetime import datetime

# ===============================
# UTILITIES
# ===============================
def time_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def minutes_to_time(m):
    h = m // 60
    m = m % 60
    return f"{h:02d}:{m:02d}"

def days_left(exam_date):
    exam = datetime.strptime(exam_date, "%Y-%m-%d")
    return max((exam - datetime.now()).days, 1)

# ===============================
# AVAILABLE TIME CALCULATION
# ===============================
def calculate_available_time(r):
    awake = time_to_minutes(r["sleep"]) - time_to_minutes(r["wake"])
    school = time_to_minutes(r["school_end"]) - time_to_minutes(r["school_start"])
    tuition = time_to_minutes(r["tuition_end"]) - time_to_minutes(r["tuition_start"])
    used = school + tuition + r["meals"] + r["travel"] + r["breaks"]
    return max(awake - used, 0)

# ===============================
# AI SCHEDULE GENERATOR
# ===============================
def generate_schedule(subjects, available):
    plan = []
    start_time = time_to_minutes("16:00")
    max_block = 60

    for s in subjects:
        allocated = min(120, int(available / len(subjects)))
        end = start_time + allocated
        plan.append(f"{minutes_to_time(start_time)} - {minutes_to_time(end)} → {s}")
        start_time = end + 10

    return plan
