python ./predict.py ./tf_keras_deliverable_model_dir && python ./predict.py ./tf_estimator_deliverable_model_dir

if (($? > 0)); then
    printf 'test failed'
    exit 1
fi
