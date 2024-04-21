def main():
    time = input("What time is it? ").strip()
    meal(convert(time))


def convert(t):
    hour, min = t.split(":")
    min = float(min)/60
    final_time = float(hour) + min
    return final_time

def meal(m):

    if 7 <= m <= 8 :
         print("breakfast time")
    elif 12 <= m <= 13 :
            print("lunch time")
    elif 18 <= m <= 19 :
         print("dinner time")

if __name__ == "__main__":
    main()
