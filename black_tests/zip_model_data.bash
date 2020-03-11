#!/bin/bash

tar czpvf - ./deliverable_model_dir | split -d -b 20M - ./model_data/part
