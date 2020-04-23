import deliverable_model as dm

endpoint_config = dm.make_endpoint_config(target="127.0.0.1:8500", model_name ="ner")

model = dm.load("./deliverable_model_dir", endpoint_config)

request = dm.make_request(query=["明天天气如何", "打开收音机"])

result = model.inference(request)

print(result.data)
