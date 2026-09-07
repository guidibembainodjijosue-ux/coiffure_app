from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'application de coiffure ! L'API fonctionne avec succès."}
