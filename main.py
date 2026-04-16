import logging

# Create two handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[console_handler, file_handler]
 )

logging.debug("debug") # level 1
logging.info("info")
logging.warning("warning") # default
logging.error("error")
logging.critical("critical") # level 5