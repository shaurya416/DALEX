import numpy as np
from .._model_performance.utils import auc, r2


def loss_root_mean_square(observed, predicted):
    return np.sqrt(((observed - predicted) ** 2).mean())


def loss_one_minus_auc(observed, predicted):
    return 1 - auc(y_true=observed, y_pred=predicted)


def loss_r2(observed, predicted):
    # r2 takes (y_pred, y_true), while loss functions take (observed, predicted)
    return r2(y_pred=predicted, y_true=observed)
