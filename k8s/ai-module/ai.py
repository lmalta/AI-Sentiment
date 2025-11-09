from fastapi import FastAPI
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
sentiment = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def convert_stars_to_label(result):
    stars = int(result[0]['label'][0])
    label = 'POSITIVE' if stars >= 4 else 'NEGATIVE'
    score = result[0]['score']
    return [{'label': label, 'score': score}]

@app.get("/analyze")
def analyze(text: str):
    raw_result = sentiment(text)
    return convert_stars_to_label(raw_result)
