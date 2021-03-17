from hotshot.xp import utils as xputils
from hotshot.xp import Train

# path to all train experiments config file
TRAIN_EXPERIMENTS_JSON_PATH = ""

trainer = Trainer(
    all_experiments=xputils.read_json(TRAIN_EXPERIMENTS_JSON_PATH))

trainer.run_all_experiments()