import json
from pathlib import Path

from deliverable_model.builder.metadata.metadata_builder import MetadataBuilder
from deliverable_model.builder.model.model_builder import ModelBuilder
from deliverable_model.builder.processor.processor_builder import ProcessorBuilder


class DeliverableModelBuilder(object):
    def __init__(self, export_dir):
        self.export_dir = Path(export_dir)

        self.processor_builder = None  # type: ProcessorBuilder
        self.model_builder = None
        self.metadata_builder = None

    def add_metadata(self, metadata_builder: MetadataBuilder):
        self.metadata_builder = metadata_builder

    def add_processor(self, processor_builder: ProcessorBuilder):
        self.processor_builder = processor_builder

    def add_model(self, model_builder: ModelBuilder):
        self.model_builder = model_builder

    def save(self):
        dependency = self.gather_dependency()

        export_data = {
            "dependency": dependency,
            "processor": self.processor_builder.serialize(self.export_dir),
            "model": self.model_builder.serialize(self.export_dir),
            "metadata": self.metadata_builder.serialize(self.export_dir),
        }

        metadata_file = self.export_dir / "metadata.json"

        with metadata_file.open('wt') as fd:
            json.dump(export_data, fd)

    def gather_dependency(self) -> list:
        pass
