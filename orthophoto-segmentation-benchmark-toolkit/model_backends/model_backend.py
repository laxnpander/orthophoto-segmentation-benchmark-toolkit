from abc import ABC, abstractmethod
from tensorflow.keras import metrics

from metrics import CustomMeanIOU


class ModelBackend(ABC):

    def __init__(self):
        self.chip_size = 512
        self.metrics = [
                metrics.Precision(top_k=1, name='precision'),
                metrics.Recall(top_k=1, name='recall'),
                CustomMeanIOU(num_classes=6, name='mIOU'),
            ]

    def load(self, weights_file_path):
        model_backend = self.compile()
        model_backend.load_weights(weights_file_path)
        return model_backend

    @abstractmethod
    def compile(self):
        pass