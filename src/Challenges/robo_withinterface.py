import random
import time
import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- GLOBAL STATE ----------------
journey_log = []
checkpoints = []
travelled_distance = 0
last_obstacle = None
second_last_obstacle = None

# ---------------- ROBOT LOGIC ----------------
def start_robot():
    global journey_log, checkpoints, travelled_distance, last_obstacle, second_last_obstacle

    robot_name = name_entry.get().strip()
    if not robot_name:
        messagebox.showerror("Error", "Enter a robot name")
        return

    try:
        distance_km = float(distance_entry.get())
    except:
        messagebox.showerror("Error", "Enter a valid number for distance")
        return

    # Reset everything
    journey_log = []
    checkpoints = ["Start Point"]
    travelled_distance = 0
    last_obstacle = None
    second_last_obstacle = None

    output_box.delete("1.0", tk.END)

    # Header
    output_box.insert(tk.END, f"🤖 RoboController 1.0 - {robot_name}\n")
    output_box.insert(tk.END, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    output_box.insert(tk.END, f"📏 Target Distance: {distance_km} km\n")
    output_box.insert(tk.END, "🚀 Robot starting journey...\n\n")

    # Random number of checks
    num_checks = random.randint(3, 5)
    output_box.insert(tk.END, f"🔄 Performing {num_checks} random obstacle checks...\n\n")

    # ✅ CHANGE MADE HERE: REMOVED "Rotate"
    directions = ["Left", "Right", "Forward", "Backward"]
    possible_obstacles = ["none", "wall", "object", "human"]

    for step in range(1, num_checks + 1):
        window.update()
        time.sleep(0.7)

        travelled_distance += distance_km / num_checks

        # Smart obstacle selection (no 3 repeats)
        while True:
            obstacle_type = random.choice(possible_obstacles)
            if not (obstacle_type == last_obstacle == second_last_obstacle):
                break

        second_last_obstacle = last_obstacle
        last_obstacle = obstacle_type

        output_box.insert(tk.END, f"Step {step}: Detected obstacle → {obstacle_type}\n")

        # Decision making
        if obstacle_type == "wall":
            speed = 2
            movement = "Changing direction (wall ahead)"
            unexpected_direction = random.choice(directions)
            output_box.insert(tk.END, f"   ➜ Speed: {speed} | Direction: {unexpected_direction}\n")

        elif obstacle_type == "object":
            speed = 3
            movement = "Avoiding object and adjusting path"
            unexpected_direction = random.choice(directions)
            output_box.insert(tk.END, f"   ➜ Speed: {speed} | Direction: {unexpected_direction}\n")

        elif obstacle_type == "human":
            speed = 0
            movement = "STOPPED – Human detected"
            output_box.insert(tk.END, "\n🛑 HUMAN DETECTED AHEAD!\n")
            output_box.insert(tk.END, "⏳ Waiting 5 seconds...\n")
            window.update()
            time.sleep(5)
            output_box.insert(tk.END, "🔴 Resuming slowly...\n")
            speed = 1
            unexpected_direction = "Stopped then resumed"

        else:
            if distance_km > 1:
                speed = 8
                movement = "Fast movement"
            else:
                speed = 5
                movement = "Moderate movement"
            unexpected_direction = "No change"
            output_box.insert(tk.END, f"   ➜ Speed: {speed} | No obstacle\n")

        checkpoint_name = f"Checkpoint {step}"
        checkpoints.append(checkpoint_name)

        journey_log.append({
            "Checkpoint": checkpoint_name,
            "Obstacle": obstacle_type,
            "Speed": speed,
            "Movement": movement,
            "Direction": unexpected_direction,
            "Distance Covered (km)": round(travelled_distance, 3)
        })

        progress = "█" * step + "-" * (num_checks - step)
        output_box.insert(tk.END, f"   [{progress}] Reached {checkpoint_name}\n\n")
        output_box.see(tk.END)

    # Remove random checkpoint
    if len(checkpoints) > 2:
        removed_checkpoint = random.choice(checkpoints[1:-1])
        checkpoints.remove(removed_checkpoint)
    else:
        removed_checkpoint = "None"

    checkpoints.append("Final Point")

    # Final obstacle status (last one)
    if obstacle_type == "wall":
        obstacle_status = "Wall detected — direction changed"
    elif obstacle_type == "human":
        obstacle_status = "Human detected — safety wait applied"
    elif obstacle_type == "object":
        obstacle_status = "Object detected — path adjusted"
    else:
        obstacle_status = "No obstacle encountered"

    # ---- FINAL SUMMARY ----
    output_box.insert(tk.END, "\n📍 FINAL TRIP SUMMARY\n")
    output_box.insert(tk.END, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    output_box.insert(tk.END, f"Robot Name           : {robot_name}\n")
    output_box.insert(tk.END, f"Total Distance       : {round(travelled_distance,3)} km\n")
    output_box.insert(tk.END, f"Last Obstacle Status : {obstacle_status}\n")
    output_box.insert(tk.END, f"Last Speed           : {speed}\n")
    output_box.insert(tk.END, f"Last Movement        : {movement}\n")
    output_box.insert(tk.END, f"Removed Checkpoint   : {removed_checkpoint}\n")
    output_box.insert(tk.END, f"Final Checkpoints    : {checkpoints}\n\n")

    # ---- DETAILED CHECKPOINT REPORT ----
    output_box.insert(tk.END, "📍 DETAILED CHECKPOINT REPORT\n")
    output_box.insert(tk.END, "-----------------------------------------------\n")
    output_box.insert(tk.END, f"{'Checkpoint':<12} | {'Obstacle':<8} | {'Speed':<5} | {'Direction':<15} | {'Dist (km)':<8}\n")
    output_box.insert(tk.END, "-----------------------------------------------\n")

    for entry in journey_log:
        output_box.insert(
            tk.END,
            f"{entry['Checkpoint']:<12} | "
            f"{entry['Obstacle']:<8} | "
            f"{entry['Speed']:<5} | "
            f"{entry['Direction']:<15} | "
            f"{entry['Distance Covered (km)']:<8}\n"
        )

    output_box.insert(tk.END, "-----------------------------------------------\n")
    output_box.insert(tk.END, "🎯 Journey Completed. Robot Stopped.\n")

# ---------------- MODERN GUI DESIGN ----------------
window = tk.Tk()
window.title("RoboController 1.0")
window.geometry("800x600")
window.configure(bg="#0F172A")  # Dark modern background

title_label = tk.Label(
    window,
    text="🤖 RoboController 1.0",
    font=("Segoe UI", 18, "bold"),
    fg="white",
    bg="#0F172A",
)
title_label.pack(pady=10)

main_frame = tk.Frame(window, bg="#0F172A")
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Left Panel (Inputs)
left_frame = tk.Frame(main_frame, bg="#111827", bd=2, relief="ridge")
left_frame.pack(side="left", fill="y", padx=10, pady=5)

tk.Label(left_frame, text="Robot Name:", fg="white", bg="#111827").pack(pady=5)
name_entry = tk.Entry(left_frame, width=25)
name_entry.pack(pady=5)

tk.Label(left_frame, text="Distance (km):", fg="white", bg="#111827").pack(pady=5)
distance_entry = tk.Entry(left_frame, width=25)
distance_entry.pack(pady=5)

start_btn = tk.Button(left_frame, text="Start Robot", command=start_robot,
                      bg="#22C55E", fg="white", font=("Segoe UI", 10, "bold"))
start_btn.pack(pady=15)

# Right Panel (Output)
right_frame = tk.Frame(main_frame, bg="#020617", bd=2, relief="ridge")
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=5)

output_box = tk.Text(right_frame, height=25, width=80, bg="#020617", fg="#E5E7EB",
                     font=("Consolas", 10))
output_box.pack(padx=10, pady=10, fill="both", expand=True)

window.mainloop()