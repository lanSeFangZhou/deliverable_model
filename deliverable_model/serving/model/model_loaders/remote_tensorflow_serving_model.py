import functools
import os
from pathlib import Path
from typing import Dict

import grpc
import tensorflow as tf
import numpy as np
import rfc3986

from deliverable_model.serving.model.model_loaders.model_loader_base import (
    ModelLoaderBase,
)

from tensorflow_serving.apis import prediction_service_pb2_grpc
from tensorflow_serving.apis.predict_pb2 import PredictRequest


class RemoveTensorFlowServingModel(ModelLoaderBase):
    name = "remote_tensorflow_serving_model"

    @classmethod
    def _parse_uri(cls, tf_serving_uri_string):
        url = rfc3986.urlparse(tf_serving_uri_string)

        parts = url.userinfo.split(":")
        model_name = parts[0]
        signature = parts[1] if len(parts) == 2 else "serving_default"

        version = None
        if url.path:
            paths = Path(url.path).parts
            if len(paths):
                assert len(paths) == 1
            version = paths[0] if paths else None

        return {
            "server": url.hostname,
            "port": {url.scheme: str(url.port)},
            "model_name": model_name,
            "signature": signature,
            "version": version
        }

    @classmethod
    def load(cls, model_path: Path, metadata: dict):
        remote_tf_serving = cls._parse_uri(os.environ.get("REMOTE_TF_SERVING"))

        target = ":".join(
            (remote_tf_serving["server"], remote_tf_serving["port"]["grpc"])
        )
        channel = grpc.insecure_channel(target)

        stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

        predictor_func = functools.partial(cls._parse, stub=stub, remote_tf_serving=remote_tf_serving)

        self = cls(predictor_func)

        return self

    @classmethod
    def _build_request(cls, inputs, remote_tf_serving):
        words, words_len = inputs["words"], inputs["words_len"]

        request = PredictRequest()
        request.model_spec.name = remote_tf_serving["model_name"]
        request.model_spec.signature_name = remote_tf_serving["signature"]
        request.inputs["words"].CopyFrom(tf.make_tensor_proto(words))
        request.inputs["words_len"].CopyFrom(tf.make_tensor_proto(words_len))

        return request

    @classmethod
    def _parse(cls, inputs, stub, remote_tf_serving) -> Dict[str, np.ndarray]:
        request = cls._build_request(inputs, remote_tf_serving)

        feature = stub.Predict(request, 5.0)

        # tags_tensor_proto = feature.outputs["tags"]
        # tags_numpy = tf.make_ndarray(tags_tensor_proto)
        # unicode_tags_numpy = np.vectorize(lambda x: x.decode())(tags_numpy)
        # tags = unicode_tags_numpy.tolist()
        # return tags

        # decode TensorProto to numpy
        decoded_value = {}
        for key in feature.outputs:
            tensor_proto = feature.outputs[key]
            numpy_tensor_proto = tf.make_ndarray(tensor_proto)

            decoded_value[key] = numpy_tensor_proto

        return decoded_value


if __name__ == "__main__":
    server_setting = RemoveTensorFlowServingModel._parse_uri("grpc://ner:signature@localhost:123/version")
    print("")
