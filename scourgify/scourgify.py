import sys
import csv

def main():
    scourgify()

def scourgify():
    if len(sys.argv) <3:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) >3:
        print("Too many command-line arguments")
        sys.exit(1)
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        print("not csv file")
        sys.exit(1)

    with open(sys.argv[1], newline="") as before_file, open (sys.argv[2], "w", newline = "") as after_file:
        reader = csv.DictReader(before_file)
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(after_file, fieldnames=fieldnames)

        for row in reader:
            split_name = row["name"].split(",")     #Last Name First Name split
            last = split_name[0].strip()
            first = split_name[1] = split_name[1].strip()    #First Name
            house = row["house"]
    
            writer.writerow({"first": first, "last" : last, "house": house})


if __name__  == "__main__":
    main()