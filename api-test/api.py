from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Hello, Vitalii!",
    description="Vitalii API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }
@app.get("/thank_you")
async def hello_world():
    return {
        "status": "Thank you! Bulat!"
    }

if __name__ == "main":
    print("Hello, Vitalii!")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)