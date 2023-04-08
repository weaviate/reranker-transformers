#!/usr/bin/env python3

from sentence_transformers.cross_encoder import CrossEncoder
# ToDo -- quantize Cross Encoder and separate inference from tokenization

#from optimum.onnxruntime import ORTModelForQuestionAnswering
#from optimum.onnxruntime.configuration import AutoQuantizationConfig
#from optimum.onnxruntime import ORTQuantizer 
import os
import sys
import json

# not sure if this is needed without ONNX enabled
def fix_config_json(model_dir: str, model_name: str):
    with open(f"{model_dir}/config.json", 'r') as f:
        data = json.load(f)

    # For now only dealing with BERT based cross encoders from the sentence transformers library
    if model_name == "cross-encoder/ms-marco-MiniLM-L-6-v2":
        data["model_type"] = "bert"
    
    with open(f"{model_dir}/config.json", 'w') as json_file:
        json.dump(data, json_file)

model_dir = './models/model'
model_name = os.getenv('MODEL_NAME') # Model name is passed in when you build the container, the bash script for this is in the readme
if model_name is None or model_name == "":
    print("Fatal: MODEL_NAME is required")
    sys.exit(1)

onnx_runtime = os.getenv('ONNX_RUNTIME')
if not onnx_runtime:
    onnx_runtime = "false"

onnx_cpu_arch = os.getenv('ONNX_CPU')
if not onnx_cpu_arch:
    onnx_cpu_arch = "ARM64"

print("Downloading model {} from huggingface model hub, onnx_runtime: {}, onnx_cpu_arch: {}".format(model_name, onnx_runtime, onnx_cpu_arch))

# Currently coupling model inference and tokenization in the Sentence Transformers library
model = CrossEncoder(model_name)
model.save_pretrained(model_dir)
