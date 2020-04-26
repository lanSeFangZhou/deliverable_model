# test one

dockerid=$(docker run -d --rm -p 8501:8501 -p 8500:8500 -v "${PWD}/tf_estimator_deliverable_model_dir/asset/model/tensorflow_saved_model:/models/ner" -e MODEL_NAME=ner tensorflow/serving)

sleep 8

python ./remote_predict.py tf_estimator_deliverable_model_dir

docker stop ${dockerid}

if (($? > 0)); then
    printf 'test failed'
    exit 1
fi


# test two

dockerid=$(docker run -d --rm -p 8501:8501 -p 8500:8500 -v "${PWD}/tf_keras_deliverable_model_dir/asset/model/keras_saved_model:/models/ner/1" -e MODEL_NAME=ner tensorflow/serving)

sleep 8

python ./remote_predict.py tf_keras_deliverable_model_dir

docker stop ${dockerid}

if (($? > 0)); then
    printf 'test failed'
    exit 1
fi
