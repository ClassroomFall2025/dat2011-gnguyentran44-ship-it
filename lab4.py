gia_ban_nuoc = (7500, 8800, 12000, 24000)

def tinh_tien_nuoc(san_luong):
    # ... (code để tính toán sẽ được thêm vào các bước sau)# Code lab 4 bài 1 ở đây
    gia_ban_nuoc = (7500, 8800, 12000, 24000)

def tinh_tien_nuoc(san_luong):
    tien_nuoc = 0
    if san_luong <= 10:
        tien_nuoc = san_luong * gia_ban_nuoc[0]
    elif san_luong <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (san_luong - 10) * gia_ban_nuoc[1]
    elif san_luong <= 30:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (san_luong - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (san_luong - 30) * gia_ban_nuoc[3]
    return tien_nuoc
gia_ban_nuoc = (7500, 8800, 12000, 24000)

def tinh_tien_nuoc(san_luong):
    tien_nuoc = 0
    if san_luong <= 10:
        tien_nuoc = san_luong * gia_ban_nuoc[0]
    elif san_luong <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (san_luong - 10) * gia_ban_nuoc[1]
    elif san_luong <= 30:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (san_luong - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (san_luong - 30) * gia_ban_nuoc[3]
    return tien_nuoc


# Code lab 4  bài 2 ở đây
def tinh_nguyen_lieu(so_banh_dau_xanh, so_banh_thap_cam, so_banh_deo):
    tong_duong = (so_banh_dau_xanh * 0.04) + (so_banh_thap_cam * 0.06) + (so_banh_deo * 0.05)
    tong_dau = (so_banh_dau_xanh * 0.07) + (so_banh_thap_cam * 0) + (so_banh_deo * 0.02)
    nguyen_lieu_can_thiet = {"sugar": tong_duong, "bean": tong_dau}
    return nguyen_lieu_can_thiet