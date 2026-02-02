import logging
import datetime

# logging.debug("this is my debug log")
# logging.info("this is my info log")
# logging.warning("this is my warning log")
# logging.error("this is my error log")
# logging.critical("this is my critical log")


# # logging.basicConfig(level=logging.DEBUG)
# # 
# # logging.debug("this is my debug log")
# # logging.info("this is my info log")
# # logging.warning("this is my warning log")
# # logging.error("this is my error log")
# # logging.critical("this is my critical log")

# # #logging.basicConfig(level=logging.DEBUG,filename='app.log')
# # #
# # #logging.debug(f"{datetime.datetime.now()}: this is my debug log")
# # #logging.info(f"{datetime.datetime.now()}: this is my info log")
# # #logging.warning(f"{datetime.datetime.now()}: this is my warning log")
# # #logging.error(f"{datetime.datetime.now()}: this is my error log")
# # #logging.critical(f"{datetime.datetime.now()}: this is my critical log")

logging.basicConfig(level=logging.DEBUG,filename='app.log',format='%(asctime)s - %(process)d - %(levelname)s - %(message)s')
logging.debug("this is my debug log")
logging.info("this is my info log")
logging.warning("this is my warning log")
logging.error("this is my error log")
logging.critical("this is my critical log")

