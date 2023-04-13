import random

# Define the rewards and their respective probabilities
reward_probabilities = {
    'Better luck next time! :(\nGo read, play the guitar, or enjoy with family! :)': 0.20,
    'Coding': 0.35*0.80,
    'Web Browsing / YouTube / Social Media': 0.25*0.80,
    'League of Legends': 0.20*0.80
}

# Define a function to generate the rewards based on their probabilities
rewards = [i for i in reward_probabilities.keys()]
probabilities = [i for i in reward_probabilities.values()]

# print(rewards, probabilities)


def generate_reward():
    return random.choices(rewards, probabilities)[0]


print(generate_reward())
input()
