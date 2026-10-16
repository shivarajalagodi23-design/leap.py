import sys

def is_leap(year):
    return (year % 4 ==0 and year % 100 != 0) or (year % 400 ==0)

if __name__ == "__main__":
    year = int(sys.argv[1])
    if is_leap(year):
        print(year, "is a leap year")
    else:
        print(year, "is not leap year")