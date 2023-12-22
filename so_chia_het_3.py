#creat by: Mao Sorakpheanukma
def loc_so_chia_het_cho_3(danh_sach):

    ket_qua = [so for so in danh_sach if so % 3 == 0]
    return ket_qua

# Ví dụ sử dụng hàm
inlist = [3, 6, 8, 11, 9, 16, 21, 22]
outlist = loc_so_chia_het_cho_3(inlist)
print("Danh sách gốc:", inlist)
print("Danh sách chỉ chứa số chia hết cho 3:", outlist)
