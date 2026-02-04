students = {"Karthik": 1,
            "Bhavish": 2,
            "Adithya": 3}
print("Students List: ",students)

#Example 1

student = {
    "name": "Karthik",
    "age": 24,
    "course": "Engineering"
    }

print(student["name"])

student["age"] = 24
student["city"] = "Delhi"

print(student)

#Example 2

marks = {"math": 80, "science": 75, "english": 85}

print(marks.get("math"))
print(marks.get("history"))

for subject, score in marks.items():
    print(subject, score)
marks.update({"History": 90})
print("After Updated: ",marks)
marks.pop("science")
print("After Popping: ",marks)

#Example 3

purchases = {"Alice":250,"Bob":400,"Charlie":150}
for name,amount in purchases.items():
    print(f"{name} made a purchase of {amount}")
print("Total customers:", len(purchases))
print("Custoomers name : ",purchases.keys())

print("Alice's purchases amount:", purchases.get("Alice",0))

#Example 4

n = int(input("Enter number of customers: "))
user_purchases = {}

for i in range(n):
    name = input(f"Enter name of customer {i+1}: ")
    amount = float(input(f"Enter purchase amount for {name}: "))
    user_purchases[name] = amount
print("Customer Purchases: ",user_purchases)

#Example 5

top_customers = max(user_purchases, key=user_purchases.get)
print("Top Customers: ",top_customers)

#Example 6

a = {1,2,3}
b = {3,4,5}
print("Union: ",a | b)
print("Intersection: ",a & b)
print(3 in a)