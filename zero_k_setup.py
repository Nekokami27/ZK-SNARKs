from def_var import *

def trusted_setup(p, g):
    """由公共參數 p 和 g 算出 x, y
    :param p: 質數
    :param g: 基數
    :return: (p, g, x, y) 公共參數和私鑰、公鑰
    """
    result =  DefPG(p, g)
    return result
    
def trusted_setup_with_secret(x, p, g):
    """由私鑰 x 和公共參數 p 和 g 算出 y
    :param x: 私鑰
    :param p: 質數
    :param g: 基數
    :return: (p, g, x, y) 公共參數和私鑰、公鑰
    """
    result = DefPGWithSecret(x, p, g)
    return result



