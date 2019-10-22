from deliverable_model.serving.model.model_loaders.model_loader_base import ModelLoaderBase

_model_reqistry = {}


def get_model_loader_class_by_type(model_type) -> ModelLoaderBase:
    model_loader_class = _model_reqistry[model_type]
    return model_loader_class


def get_model_loader_instance_by_type(model_type, model_path, metadata) -> ModelLoaderBase:
    model_loader_class = get_model_loader_class_by_type(model_type)
    model_loader_instance = getattr(model_loader_class, 'load')(model_path, metadata)

    return model_loader_instance


def register_model_loader(model_type, model_loader_class: ModelLoaderBase):
    if model_loader_class in _model_reqistry:
        raise ValueError()
    _model_reqistry[model_loader_class] = model_type
