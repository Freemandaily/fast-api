from fastapi import FastAPI


# Initialize FastAPI app
app = FastAPI()

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "success": True,
        "status": "healthy"
    }
