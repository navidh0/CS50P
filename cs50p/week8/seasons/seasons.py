from datetime import datetime,date
from sys import exit
import inflect


class Birth:
    def __init__(self,birthday):
        try:
            self.birthday = datetime.strptime(birthday, "%Y-%m-%d")
        except ValueError:
            exit("Invalid date")

    def cal(self):
        today = datetime.combine(date.today(), datetime.min.time())
        minutes = (today - self.birthday).days * 24 * 60
        p = inflect.engine()
        return f"{p.number_to_words(int(minutes), andword='').capitalize()} {p.plural('minute', int(minutes))}"


def main():
    date_of_birth = Birth(input("Date of Birth: "))
    print(date_of_birth.cal())

if __name__ == "__main__":
    main()
