#creat by: Mao Sorakpheanukma
def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * tinh_giai_thua(n-1)

# Kiểm tra với một số nguyên không âm
so_nguyen_khong_am = 5
ket_qua = tinh_giai_thua(so_nguyen_khong_am)
print(f"Giai thừa của {so_nguyen_khong_am} là {ket_qua}")
