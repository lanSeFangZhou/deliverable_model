# docker run -it --rm -p 8501:8501 -p 8500:8500 -v "${PWD}/deliverable_model_dir/asset/model/keras_saved_model:/models/ner/1" -e MODEL_NAME=ner tensorflow/serving
docker run -it --rm -p 8501:8501 -p 8500:8500 -v "${PWD}/deliverable_model_dir/asset/model/tensorflow_saved_model:/models/ner" -e MODEL_NAME=ner tensorflow/serving
