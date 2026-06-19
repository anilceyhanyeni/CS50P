def main():
    time = input("Enter time in #:## or ##:## format : ")
    convert(time)

def convert(time):
    time = time.split(":")
    real_time = int(time[0]) * 60 + int(time[1])
    dec_time = float(time[0]) + float(time[1]) / 60
    print(dec_time)
    if (7*60 <= real_time <= 8*60):
        print("Breakfast Time")
    elif (12*60 <= real_time <= 13*60):
        print("Lunch Time")
    elif (18*60 <= real_time <= 19*60):
        print("Dinner Time")
    else:
        return None
    
    

if __name__ == "__main__":
    main()