import random

def zk_varifiyer_start_challenge(p, g):
    """驗證者執行零知識證明過程。
    :param p: 質數
    :param g: 基數
    :return: (r, C) 隨機、挑戰
    """
    r = random.randint(1, p - 2)      # 選擇隨機值 r (1 < r < p-2)
    C = pow(g, r, p)                  # 生成挑戰 C = g^r mod p
    return r, C

def zk_verifier_varify(p, g, s, C, y):
    """驗證者檢查證明是否有效。
    :param p: 質數
    :param g: 基數
    :param y: 公鑰
    :param r: 隨機值
    :param C: 挑戰
    :param s: 驗證
    :return: Boolean (驗證結果)
    """
    if C == 0:
        left = pow(g, s, p)  # 左側 = g ^ r mod p (驗證者直接回傳 r ， 所以 g^s mod p = g ^ r mod p)
        right = C # 右側 = C
        print(f"驗證值 : g^s mod p: {left} = C : {right}")
    else:
        left = (C * y) % p  # 左側 = C * y mod p
        right = pow(g, s, p) # 右側 = (驗證者回傳 s 應該等於(r + x) mod (p - 1) ， 所以 g ^ s mod p = g ^ ( r + x ) mod ( p - 1 ) )
        print(f"驗證值 : C * y mod p: {left} = g ^ s mod p : {right}")
    return left == right