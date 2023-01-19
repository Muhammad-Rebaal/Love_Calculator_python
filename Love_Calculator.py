import random
print("              Welcome to the Love Calculator")
love_percent = random.randint(0, 100)
person_1 = input("Enter the name of the 1st_Person :")
person_2 = input("Enter the name of the 2nd_Person :")
def love (p1,p2):
    return f"The love percentage between {p1} and {p2} is {love_percent}%."

print(love(person_1,person_2))