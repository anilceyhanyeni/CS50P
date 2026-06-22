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
        date = input("Enter Date:").strip()
        if "/" in date:
            month, day, year = date.split("/")
            if not month.isdigit():
                continue

        elif "," in date:
            parts = date.split()
            if len(parts) != 3:
                continue

            month, day, year = parts[0], parts[1], parts[2]

            if month in months: # if "month day, year" format
                month = months.index(month) + 1
            else:
                continue

            if not day.endswith(","):
                continue
            day = day.replace(",", "")

        else:
            continue

        month, day, year = int(month), int(day), int(year)
        if not (1 <= int(month) <= 12 and 1 <= int(day) <= 31 and 0 <= int(year) <= 9999): #check correctness in date
            raise ValueError

    except (ValueError, IndexError):
        continue
    except EOFError:
        break
    else:  
        print(f"{year:04}-{month:02}-{day:02}")
        break


