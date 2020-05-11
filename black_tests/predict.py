import deliverable_model as dm
import sys

model_dir = sys.argv[1]

model = dm.load(model_dir)

request = dm.make_request(query=["明天天气如何", "上海明天天气"])

result = model.inference(request)

print(result.data)
