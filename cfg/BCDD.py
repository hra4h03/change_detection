import os

BASE_PATH = os.getcwd()
PRETRAIN_MODEL_PATH = os.path.join(BASE_PATH, 'pretrain')
DATA_PATH = os.path.join(BASE_PATH, 'data')
TRAIN_DATA_PATH = os.path.join(DATA_PATH)
TRAIN_LABEL_PATH = os.path.join(DATA_PATH)
TRAIN_TXT_PATH = os.path.join(TRAIN_DATA_PATH, 'train.txt')
VAL_DATA_PATH = os.path.join(DATA_PATH)
VAL_LABEL_PATH = os.path.join(DATA_PATH)
VAL_TXT_PATH = os.path.join(VAL_DATA_PATH, 'val.txt')
SAVE_PATH = os.path.join(BASE_PATH, 'save')
SAVE_CKPT_PATH = os.path.join(SAVE_PATH, 'ckpt')
if not os.path.exists(SAVE_CKPT_PATH):
    os.mkdir(SAVE_CKPT_PATH)
SAVE_PRED_PATH = os.path.join(SAVE_PATH, 'prediction')
if not os.path.exists(SAVE_PRED_PATH):
    os.mkdir(SAVE_PRED_PATH)
TRAINED_BEST_PERFORMANCE_CKPT = os.path.join(
    SAVE_CKPT_PATH, 'bcd_model_best.pth')
INIT_LEARNING_RATE = 1e-4
DECAY = 5e-5
MOMENTUM = 0.90
MAX_ITER = 40000
BATCH_SIZE = 1
TRANSFROM_SCALES = (256, 256)
T0_MEAN_VALUE = (98.62, 113.27, 123.59)
T1_MEAN_VALUE = (117.38, 123.09, 123.20)
