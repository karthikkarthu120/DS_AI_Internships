import random
P_heads = 1 / 2  
P_six = 1 / 6

independent_probability = P_heads * P_six

print("----- Independent Event -----")
print("Probability of Heads AND rolling a 6:", independent_probability)
trials = 10000
success = 0

for _ in range(trials):

    bag = ['R'] * 5 + ['B'] * 5

    first_pick = random.choice(bag)
    bag.remove(first_pick)

    second_pick = random.choice(bag)

    if first_pick == 'R' and second_pick == 'R':
        success += 1

experimental_probability = success / trials

theoretical_probability = (5/10) * (4/9)

print("\n----- Dependent Event -----")
print("Total trials:", trials)
print("Both red occurred:", success)
print("Experimental Probability:", experimental_probability)
print("Theoretical Probability:", theoretical_probability)
