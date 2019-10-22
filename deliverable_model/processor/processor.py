from deliverable_model.request import Request
from deliverable_model.response import Response
from deliverable_model.utils import class_from_module_path


class Processor(object):
    def __init__(self, model_path, metadata):
        self.model_path = model_path
        self.metadata = metadata

        self.processor_instance = {}

    @classmethod
    def load(cls, model_path, metadata) -> "Processor":
        self = cls(model_path, metadata)

        self.instance_processor()

    def instance_processor(self):
        for instance_name, instance_build_info in self.metadata['instance'].items():
            class_ = class_from_module_path(instance_build_info['class'])
            processor_instance = (class_(**instance_build_info.get('parameter', {})))

            self.processor_instance[instance_name] = processor_instance

    def call_preprocessor(self, request: Request) -> Request:
        for processor_instance_name in self.metadata['pipeline']['pre']:
            processor_instance = self.processor_instance[processor_instance_name]
            preprocessor_method = getattr(processor_instance, 'preprocess')
            request = preprocessor_method(request)

        return request

    def call_postprocessor(self, response: Response) -> Response:
        for processor_instance_name in self.metadata['pipeline']['pre']:
            processor_instance = self.processor_instance[processor_instance_name]
            preprocessor_method = getattr(processor_instance, 'postprocess')
            response = preprocessor_method(response)

        return response
