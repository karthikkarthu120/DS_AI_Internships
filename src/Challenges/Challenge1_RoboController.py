import random
import time

# ===================== USER INPUTS =====================
robot_name = input("Enter the robot's name: ")
distance_km = float(input("Enter distance to target (in kilometers): "))

# ===================== INITIAL SETUP =====================
travelled_distance = 0
checkpoints = ["Start Point"]

# To store full details of each step
journey_log = []

print("\n====================================")
print(f"   🤖 ROBOCONTROLLER 1.0 - {robot_name.upper()}")
print("====================================\n")

print(f"📏 Target Distance: {distance_km} km")
print("🚀 Robot starting journey...\n")

# ===================== JOURNEY WITH RANDOM OBSTACLES =====================
num_checks = random.randint(3, 5)   # 3 to 5 random obstacle checks
print(f"🔄 Performing {num_checks} random obstacle checks on the way...\n")

directions = ["Left", "Right", "Forward", "Backward", "Rotate"]

# Keep track of last two obstacles to avoid 3 repeats
last_obstacle = None
second_last_obstacle = None

for step in range(1, num_checks + 1):

    time.sleep(0.7)

    # Move a portion of the total distance
    travelled_distance += distance_km / num_checks

    # -------- SMART OBSTACLE SELECTION (NO 3 REPEATS) --------
    possible_obstacles = ["none", "wall", "object", "human"]

    while True:
        obstacle_type = random.choice(possible_obstacles)

        # Allow obstacle only if it is NOT same as last two
        if not (obstacle_type == last_obstacle == second_last_obstacle):
            break

    # Update history
    second_last_obstacle = last_obstacle
    last_obstacle = obstacle_type

    print(f"Step {step}: Detected obstacle → {obstacle_type}")

    # -------- Decision making for this obstacle --------
    if obstacle_type == "wall":
        speed = 2
        movement = "Changing direction (wall ahead)"
        unexpected_direction = random.choice(directions)
        print(f"   ➜ Speed: {speed} | Direction Adjusted: {unexpected_direction}")

    elif obstacle_type == "object":
        speed = 3
        movement = "Avoiding object and adjusting path"
        unexpected_direction = random.choice(directions)
        print(f"   ➜ Speed: {speed} | Direction Adjusted: {unexpected_direction}")

    elif obstacle_type == "human":
        speed = 0
        movement = "STOPPED – Human detected"
        print("\n🛑 HUMAN DETECTED AHEAD!")
        print("⏳ Robot is waiting for 5 seconds...")
        time.sleep(5)
        print("🔴 Robot resumed slowly after safety wait.\n")
        speed = 1   # resume slowly
        unexpected_direction = "Stopped then resumed"

    else:  # no obstacle
        if distance_km > 1:
            speed = 8
            movement = "Fast movement"
        else:
            speed = 5
            movement = "Moderate movement"
        unexpected_direction = "No change"
        print(f"   ➜ Speed: {speed} | No obstacle")

    # Save checkpoint
    checkpoint_name = f"Checkpoint {step}"
    checkpoints.append(checkpoint_name)

    # Store full details of this checkpoint
    journey_log.append({
        "Checkpoint": checkpoint_name,
        "Obstacle": obstacle_type,
        "Speed": speed,
        "Movement": movement,
        "Direction": unexpected_direction,
        "Distance Covered (km)": round(travelled_distance, 3)
    })

    progress = "█" * step + "-" * (num_checks - step)
    print(f"   [{progress}] Reached {checkpoint_name}\n")

# ===================== RANDOM CHECKPOINT REMOVAL =====================
if len(checkpoints) > 2:
    removed_checkpoint = random.choice(checkpoints[1:-1])
    checkpoints.remove(removed_checkpoint)
else:
    removed_checkpoint = "None"

checkpoints.append("Final Point")

# ===================== FINAL OBSTACLE STATUS (last one detected) =====================
if obstacle_type == "wall":
    obstacle_status = "⚠️ Wall detected — direction changed"
elif obstacle_type == "human":
    obstacle_status = "🛑 Human detected — safety wait applied"
elif obstacle_type == "object":
    obstacle_status = "🔁 Object detected — path adjusted"
else:
    obstacle_status = "🟢 No obstacle encountered"

# ===================== FINAL TRIP SUMMARY =====================
print("\n====================================")
print("        📍 FINAL TRIP SUMMARY")
print("====================================")
print(f"🤖 Robot Name           : {robot_name}")
print(f"📏 Total Distance       : {round(travelled_distance, 3)} km")
print(f"🚧 Last Obstacle Status : {obstacle_status}")
print(f"⚡ Last Recorded Speed  : {speed} units")
print(f"🧭 Last Movement Type   : {movement}")
print(f"❌ Removed Checkpoint   : {removed_checkpoint}")
print(f"🗺️  Final Checkpoints   : {checkpoints}")
print("====================================\n")

# ===================== DETAILED CHECKPOINT REPORT =====================
print("📍 DETAILED CHECKPOINT REPORT")
print("---------------------------------------------------------------")
print(f"{'Checkpoint':<15} | {'Obstacle':<10} | {'Speed':<5} | {'Direction':<18} | {'Distance (km)':<10}")
print("---------------------------------------------------------------")

for entry in journey_log:
    print(f"{entry['Checkpoint']:<15} | "
          f"{entry['Obstacle']:<10} | "
          f"{entry['Speed']:<5} | "
          f"{entry['Direction']:<18} | "
          f"{entry['Distance Covered (km)']:<10}")

print("---------------------------------------------------------------\n")
print("🎯 Journey Completed. Robot Stopped.")
