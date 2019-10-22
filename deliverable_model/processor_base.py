from deliverable_model.request import Request
from deliverable_model.response import Response


class ProcessorBase(object):
    def get_config(self):
        return {}

    def preprocess(self, request: Request) -> Request:
        raise NotImplementedError

    def postprocess(self, response: Response) -> Response:
        raise NotImplementedError

    def get_dependency(self) -> list:
        return []
