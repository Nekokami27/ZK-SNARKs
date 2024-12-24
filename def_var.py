from abc import ABC, abstractmethod
import random
from typing import Tuple

class Def():
    @abstractmethod
    def __init__(ABC):
        pass

class DefPG(Def):
    def __init__(self, p, g) -> Tuple[int, int, int, int]:
        """
        設定質數和基數
        :param p: 質數
        :param g: 基數'
        :return: (p, g, x, y) 公共參數和私鑰、公鑰
        """
        self.p = p
        self.g = g
        self.x = random.randint(1, p - 2) # 私鑰 between 1 and p-2
        self.y = pow(g, self.x, p) # 公鑰 y = g^x mod p


class DefPGWithSecret(Def):
    def __init__(self, x, p, g) -> Tuple[int, int, int, int]:
        """
        設定私鑰和質數和基數
        :param x: 私鑰
        :param p: 質數
        :param g: 基數
        :return: (p, g, x, y) 公共參數和私鑰、公鑰
        """
        self.x = x
        self.p = p
        self.g = g
        self.y = pow(g, x, p) # 公鑰 y = g^x mod p