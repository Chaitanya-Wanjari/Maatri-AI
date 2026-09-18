from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import router
from backend.api.health import router as health_router

# English loaders
from backend.english_rag.loader import (
    get_encoder as get_en_encoder,
    get_cross_encoder as get_en_cross,
    get_vectorstores as get_en_store,
)

# Hindi loaders
from backend.hindi_rag.loader import (
    get_encoder as get_hi_encoder,
    get_cross_encoder as get_hi_cross,
    get_vectorstore as get_hi_store,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Preloading Maatri models...")
    
    # English
    get_en_encoder()
    get_en_cross()
    get_en_store()

    # Hindi
    get_hi_encoder()
    get_hi_cross()
    get_hi_store()

    print("All models loaded successfully.\n")

    yield


app = FastAPI(
    title="Maatri AI",
    version="2.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(router)
