from hotshot.xp import Predict

SAVED_MODEL_PATH = ...
SAVE_ALL_PRED_IMGS_PATH = None
INFERENCE_CONFIG = dict(
    thresh=0.5,
    margin=1.,
    save_preds=SAVE_ALL_PRED_IMGS_PATH
)


predictor = Predict(
    model_path=SAVED_MODEL_PATH
)


predictor.predict(
    im_or_im_path=...
    config=INFERENCE_CONFIG
)