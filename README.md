# cross-ranker-transformers-models
The inference container for the cross-ranker-transformers module

## Documentation

Documentation for this module can be found [here](https://weaviate.io/developers/weaviate/current/reader-generator-modules/qna-transformers.html).

## Build Docker container

```
LOCAL_REPO="ce-ranker" MODEL_NAME="cross-encoder/ms-marco-MiniLM-L-6-v2" ./cicd/build.sh
```

### Local development

```
python3 -m venv .venv
pip3 install -r requirements.txt
```

### Downloading model

Run command: 
```
MODEL_NAME=cross-encoder/ms-marco-MiniLM-L-6-v2 ./download.py
```

### Downloading model with ONNX runtime
To-Do

### Running local server

Run command:
```
python3 -m uvicorn app:app --host 0.0.0.0 --port 8000    
```
