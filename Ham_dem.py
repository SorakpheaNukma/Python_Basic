#creat by: Mao Sorakpheanukma
def tim_doan_tang_dai_nhat(danh_sach):
    if not danh_sach:
        return 0, []  # Trả về 0 nếu danh sách rỗng

    max_doan_tang = [danh_sach[0]]
    current_doan_tang = [danh_sach[0]]
    so_doan_tang = 1

    for i in range(1, len(danh_sach)):
        if danh_sach[i] > danh_sach[i - 1]:
            current_doan_tang.append(danh_sach[i])
        else:
            current_doan_tang = [danh_sach[i]]

        if len(current_doan_tang) > len(max_doan_tang):
            max_doan_tang = current_doan_tang

    return so_doan_tang, max_doan_tang

# Nhập danh sách từ người dùng
danh_sach_so = input("Nhập danh sách số, cách nhau bằng dấu phẩy: ")
danh_sach = [int(x) for x in danh_sach_so.split(',')]

# Gọi hàm và in kết quả
so_doan_tang, doan_tang_dai_nhat = tim_doan_tang_dai_nhat(danh_sach)
print(f"Số đoạn tăng: {so_doan_tang}")
print(f"Doạn tăng dài nhất: {doan_tang_dai_nhat}")
