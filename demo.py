import zero_k_cal_varifiyer as zkcv # 驗證者
import zero_k_cal_challenger as zkcc # 挑戰者
import zero_k_setup as zks

if __name__ == "__main__":
    # 公開參數
    p = 1009  # prime number (質數)
    g = 5   # generator (基數)

    # 信任執行設置
    known_values = zks.trusted_setup(p, g)
    p, g, x, y = known_values.p, known_values.g, known_values.x, known_values.y
    print(f"公共參數 (p, g): {p}, {g}")
    print(f"私鑰 (x): {x}")
    print(f"公鑰 (y): {y}")
    
    print("\n這是雙方都知道，約定好的參數 \n")
    print("-------------------------- \n")
    # 零知識挑戰
    print("挑戰者進行驗證要求，驗證者開始製作隨機數 r 與挑戰數 C \n")
    r , C = zkcv.zk_varifiyer_start_challenge(p, g)
    print(f"驗證者生成： r = {r}, C = {C}")
    print("\n這是驗證者生成的隨機數與挑戰數 \n")
    print("-------------------------- \n")
    print("驗證者只將挑戰數Ｃ傳給挑戰者 \n")
    print("-------------------------- \n")
    print("挑戰者將計算隨機值r 與驗證值 s \n")

    r_challenger = zkcc.zk_challanger_find_r(p, g, C)
    s = zkcc.zk_challanger_return(p, x, r_challenger, C)
    print(f"挑戰者算出：r = {r_challenger}, s = {s}")
    print("\n這是挑戰者生成的隨機數與驗證值 \n")
    print("挑戰者用公共參數 (p, g) 及挑戰數 C 求出隨機數r_challenger \n")
    print("挑戰者用隨機數r_challenger、質數 p、私鑰x及挑戰數C求出回傳驗證值s \n")
    print("-------------------------- \n")

    # 驗證過程
    is_valid = zkcv.zk_verifier_varify(p, g, s, C, y)
    print(f"驗證結果：{'成功' if is_valid else '失敗'}")
    print("\n這是驗證者用公共參數 (p, g)、公鑰 y、驗證值 s、挑戰數 C 求出左右兩側值，並比對是否相等 \n")