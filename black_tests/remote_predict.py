import deliverable_model as dm
import sys

model_dir = sys.argv[1]

endpoint_config = dm.make_endpoint_config(target="127.0.0.1:8500", model_name="ner")

model = dm.load(model_dir, endpoint_config)

request = dm.make_request(query=["明天天气如何", "上海明天天气"])

result = model.inference(request)

print(result.data)
