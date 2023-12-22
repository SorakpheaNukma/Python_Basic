#creat by: Mao Sorakpheanukma
def tim_phan_so_toi_gian(tu_so, mau_so):
    def tim_uoc_chung(a, b):
        while b:
            a, b = b, a % b
        return a

    uoc_chung = tim_uoc_chung(tu_so, mau_so)
    tu_so_toi_gian = tu_so // uoc_chung
    mau_so_toi_gian = mau_so // uoc_chung

    return tu_so_toi_gian, mau_so_toi_gian

# Nhập phân số từ người dùng
tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))

# Gọi hàm và in kết quả
tu_so_toi_gian, mau_so_toi_gian = tim_phan_so_toi_gian(tu_so, mau_so)
print(f"Phân số tối giản của {tu_so}/{mau_so} là {tu_so_toi_gian}/{mau_so_toi_gian}")
