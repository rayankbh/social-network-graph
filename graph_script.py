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

