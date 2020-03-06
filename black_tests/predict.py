import deliverable_model as dm

model = dm.load("/home/howl/PycharmProjects/seq2annotation/blackbox_tests/test_keras_train/results/deliverable_model_dir")

request = dm.make_request(query=["明天天气如何", "打开收音机"])

result = model.inference(request)

print(result.data)
