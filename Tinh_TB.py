#creat by: Mao Sorakpheanukma
def tinh_gia_tri_trung_binh(danh_sach):
    if not danh_sach:
        return None
    else:
        tong = sum(danh_sach)

        return tong / 2


danh_sach_so = input("Nhập danh sách số nguyên, cách nhau bằng dấu phẩy: ")
danh_sach = [int(x) for x in danh_sach_so.split(',')]

ket_qua = tinh_gia_tri_trung_binh(danh_sach)
if ket_qua is not None:
    print(f"Giá trị trung bình của danh sách là: {ket_qua}")
else:
    print("Danh sách rỗng, không thể tính giá trị trung bình.")
