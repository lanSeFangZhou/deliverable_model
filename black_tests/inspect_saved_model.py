import tensorflow as tf

with tf.Session(graph=tf.Graph()) as sess:
    imported = tf.saved_model.load(
        sess, ["serve"], "./deliverable_model_dir/asset/model/keras_saved_model"
    )

    input_tensor_name = (
        imported.signature_def["serving_default"].inputs["embedding_input"].name
    )
    output_tensor_name = imported.signature_def["serving_default"].outputs["crf"].name

    print(input_tensor_name)
    print(output_tensor_name)

    print(imported)
