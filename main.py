from fastapi import FastAPI
import logging
import uvicorn

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),  # To file
        logging.StreamHandler()  # To terminal
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/divide")
def divide(a: int, b: int):
    try:
        result = a / b
        return {"result": result}
    except Exception as e:
        logger.error("Division failed", exc_info=True) # trace stack을 볼 수 있음
        # logger.exception("Division failed")          
        return {"error": "Something went wrong"}

# Run the server when script is executed
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)