def main():
    user = input("what time is it?").strip()
    b=convert(user)
    print("so it is", b ,"hours")

    if 7.0 <= b <= 8.0:
        print("Breakfast time")
    elif 12.0 <= b <= 13.0:
        print("Lunch time")
    elif 18.0 <= b <= 19.0:
        print("Dinner time")

def convert(time):
    h,m=time.split(":")
    m=float(m)
    m=m/60
    h=float(h)
    return h + m
# orrr
# """Convert time from HH:MM format to a float (hours)."""
#     hours, minutes = map(int, time.split(":"))
#     return hours + (minutes / 60)  # Convert minutes to fraction of an hour
# map() to convert the string components of time into integers.


if __name__ == "__main__":
    main()
