from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "Maatri AI",
        "version": "1.0.0",
    }