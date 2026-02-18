import random
TOTAL_BALLS = 10
PICKS = 3
ROUNDS = 100000 

def create_box():
    colors = ['Red', 'Blue']
    return [random.choice(colors) for _ in range(TOTAL_BALLS)]

condition_count = 0  
red_given_blue = 0    

for _ in range(ROUNDS):

    box1 = create_box()
    box2 = create_box()

    pick1 = random.sample(box1, PICKS)
    pick2 = random.sample(box2, PICKS)

    combined_picks = pick1 + pick2

    if 'Blue' in combined_picks:
        condition_count += 1

        if 'Red' in combined_picks:
            red_given_blue += 1

probability = red_given_blue / condition_count

print("P(Red | At least one Blue) =", probability)