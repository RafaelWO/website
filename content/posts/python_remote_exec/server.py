import logging
import os
import time

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("main")


def main() -> None:
    print(f"Server started. PID: {os.getpid()}")
    while True:
        time.sleep(5)
        logger.debug("This gives the missing context for the error.")
        logger.error("An error occurred!")


if __name__ == "__main__":
    main()
