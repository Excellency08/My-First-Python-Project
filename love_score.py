import random 

random_integer = random.randint(1, 10)
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1,100)
if love_score >= 50:
    print(f"Your Love Score is {love_score} and You have good Heart")
elif random_integer < love_score:
        print(f"Your Heart need repair")
else:
    print(f"Your Love Score is {love_score} you have bad heart")
