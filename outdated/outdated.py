import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Enter Date:")
        if "/" in date:
            month, day, year = date.split("/")
        else:
            month, day, year = re.split(r"/| ,| ", date)
            day = day.replace(",", "")
        
        if month in months: # if "month day, year" format
            month = months.index(month) + 1

        month, day, year = int(month), int(day), int(year)
        if not (1 <= int(month) <= 12 and 1 <= int(day) <= 31 and 0 <= int(year) <= 9999): #check correctness in date
            raise ValueError

    except ValueError:
        print("Enter correct date")
    except EOFError:
        print("User stopped inputing")
    else:  
        print(f"{year:04}-{month:02}-{day:02}")
        break


