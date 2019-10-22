from pathlib import Path

from deliverable_model.serving.model.model_loaders.model_loader_base import ModelLoaderBase
from deliverable_model.serving.model.model_loaders.model_registry import get_model_loader_instance_by_type
from deliverable_model.request import Request
from deliverable_model.response import Response


class Model(object):
    def __init__(self, model_loader_instance: ModelLoaderBase):
        self.model_loader_instance = model_loader_instance

    @classmethod
    def load(cls, asset_dir: Path, metadata) -> "Model":
        model_type = metadata['type']
        model_loader_instance = get_model_loader_instance_by_type(model_type, asset_dir, metadata)

        self = cls(model_loader_instance)

        return self

    def parse(self, request: Request) -> Response:
        return self.model_loader_instance.parse(request)
