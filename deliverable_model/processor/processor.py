from deliverable_model.request import Request
from deliverable_model.response import Response


class Processor(object):
    def __init__(self, model_path, metadata):
        pass

    @classmethod
    def load(cls, model_path, metadata) -> "Processor":
        pass

    def call_preprocessor(self, request: Request) -> Request:
        pass

    def call_postprocessor(self, response: Response) -> Response:
        pass
