import re
import sys

def main():
    print(convert(input("Hours:")))

def convert(s):
    try:
        match = re.search(r"([1][0-2]|[0-9]):?([0-5][0-9])? (AM|PM) to ([1][0-2]|[0-9]):?([0-5][0-9])? (AM|PM)",s) #search if the string matches our format
        if not (match):
            raise ValueError
    except ValueError:
        print("Value Error")
    else: # if the string matches the format do the below

        # fixing the hours
        start_hour = int(match.group(1))
        end_hour = int(match.group(4))

        if match.group(3) == "PM": # if 3rd group is pm, we need to add 12 hours to the hour
            start_hour = start_hour + 12
        if start_hour == 24 : 
            start_hour = 0
        if match.group(6) == "PM": # if 6th group is pm, we need to add 12 hours to the hour
            end_hour = end_hour + 12
        if end_hour == 24 : 
            end_hour = 0
        

        # fixing the minutes
        if match.group(2) == None:
            start_minutes = 0
        else:
            start_minutes = int(match.group(2))
        if match.group(5) == None:
            end_minutes = 0
        else:
            end_minutes = int(match.group(5))

        return f"{int(start_hour):02}:{start_minutes:02} to {int(end_hour):02}:{end_minutes:02}"


if __name__ == "__main__":
    main()