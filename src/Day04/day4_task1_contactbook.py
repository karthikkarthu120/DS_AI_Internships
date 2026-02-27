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