import json
from box import Box
from pprint import pprint

with open('training_config.json', 'r') as fp:
    cfg = json.load(fp)
    print(cfg)
    pprint(Box(cfg))