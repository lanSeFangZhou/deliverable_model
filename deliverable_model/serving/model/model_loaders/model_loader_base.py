from deliverable_model.request import Request
from deliverable_model.response import Response


class ModelLoaderBase(object):
    @classmethod
    def load(cls, model_path, metadata) -> "ModelLoaderBase":
        raise NotImplementedError

    def parse(self, request: Request) -> Response:
        raise NotImplementedError
