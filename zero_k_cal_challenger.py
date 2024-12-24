from sympy.ntheory import discrete_log

def zk_challanger_find_r(p, g, C):
    """挑戰者計算隨機值 r ， C = g^r mod p。
    :param p: 質數
    :param g: 基數
    :param C: 挑戰
    :return: (r) 正確隨機值
    """
    try:
        # 使用離散對數公式求解 r => r = log_g(C) mod p
        r = discrete_log(p, C, g)
        return r
    except ValueError:
        return None  # 若無法求解則返回 None

def zk_challanger_return(p, x, r, C):
    """挑戰者計算驗證值。
    :param p: 質數
    :param x: 私鑰
    :param r: 隨機值
    :param C: 挑戰
    :return: s 驗證值
    """
    # 計算驗證值 s ， 當 C = 0 時， 回傳 r，否則 ， 回傳 (r + x) mod (p-1)
    s = r if C == 0 else (r + x) % (p - 1)
    return s


