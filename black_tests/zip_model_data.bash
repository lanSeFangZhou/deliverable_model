#!/bin/bash

<<<<<<< HEAD
tar czpvf tf_estimator_deliverable_model_dir.tar.gz ./tf_estimator_deliverable_model_dir/
tar czpvf tf_keras_deliverable_model_dir.tar.gz ./tf_keras_deliverable_model_dir/
=======
tar czpvf - ./deliverable_model_dir | split -d -b 20M - ./model_data/part
>>>>>>> 7550df3ca206cd1d7dee54f382fdfc76d7f063a8
