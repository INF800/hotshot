from hotshot.file import utils as futils
from hotshot.xp import Predict

# path to all train experiments config file
INFERENCE_EXPERIMENTS_JSON_PATH = ""

predictor = Predict(
    all_experiments=futils.read_json(TRAIN_EXPERIMENTS_JSON_PATH))

predictor.run_all_experiments()