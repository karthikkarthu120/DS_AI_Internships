import random

# ---------- STEP 1: Taking User Inputs ----------
robot_name = input("Enter the robot's name: ")
distance = float(input("Enter distance to target (in meters): "))
obstacle = input("Is there an obstacle ahead? (yes/no): ").strip().lower()

# ---------- STEP 2: Decision Making using if-elif-else ----------
if obstacle == "yes":
    speed = 2
    movement = "Cautious movement"

    if distance > 50:
        movement = "Very slow and careful movement"

elif obstacle == "no":
    if distance > 100:
        speed = 8
        movement = "Fast movement"
    else:
        speed = 5
        movement = "Moderate movement"

else:
    speed = 0
    movement = "Invalid input – robot stopped"

# ---------- STEP 3: Creating Checkpoints List ----------
checkpoints = ["Start Point"]

# ---------- STEP 4: Adding Checkpoints ----------
checkpoints.append("Checkpoint A")
checkpoints.append("Checkpoint B")

# ---------- STEP 5: Random Unexpected Direction Change ----------
directions = ["North", "South", "East", "West"]
unexpected_direction = random.choice(directions)

# ---------- STEP 6: Removing a Checkpoint ----------
removed_checkpoint = checkpoints.pop(1)  # Removes "Checkpoint A"

# ---------- STEP 7: Adding Final Checkpoint ----------
checkpoints.append("Final Point")

# ---------- STEP 8: Display Trip Summary using f-strings ----------
print("\n--- TRIP SUMMARY ---")
print(f"Robot Name: {robot_name}")
print(f"Total Distance Travelled: {distance} meters")
print(f"Obstacle Ahead: {obstacle}")
print(f"Robot Speed: {speed} units")
print(f"Movement Type: {movement}")
print(f"Unexpected Direction Change: {unexpected_direction}")
print(f"Final Checkpoints List: {checkpoints}")
