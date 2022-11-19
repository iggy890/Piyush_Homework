# Self service checkout.
"""
shopping_tax = 0.055
subtotal = 0

print("Press 0 when you want to checkout")

def get_items():
    global subtotal

    while True:
        quantity = int(input("Please enter quantity (3 maximum): "))

        if quantity == 0:
            return

        price = float(input("Please enter the price: "))

        subtotal += price * quantity

get_items()

total = subtotal + (subtotal / shopping_tax)
print(f"Subtotal: £ {subtotal} Shopping Tax: £ {total - subtotal}")
print(f"Please pay: £ {total}")

# Calculate Pi


# Initialize denominator
k = 1
 
# Initialize sum
s = 0
 
for i in range(10000000):
    if i % 2 == 0:
        s += 4/k
    else:
        s -= 4/k
 
    # denominator is odd
    k += 2
     
print(s)

def get_pi(precision: int):
    num = 4
    for i in range(2, (precision * 2) + 1, 2):
        num *= (i * (i + 2)) / ((i + 1) * (i + 1))
    return num

print(get_pi(10))
"""

def ampm(mtime: str):
    t = mtime
    int_mtime = int(mtime)

    if int_mtime >= 1200:
        return t[0]+t[1]+":"+t[2]+t[3]+"PM"
    elif int_mtime < 1200:
        return t[0]+t[1]+":"+t[2]+t[3]+"PM"
    elif int_mtime == 0:
        return "12:00AM"

def valid_military_time(mtime):
    if int(mtime) > 0 and int(mtime) < 2400 and len(mtime) == 4 and not int(mtime[2]) >= 6:
        return True

    print(" (!) Invalid military time")
    raise SystemExit()

def minutes_elapsed(mtstart, mtend):
    hrs_start = mtstart[:2]
    hrs_end = mtend[:2]
    hrs_diff = int(hrs_end) - int(hrs_start)
    minutes = (hrs_diff * 60) + (int(mtend[2:]) - int(mtstart[2:]))
    return minutes

def get_daily_salary():
    job_role = input("What role do you have: ")

    start_time = input("Start time: ")
    end_time = input("End time: ")

    valid_military_time(start_time)
    valid_military_time(end_time)

    time = minutes_elapsed(start_time, end_time) / 60
    print(time)
    print(" -------------------------- ")
    print("        Daily Salary")
    if job_role == "M":
        print(f"    Type of employee: Managerial")
        print(f"      Start Time: {ampm(start_time)}")
        print(f"      End Time: {ampm(end_time)}")

        print(f"Total time worked: {time * 60} minutes")

        if time > 10:
            print(f"You will recieve: ${(time * 30) * 1.25}")
        if time == 10:
            print(f"You will receive: ${time * 30}")
        if time < 10:
            print(f"You will receive: ${(time * 30) * 0.8}")

    if job_role == "T":
        print(f"    Type of employee: Technical")
        print(f"      Start Time: {ampm(start_time)}")
        print(f"      End Time: {ampm(end_time)}")

        print(f"Total time worked: {time * 60} minutes")
        if time > 8:
            print(f"You will receive: ${(time * 25) * 1.25}")
        if time == 8:
            print(f"You will receive: ${time * 25}")
        if time < 8:
            print(f"You will receive: ${(time * 25) * 0.8}")

    if job_role == "J":
        print(f"    Type of employee: Janitor")
        print(f"      Start Time: {ampm(start_time)}")
        print(f"      End Time: {ampm(end_time)}")

        print(f"Total time worked: {time * 60} minutes")
        if time > 7:
            print(f"You will receive: ${(time * 10) * 1.25}")
        if time == 8:
            print(f"You will receive: ${time * 10}")
        if time < 8:
            print(f"You will receive: ${(time * 10) * 0.8}")

get_daily_salary()
