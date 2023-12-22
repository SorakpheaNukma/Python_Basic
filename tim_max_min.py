#creat by: Mao Sorakpheanukma
def thong_tin_danh_sach(danh_sach):
    if not danh_sach:
        print("Danh sách rỗng.")
        return

    # Tìm phần tử nhỏ nhất, lớn nhất và tính trung bình cộng
    min_phan_tu = min(danh_sach)
    max_phan_tu = max(danh_sach)
    trung_binh_cong = sum(danh_sach) / len(danh_sach)

    # In ra kết quả
    print(f"Phần tử nhỏ nhất: {min_phan_tu}")
    print(f"Phần tử lớn nhất: {max_phan_tu}")
    print(f"Trung bình cộng: {trung_binh_cong}")

    # In ra các phần tử nhỏ hơn và lớn hơn trung bình cộng
    print("Các phần tử nhỏ hơn trung bình cộng:")
    for phan_tu in danh_sach:
        if phan_tu < trung_binh_cong:
            print(phan_tu)

    print("Các phần tử lớn hơn trung bình cộng:")
    for phan_tu in danh_sach:
        if phan_tu > trung_binh_cong:
            print(phan_tu)

# Nhập danh sách từ người dùng (hoặc tuple)
danh_sach_so = input("Nhập danh sách số, cách nhau bằng dấu phẩy: ")
danh_sach = [int(x) for x in danh_sach_so.split(',')]

# Gọi hàm và in kết quả
thong_tin_danh_sach(danh_sach)
