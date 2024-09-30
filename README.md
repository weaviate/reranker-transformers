# Cross ranker transformers module

The inference container for Weaviate's reranker-transformers module

📚 Documentation
-----------------

Documentation for this module can be found [here](https://weaviate.io/developers/weaviate/model-providers/transformers/reranker).

📦 Requirements
----------------

1. Create a new virtual environment

```sh
python3 -m venv .venv
source .venv/bin/activate
```

2. Install all module and test dependencies

```sh
pip3 install -r requirements.txt
pip3 install -r requirements-test.txt
```

3. Download the model locally

```sh
MODEL_NAME=cross-encoder/ms-marco-MiniLM-L-6-v2 ./download.py
```

5. Run the inference server

```sh
uvicorn app:app --host 0.0.0.0 --port 8000
```

💡 Testing
----------

For sanity checks that to check that all works properly you can run our smoke tests against your server

```sh
python3 smoke_tests.py
```

🐳 Docker support
-----------------

In order to build locally a docker image one can run this command in project's root folder

```sh
LOCAL_REPO="local-reranker" MODEL_NAME="cross-encoder/ms-marco-MiniLM-L-6-v2" ./cicd/build.sh
```

In order to test the built docker image run this command in project's root folder

```sh
LOCAL_REPO="local-reranker" ./cicd/test.sh
```

🔗 Useful Resources
--------------------

- [HuggingFace cross-encoder/ms-marco-MiniLM-L-6-v2 model description](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L-6-v2)
