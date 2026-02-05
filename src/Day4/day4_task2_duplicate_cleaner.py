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