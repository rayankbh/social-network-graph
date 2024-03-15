import json
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# ----------------------
# Data Loading
# ----------------------

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

data = {
    'dontFollowMeBack': load_json('dontFollowMeBack.json'),
    'iDontFollowBack': load_json('iDontFollowBack.json'),
    'imFollowing': load_json('imFollowing.json'),
    'myFollowers': load_json('myFollowers.json')
}


# ----------------------
# Category Colors
# ----------------------

# colors and categories can be changed as needed
category_colors = {
    "Middle School": '#b04853',
    "High School": '#5890d1',
    "College 1": '#82b250',
    "College 2": '#870309',
    "Extra-Curricular": '#e4b7c6',
    "Celebrities": '#008897',
    "Interests": '#87d6b6',
    "Random Interactions": '#6b8af3',
    "Misc": '#d3cc31',
    "Me": '#7b98bd'
}

# ----------------------
# Manual Categorization
# ----------------------
user_categories = {}

def categorize_user(user, is_me=False):
    if is_me:
        return "Me"
    while True:
        print(f"\nUser: {user}")
        print("Select a category:")
        for i, (category, color) in enumerate(category_colors.items()):
            print(f"{i + 1}. {category}")
        choice = input("Enter your choice (1-{}): ".format(len(category_colors)))
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(category_colors):
                return list(category_colors.keys())[choice_index]  # Return category name 
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        user_categories[user] = category
        return category 

