from hotshot.xp import utils as xputils
from hotshot.xp import Predict

# path to all train experiments config file
INFERENCE_EXPERIMENTS_JSON_PATH = ""

predictor = Predict(
    all_experiments=xputils.read_json(TRAIN_EXPERIMENTS_JSON_PATH))

predictor.run_all_experiments()