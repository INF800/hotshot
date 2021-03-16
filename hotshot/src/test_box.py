import json
from box import Box

with open('config.json', 'r') as fp:
    cfg = json.load(fp)
    print(cfg)
    print(Box(cfg))
    print(Box(cfg).Experiment.Name)