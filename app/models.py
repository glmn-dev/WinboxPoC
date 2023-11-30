from dataclasses import dataclass
from typing import List


@dataclass
class Mikrotik:
    address: str
    port: int


@dataclass
class MikrotikList:
    addresses: List[Mikrotik]

    def __iter__(self):
        return iter(self.addresses)
