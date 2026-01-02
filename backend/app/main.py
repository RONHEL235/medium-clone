from fastapi import FastAPI

app = FastAPI(
    title="Medium Clone API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Medium Clone backend running 🚀"}
