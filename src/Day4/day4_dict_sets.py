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

#Task 1

contacts = {"Adithya": 9765287657,
            "Karthik": 9876543210,
            "Bhavish": 9876543211}

contacts["Dilan"] = 9123456780

print("Updated Contact Book: ",contacts)

contacts["Adithya"] = 9826529806

print("Updated Contact Book of Adithya: ",contacts["Adithya"])

print("Lookup of Existing Contact: ",contacts.get("Karthik"))

print("Lookup of Missing Contact: ",contacts.get("Rajesh", "Contact not found"))

print("Final Contacts List:")
for contacts, number in contacts.items():
    
    print(f"{contacts}: {number}") 
    
#Task 2

raw_logs = ["ID01","ID02","ID01","ID05","ID02","ID08","ID01"]

unique_users = set(raw_logs)

is_id05_present = "ID05" in unique_users

original_count = len(raw_logs)
unique_count = len(unique_users)

print("Original Lisrt:", raw_logs)
print("Unique Users:", unique_users)
print("Is ID05 present:", is_id05_present)
print("Original Count:", original_count)
print("Unique Count:", unique_count)
print("Duplicates Removed:", original_count - unique_count)

#Task 3

friend_a = {"Python","Cooking","Hiking","Movies"}
friend_b = {"Hiking","Gaming","Photography","Python"}

shared_interests = friend_a & friend_b

all_interests = friend_a | friend_b

unique_to_a = friend_a - friend_b

print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Interests only Friend A has: ", unique_to_a)