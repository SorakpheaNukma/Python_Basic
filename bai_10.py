#creat by: Mao Sorakpheanukma
def chuan_hoa_xau(xau):
    xau_chuan_hoa = ' '.join(word.capitalize() for word in xau.split())
    return xau_chuan_hoa

# Nhập xâu ký tự từ người dùng
xau_ky_tu = input("Nhập một xâu ký tự: ")

# Gọi hàm và in kết quả
xau_da_chuan_hoa = chuan_hoa_xau(xau_ky_tu)
print("Xâu ký tự sau khi chuẩn hóa:", xau_da_chuan_hoa)
