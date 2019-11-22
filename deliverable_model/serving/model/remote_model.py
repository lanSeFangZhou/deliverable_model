import grpc
import tensorflow as tf

from deliverable_model.serving.model.tensorflow_serving.apis import prediction_service_pb2_grpc
from deliverable_model.serving.model.tensorflow_serving.apis.predict_pb2 import PredictRequest

channel = grpc.insecure_channel("localhost:50051")

stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

request = PredictRequest()
request.inputs[""].CopyFrom(tf.make_tensor_proto(data))

feature_future = stub.Predict()
feature = feature_future.result()
