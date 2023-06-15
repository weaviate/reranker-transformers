#!/usr/bin/env python3

from sentence_transformers.cross_encoder import CrossEncoder
# ToDo -- quantize Cross Encoder and separate inference from tokenization

#from optimum.onnxruntime import ORTModelForQuestionAnswering
#from optimum.onnxruntime.configuration import AutoQuantizationConfig
#from optimum.onnxruntime import ORTQuantizer 
import os
import sys

model_dir = './models/model'
model_name = os.getenv('MODEL_NAME') # Model name is passed in when you build the container, the bash script for this is in the readme
if model_name is None or model_name == "":
    print("Fatal: MODEL_NAME is required")
    sys.exit(1)

print("Downloading model {} from huggingface model hub".format(model_name))

# Currently coupling model inference and tokenization in the Sentence Transformers library
model = CrossEncoder(model_name)
model.save_pretrained(model_dir)

print("Success")
