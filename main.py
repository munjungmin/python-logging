import structlog
from fastapi import FastAPI

# Configure structlog
structlog.configure(
    processors=[ # Chain of functions that transform your log entries
        structlog.processors.add_log_level,  # Add log level to each log
        structlog.processors.TimeStamper(fmt="iso"),  # Add timestamp
        structlog.processors.JSONRenderer()  # Output as JSON
    ]
)

# Create a logger
logger = structlog.get_logger()

# Create FastAPI app
app = FastAPI()

@app.get("/")
async def root():
    logger.info("root_endpoint_called")
    return {"message": "Hello World"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    logger.info("user_endpoint_called", user_id=user_id) # event name, key-value pairs
    return {"user_id": user_id, "name": "John Doe"}

# Run the server when script is executed
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)