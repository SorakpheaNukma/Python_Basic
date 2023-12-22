#creat by: Mao Sorakpheanukma
def kiem_tra_doi_xung(xau):
    xau = xau.lower()  # Chuyển đổi tất cả ký tự thành chữ thường để kiểm tra không phân biệt chữ hoa/chữ thường
    xau = ''.join(c for c in xau if c.isalnum())  # Loại bỏ các ký tự không phải chữ cái và số

    return xau == xau[::-1]

# Nhập xâu ký tự từ người dùng
xau_ky_tu = input("Nhập một xâu ký tự: ")

# Gọi hàm và in kết quả
if kiem_tra_doi_xung(xau_ky_tu):
    print("Xâu ký tự là đối xứng.")
else:
    print("Xâu ký tự không đối xứng.")
