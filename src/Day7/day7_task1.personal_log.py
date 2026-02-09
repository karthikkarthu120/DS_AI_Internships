name = input("Enter your name: ")
Daily_Goal = input("Enter your daily goal: ")


with open("journal.txt", "a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Daily Goal: {Daily_Goal}\n")
    file.close()