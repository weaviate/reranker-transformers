# Please note this first version is using the Sentence Transformers library
# -- such that model inference and toeknization is coupled
# -- This is likely not optimal compared to i.e. the batch encodign tokenization.
# -- will fix after getting initial POC together.

from sentence_transformers.cross_encoder import CrossEncoder
from pydantic import BaseModel

class CrossEncoderInput(BaseModel):
    Query: str
    Property: str

class CrossEncoderRanker:
    model: CrossEncoder
    cuda: bool
    cuda_core: str

    def __init__(self, model_path: str, cuda_support: bool, cuda_core: str):
        self.cuda = cuda_support
        self.cuda_core = cuda_core
        
        self.model = CrossEncoder(model_path)

        if self.cuda:
            self.model.to(self.cuda_core)

    async def do(self, item: CrossEncoderInput):
        # so probably makes sense to separate tokenization and inference in the future
        # -- just trying to get a POC together.
        cross_inp = [item.Query, item.Property] # this is how Sentence Transformers expects the query-text input 
        return self.model.predict(cross_inp).astype(float)
