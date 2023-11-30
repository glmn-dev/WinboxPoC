from app.config import logger_setup
from app.exploit_tool import Exploiter
from app.source_loader import load_mikrotik_list_from_file

if __name__ == "__main__":
    logger_setup("exploit.log")
    mikrotik_list = load_mikrotik_list_from_file("mikrotiks.txt")
    for mikrotik in mikrotik_list:
        exploiter = Exploiter(mikrotik.address, mikrotik.port)
        exploiter.crack()
