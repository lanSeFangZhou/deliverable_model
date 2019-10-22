class MetadataBuilder(object):
    version = "1.0"

    def __init__(self):
        self.id = None  # type: (str, str)
        self.dependency = []
        self.build = False

    def set_id(self, id_):
        self.id = id_

    def save(self):
        self.build = True

    def serialize(self, export_dir):
        return {"version": self.version, "id": self.id}

    def get_dependency(self):
        return self.dependency
