from app.models import Mikrotik, MikrotikList


def load_mikrotik_list_from_file(file_path: str) -> MikrotikList:
    mikrotik_list = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(":")
            if len(parts) == 2:
                ip = parts[0]
                port = int(parts[1])
                mikrotik = Mikrotik(ip, port)
                mikrotik_list.append(mikrotik)
    return MikrotikList(mikrotik_list)
