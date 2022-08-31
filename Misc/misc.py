
class Ranking:
    def __init__(self, words):
        self.rank = None
        self.words = words

    def ranks(self):
        self.rank = []
        rank_list = list(set(self.words))
        rank_list.sort(key = lambda x:self.words.count(x))
        rank_list.reverse()
        for index, word in enumerate(rank_list):
            self.rank.append((word, index + 1))

    def display(self):
        print(self.rank)


# question 1
class Student:
    def __init__(self, name, roll, ph_number):
        self.name = name
        self.roll = roll
        self.ph = ph_number

    def display(self):
        print(f"Name   :  {self.name}")
        print(f"Roll No:  {self.roll}")
        print(f"Ph no. :  {self.ph}")

sam = Student("Sam", "12195", "1245788948")
john = Student("John", "12810", "2659314870")
sam.display()
john.display()

# question 2
class SalarySort:
    def __init__(self, salaries):
        self.salaries = salaries

    def sort(self):
        return sorted(self.salaries)

def hyphen_sort(x):
    return "-".join(sorted(x.split("-")))

print(hyphen_sort("green-red-yellow-black-white"))
