# Please note this first version is using the Sentence Transformers library
# -- such that model inference and toeknization is coupled
# -- This is likely not optimal compared to i.e. the batch encodign tokenization.
# -- will fix after getting initial POC together.

from sentence_transformers.cross_encoder import CrossEncoder
from pydantic import BaseModel
from typing import Optional
import asyncio
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

class CrossEncoderInput(BaseModel):
    query: str
    property: Optional[str]
    documents: Optional[list[str]]

class DocumentScore(BaseModel):
    document: str
    score: float

class CrossEncoderResponse(BaseModel):
    query: str
    scores: Optional[list[DocumentScore]]
    property: Optional[str]
    score: Optional[float]

class CrossEncoderRanker:
    lock: Lock
    executor: ThreadPoolExecutor
    model: CrossEncoder

    def __init__(self, model_path: str, cuda_support: bool, cuda_core: str):
        self.lock = Lock()
        self.executor = ThreadPoolExecutor()
        device = cuda_core if cuda_support else 'cpu'
        self.model = CrossEncoder(model_path, device=device)

    def _batch_rerank(self, item: CrossEncoderInput) -> CrossEncoderResponse:
        sentences = []
        [sentences.append([item.query, document]) for document in item.documents]
        scores = self.model.predict(sentences)
        documentScores = []
        for i in range(len(scores)):
            documentScores.append(DocumentScore(document=item.documents[i], score=scores[i]))
        return CrossEncoderResponse(query=item.query, scores=documentScores)

    def _perform_rerank(self, item: CrossEncoderInput) -> CrossEncoderResponse:
        if item.documents is not None:
            return self._batch_rerank(item)

        cross_inp = [item.query, item.property]
        score = self.model.predict(cross_inp).astype(float)
        return CrossEncoderResponse(query=item.query, property=item.property, score=score)

    def _rerank(self, item: CrossEncoderInput) -> CrossEncoderResponse:
        try:
            self.lock.acquire()
            return self._perform_rerank(item)
        finally:
            self.lock.release()

    async def do(self, item: CrossEncoderInput):
        return await asyncio.wrap_future(self.executor.submit(self._rerank, item))
