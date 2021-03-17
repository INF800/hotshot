from hotshot.file import utils as futils
from hotshot.xp import Train

# path to all train experiments config file
TRAIN_EXPERIMENTS_JSON_PATH = ""

trainer = Trainer(
    all_experiments=futils.read_json(TRAIN_EXPERIMENTS_JSON_PATH))

trainer.run_all_experiments()