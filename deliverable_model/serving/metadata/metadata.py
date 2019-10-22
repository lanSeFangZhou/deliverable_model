from deliverable_model.metacontent import MetaContent


class Metadata(object):
    def __init__(self, model_path, metadata):
        self.metadata = metadata

    @classmethod
    def load(cls, model_path, metadata) -> "Metadata":
        pass

    def get_meta_content(self) -> MetaContent:
        return MetaContent(self.metadata['id'])
