from typing import Callable

from deliverable_model.serving.model.model_loaders.model_loader_base import ModelLoaderBase
from deliverable_model.request import Request
from deliverable_model.response import Response

from tensorflow.contrib import predictor


class TensorFlowSavedModel(ModelLoaderBase):
    name = "tensorflow_saved_model"

    def __init__(self, predictor_func: Callable):
        self.predictor_func = predictor_func

    @classmethod
    def load(cls, model_path, metadata):
        predictor_func = predictor.from_saved_model(model_path)

        self = cls(predictor_func)

        return self

    def parse(self, request: Request) -> Response:
        # TODO: fix me
        return self.predictor_func(request.query)
