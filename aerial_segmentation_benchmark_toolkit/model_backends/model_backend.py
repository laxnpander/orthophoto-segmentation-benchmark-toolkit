from abc import ABC, abstractmethod


class ModelBackend(ABC):

    def __init__(self):
        pass

    def load(self, weights_file_path):
        model_backend = self.compile()
        model_backend.load_weights(weights_file_path)
        return model_backend

    @abstractmethod
    def compile(self):
        pass
