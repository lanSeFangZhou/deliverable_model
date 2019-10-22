import shutil
from collections import namedtuple
from pathlib import Path

ModelInfo = namedtuple("ModelInfo", ["type", "store_dir"])


class ModelBuilder(object):
    version = "1.0"

    def __init__(self):
        self.model = None  # type: ModelInfo
        self.dependency = []

    def add_keras_h5_model(self, model_dir):
        if self.model:
            raise ValueError()

        self.model = ModelInfo("keras_h5_model", model_dir)

    def add_tensorflow_saved_model(self, model_dir):
        if self.model:
            raise ValueError()

        self.model = ModelInfo("tensorflow_saved_model", model_dir)

    def add_keras_saved_model(self, model_dir):
        if self.model:
            raise ValueError()

        self.model = ModelInfo("keras_saved_model", model_dir)

    def save(self):
        self.build = True

    def serialize(self, asset_dir: Path):
        output_dir = asset_dir / self.model.type

        shutil.copytree(self.model.store_dir, output_dir)

        return {"version": self.version, "type": self.model[0]}

    def get_dependency(self):
        return self.dependency

    def set_dependency(self, dependency):
        self.dependency = dependency
