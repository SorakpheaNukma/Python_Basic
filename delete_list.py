#creat by: Mao Sorakpheanukma
def xoa_gia_tri(danh_sach, *gia_tri_can_xoa):

    ket_qua = [so for so in danh_sach if so not in gia_tri_can_xoa]
    return ket_qua

# Ví dụ sử dụng hàm
inlist = [5, 8, 11, 9, 11, 8, 8]
gia_tri_can_xoa = [8, 11]
outlist = xoa_gia_tri(inlist, *gia_tri_can_xoa)
print("Danh sách gốc:", inlist)
print("Danh sách sau khi xóa các giá trị:", outlist)
