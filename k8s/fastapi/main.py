from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

AI_MODULE_URL = os.environ.get("AI_MODULE_URL", "http://ai_module:9000/analyze")

# Cette partie sert à gérer le CORS (Cross-Origin Resource Sharing) dans FastAPI.
# Contexte
# Quand ton frontend (dans Nginx, http://localhost) fait une requête JavaScript vers ton API FastAPI (http://fastapi:8000/analyze), le navigateur applique des restrictions de sécurité :
# Par défaut, une page web ne peut pas interroger un domaine différent de celui depuis lequel elle est servie.
# Ici, le frontend et FastAPI sont techniquement sur des origines différentes (localhost:80 vs fastapi:8000), donc le navigateur bloque la requête sauf si l’API autorise explicitement cette origine.

app.add_middleware(
    CORSMiddleware,
   allow_origins=[
    "http://localhost",            # pour dev local
    "http://analyse.cloudns.ch"    # pour prod via Nginx pour AJAX
    ],                             # Seule l'origine localhost est autorisée
    allow_methods=["*"],                  # Autorise GET, POST, etc.
    allow_headers=["*"],                  # Autorise tous les headers
)

@app.get("/analyze")
def analyze(text: str):
    try:
        resp = requests.get(AI_MODULE_URL, params={"text": text}, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI module error: {str(e)}")
