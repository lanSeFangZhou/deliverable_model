from deliverable_model.request import Request
from deliverable_model.response import Response


class Model(object):
    def __init__(self, model_path, metadata):
        pass

    @classmethod
    def load(cls, model_path, metadata):
        pass

    def parse(self, request: Request) -> Response:
        pass
