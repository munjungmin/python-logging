import logging
import database
import auth

logging.basicConfig(
    level=logging.INFO,
    format="%(name)s %(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__) # child logger를 생성 (logger의 이름이 모듈 경로)

logger.info("Application started")
database.connect()
database.query_users()
auth.login("alice")
auth.logout("alice")
logger.info("Application finished")