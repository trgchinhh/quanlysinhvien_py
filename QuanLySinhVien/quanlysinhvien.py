# -----------------------------------------------------
# (+) ! python
# (+) github: @trgchinhh
# (+) chương trình quản lý danh sách sinh viên
# -----------------------------------------------------

import os, sys, time, shutil
from dangnhap import *
from math import floor
duongdan = "D:\\ChuongTrinh_Python\\QuanLySinhVien\\danhsachsinhvien.txt"

def banner_chinh():
    os.system("cls")
    chieu_rong_man_hinh = shutil.get_terminal_size().columns
    banner = r"""
    Github: https://github.com/trgchinhh
  ____  _    _         _   _    _  __     __   _____ _____ _   _ _    _   __      _______ ______ _   _ 
 / __ \| |  | |  /\   | \ | |  | | \ \   / /  / ____|_   _| \ | | |  | |  \ \    / /_   _|  ____| \ | |
| |  | | |  | | /  \  |  \| |  | |  \ \_/ /  | (___   | | |  \| | |__| |   \ \  / /  | | | |__  |  \| |
| |  | | |  | |/ /\ \ | . ` |  | |   \   /    \___ \  | | | . ` |  __  |    \ \/ /   | | |  __| | . ` |
| |__| | |__| / ____ \| |\  |  | |____| |    _ ___) |_| |_| |\  | |  | |     \  /   _| |_| |____| |\  |
 \___\_\\____/_/    \_\_| \_|  |______|_|    |_____/|_____|_| \_|_|  |_|      \/   |_____|______|_| \_|

"""
    for dong in banner.splitlines():
        giua_dong = dong.center(chieu_rong_man_hinh)
        for tu in giua_dong:
            sys.stdout.write(tu)
            sys.stdout.flush()
            time.sleep(0.00001) 
        sys.stdout.write("\n")    

def banner_tambiet():
    os.system("cls")
    chieu_rong_man_hinh = shutil.get_terminal_size().columns 
    banner = r"""
    Github: https://github.com/trgchinhh
 _    _ ______ _   _     _____          _____     _               _____ 
| |  | |  ____| \ | |   / ____|   /\   |  __ \   | |        /\   |_   _|
| |__| | |__  |  \| |  | |  __   /  \  | |__) |  | |       /  \    | |  
|  __  |  __| | . ` |  | | |_ | / /\ \ |  ___/   | |      / /\ \   | |  
| |  | | |____| |\  |  | |__| |/ ____ \| |       | |____ / ____ \ _| |_ 
|_|  |_|______|_| \_|   \_____/_/    \_\_|       |______/_/    \_\_____|

"""
    for dong in banner.splitlines():
        giua_dong = dong.center(chieu_rong_man_hinh)
        for tu in giua_dong:
            sys.stdout.write(tu)
            sys.stdout.flush()
            time.sleep(0.00001) 
        sys.stdout.write("\n")    

class SinhVien:
    def __init__(self, ho_ten="", tuoi=0, mssv="", diem=0):
        self.ho_ten = str(ho_ten)
        self.tuoi = int(tuoi)
        self.mssv = str(mssv)
        self.diem = float(diem)

# Lay danh sach sinh vien 
def lay_danh_sach_sinh_vien(duongdan):
    danh_sach_sinh_vien = []
    with open(duongdan, "r", encoding="utf-8") as file:
        for dong in file:
            phan = dong.strip().split(";")
            if len(phan) == 4:
                sinh_vien = SinhVien(phan[0], phan[1], phan[2], phan[3])
                danh_sach_sinh_vien.append(sinh_vien)
    return danh_sach_sinh_vien

# 1 In theo danh sach  
def in_theo_danh_sach(danh_sach_sinh_vien):
    print("\t┌─────┬────────────────────────────────┬───────┬────────────┬───────┐")
    print("\t│ STT │ Ho Ten                         │ Tuoi  │ MSSV       │ Diem  │")
    print("\t├─────┼────────────────────────────────┼───────┼────────────┼───────┤")
    for i, sinh_vien in enumerate(danh_sach_sinh_vien, start=1):
        print(f"\t│ {i:<3} │ {sinh_vien.ho_ten:<30} │ {sinh_vien.tuoi:<5} │ {sinh_vien.mssv:<10} │ {sinh_vien.diem:>5.1f} │")
    print("\t└─────┴────────────────────────────────┴───────┴────────────┴───────┘")


# Ghi vao file data
def ghi_vao_file(duongdan, danh_sach_sinh_vien):
    with open(duongdan, "w", encoding="utf-8") as file:
        for sinh_vien in danh_sach_sinh_vien:
            file.write(sinh_vien.ho_ten + ";" + str(sinh_vien.tuoi) + ";" + sinh_vien.mssv + ";" + str(sinh_vien.diem) + "\n")

# 2 Them vao danh sach
def them_vao_danh_sach(danh_sach_sinh_vien):
    so_luong_muon_them = int(input("\t(?) So luong sinh vien muon them: "))
    for i in range(so_luong_muon_them):
        ho_ten = input("\t\t(?) Nhap ten: ")
        tuoi = int(input("\t\t(?) Nhap tuoi: "))
        mssv = input("\t\t(?) Nhap mssv: ")
        diem = float(input("\t\t(?) Nhap diem: "))
        sinh_vien = SinhVien(ho_ten, tuoi, mssv, diem)
        danh_sach_sinh_vien.append(sinh_vien)
        ghi_vao_file(duongdan, danh_sach_sinh_vien)
    print(f"\t(!) Da them {so_luong_muon_them} sinh vien thanh cong !")    

# 3 Sua danh sach sinh vien 
def sua_danh_sach(danh_sach_sinh_vien):
    in_theo_danh_sach(danh_sach_sinh_vien)
    stt = int(input("\t(?) Nhap so thu tu muon sua thong tin: "))
    if stt < 1 or stt > len(danh_sach_sinh_vien):
        print("\t(!) So thu tu khong hop le !")
        return 
    sinh_vien = SinhVien()
    sinh_vien = danh_sach_sinh_vien[stt-1]
    ten_moi = input("\t\t(?) Nhap ten moi (Enter bo qua neu khong sua): ")
    if ten_moi:
        sinh_vien.ho_ten = ten_moi
    tuoi_moi = int(input("\t\t(?) Nhap tuoi moi (nhap 0 bo qua neu khong sua): "))
    if tuoi_moi > 0:
        sinh_vien.tuoi = tuoi_moi
    mssv_moi = input("\t\t(?) Nhap ma so sinh vien moi (nhap enter bo qua neu khong sua): ")
    if mssv_moi:
        sinh_vien.mssv = mssv_moi
    diem_moi = float(input("\t\t(?) Nhap diem moi (nhap -1 bo qua neu khong sua): "))
    if(diem_moi >= 0):
        sinh_vien.diem = diem_moi
    ghi_vao_file(duongdan, danh_sach_sinh_vien)
    print(f"\t(*) Da cap nhat thanh cong thong tin sinh vien so thu tu {stt}")        

# 4 Xoa thong tin sinh vien
def xoa_sinh_vien(danh_sach_sinh_vien):
    in_theo_danh_sach(danh_sach_sinh_vien)
    stt = int(input("\t(?) Nhap so thu tu sinh vien muon xoa: "))
    if stt < 1 or stt > len(danh_sach_sinh_vien):
        print("\t(!) So thu tu khong hop le !")
        return
    sinh_vien = SinhVien()
    sinh_vien = danh_sach_sinh_vien[stt-1]
    del danh_sach_sinh_vien[stt-1]
    ghi_vao_file(duongdan, danh_sach_sinh_vien)
    print(f"\t(*) Da xoa thong tin sinh vien {sinh_vien.ho_ten} - stt: {stt}")    

# 5 Tim kiem thong tin xin vien 
def tim_kiem_sinh_vien(danh_sach_sinh_vien):
    print("\t1 - Tim kiem theo so thu tu")
    print("\t2 - Tim kiem theo ky tu ten")
    print("\t3 - Tim kiem theo mssv")
    lua_chon = input("\t(?) Nhap lua chon muon tim kiem: ")
    stt = 1
    if lua_chon == "1":
        stt = int(input("\t\t(?) Nhap vao so thu tu muon tim kiem: "))
        if stt < 1 or stt > len(danh_sach_sinh_vien):
            print("\t(!) So thu tu khong hop le !")
            return 
        sinh_vien = SinhVien()
        sinh_vien = danh_sach_sinh_vien[stt-1]
        print("\t┌─────┬────────────────────────────────┬───────┬────────────┬───────┐")
        print("\t│ STT │ Ho Ten                         │ Tuoi  │ MSSV       │ Diem  │")
        print("\t├─────┼────────────────────────────────┼───────┼────────────┼───────┤")
        print(f"\t│ {stt:<3} │ {sinh_vien.ho_ten:<30} │ {sinh_vien.tuoi:<5} │ {sinh_vien.mssv:<10} │ {sinh_vien.diem:>5.1f} │")
        print("\t└─────┴────────────────────────────────┴───────┴────────────┴───────┘")
    elif lua_chon == "2":
        nhap_ky_tu = input("\t\t(?) Nhap ky tu muon tim kiem: ")
        danh_sach_tim_kiem = []
        sinh_vien = SinhVien()
        for sinh_vien in danh_sach_sinh_vien:
            if nhap_ky_tu.lower() in sinh_vien.ho_ten.lower():
                danh_sach_tim_kiem.append(sinh_vien)
        if not danh_sach_tim_kiem:
            print("\t(!) Khong tim thay sinh vien nao phu hop !")
            return 
        print("\t┌─────┬────────────────────────────────┬───────┬────────────┬───────┐")
        print("\t│ STT │ Ho Ten                         │ Tuoi  │ MSSV       │ Diem  │")
        print("\t├─────┼────────────────────────────────┼───────┼────────────┼───────┤")
        for i, sinh_vien in enumerate(danh_sach_tim_kiem, start=1):
            print(f"\t│ {i:<3} │ {sinh_vien.ho_ten:<30} │ {sinh_vien.tuoi:<5} │ {sinh_vien.mssv:<10} │ {sinh_vien.diem:>5.1f} │")
        print("\t└─────┴────────────────────────────────┴───────┴────────────┴───────┘")   
    elif lua_chon == "3":
        mssv = input("\t\t(?) Nhap ky tu mssv muon tim kiem: ")
        danh_sach_tim_kiem = []
        sinh_vien = SinhVien()
        for sinh_vien in danh_sach_sinh_vien:
            if mssv in sinh_vien.mssv:
                danh_sach_tim_kiem.append(sinh_vien)
        if not danh_sach_tim_kiem:
            print("\t(!) Khong tim thay sinh vien phu hop !")
            return 
        print("\t┌─────┬────────────────────────────────┬───────┬────────────┬───────┐")
        print("\t│ STT │ Ho Ten                         │ Tuoi  │ MSSV       │ Diem  │")
        print("\t├─────┼────────────────────────────────┼───────┼────────────┼───────┤")
        for i, sinh_vien in enumerate(danh_sach_tim_kiem, start=1):
            print(f"\t│ {i:<3} │ {sinh_vien.ho_ten:<30} │ {sinh_vien.tuoi:<5} │ {sinh_vien.mssv:<10} │ {sinh_vien.diem:>5.1f} │")
        print("\t└─────┴────────────────────────────────┴───────┴────────────┴───────┘")        
    else:
        print("\t(!) Vui long chon lai 1 -> 3")

# 6 sap xep danh sach sinh vien
def sap_xep_danh_sach(danh_sach_sinh_vien):
    print("\t1 - Sap xep theo ten (A -> Z)")
    print("\t2 - Sap xep theo ten (Z -> A)")
    print("\t3 - Sap xep theo diem (Cao -> Thap)")
    print("\t4 - Sap xep theo diem (Thap -> Cao)")
    print("\t5 - Sap xep theo tuoi (Tang dan)")
    print("\t6 - Sap xep theo tuoi (Giam dan)")
    lua_chon = input("\t(?) Nhap lua chon muon sap xep: ")
    sinh_vien = SinhVien()
    def lay_ten(ho_ten):
        return ho_ten.strip().split()[-1].lower() 
    if lua_chon == "1":
        danh_sach_sinh_vien.sort(key=lambda sinh_vien: lay_ten(sinh_vien.ho_ten))
        print("\t\t(*) Da sap xep theo ten (A-Z)")
    elif lua_chon == "2":
        danh_sach_sinh_vien.sort(key=lambda sinh_vien: lay_ten(sinh_vien.ho_ten), reverse=True)
        print("\t\t(*) Da sap xep theo ten (Z-A)")
    elif lua_chon == "3":
        danh_sach_sinh_vien.sort(key=lambda sinh_vien: sinh_vien.diem, reverse=True)
        print("\t\t(*) Da sap xep theo diem (cao -> thap)")
    elif lua_chon == "4":
        danh_sach_sinh_vien.sort(key=lambda sinh_vien: sinh_vien.diem)
        print("\t\t(*) Da sap xep theo diem (thap -> cao)")
    elif lua_chon == "5":
        danh_sach_sinh_vien.sort(key=lambda sinh_vien: sinh_vien.tuoi)
        print("\t\t(*) Da sap xep theo tuoi (tang dan)")
    elif lua_chon == "6":
        danh_sach_sinh_vien.sort(key=lambda sinh_vien: sinh_vien.tuoi, reverse=True)
        print("\t\t(*) Da sap xep theo tuoi (giam dan)")
    else:
        print("\t(!) Vui long chon lai 1-> 6")
        return 
    print("\t┌─────┬────────────────────────────────┬───────┬────────────┬───────┐")
    print("\t│ STT │ Ho Ten                         │ Tuoi  │ MSSV       │ Diem  │")
    print("\t├─────┼────────────────────────────────┼───────┼────────────┼───────┤")
    for i, sinh_vien in enumerate(danh_sach_sinh_vien, start=1):
        print(f"\t│ {i:<3} │ {sinh_vien.ho_ten:<30} │ {sinh_vien.tuoi:<5} │ {sinh_vien.mssv:<10} │ {sinh_vien.diem:>5.1f} │")
    print("\t└─────┴────────────────────────────────┴───────┴────────────┴───────┘")    
    lua_chon_ghi_vao_file = input("\t(?) Luu noi dung da sap xep vao file (y/n): ")
    if lua_chon_ghi_vao_file == "y":
        ghi_vao_file(duongdan, danh_sach_sinh_vien)
        print("\t(*) Ban da chon ghi vao file !")
    else:
        print("\t(*) Ban da chon khong ghi vao file !")    

# ve bieu do cot 
def ve_bieu_do_cot_cach_deu(danh_sach_sinh_vien):
    top5 = sorted(danh_sach_sinh_vien, key=lambda sv: sv.diem, reverse=True)[:5]
    ten_top5 = [sv.ho_ten.split()[-1][:6] for sv in top5]
    diem_top5 = [sv.diem for sv in top5]
    sv_con_lai = danh_sach_sinh_vien[5:] if len(danh_sach_sinh_vien) > 5 else []
    diem_tb_con_lai = sum(sv.diem for sv in sv_con_lai) / len(sv_con_lai) if sv_con_lai else 0
    ten_top5.append("Khac")
    diem_top5.append(diem_tb_con_lai)
    chieu_cao = [floor(d) for d in diem_top5]
    so_cot = len(chieu_cao)
    do_rong_cot = 5 
    print("\n\tBiểu đồ điểm 5 sinh vien cao nhất lớp\n")
    for y in range(10, -1, -1):
        if y == 10:
            print("\t       Y")
            print("\t       ↑")
        dong = f"\t{y:>4}.0 ├"
        for cao in chieu_cao:
            if cao >= y:
                dong += f"{'┃'.center(do_rong_cot)}"
            else:
                dong += " " * do_rong_cot
        print(dong)
    print("\t       └" + "─" * (do_rong_cot * so_cot) + "─> X")
    dong_ten = "\t       "
    for ten in ten_top5:
        dong_ten += ten.center(do_rong_cot)
    print(dong_ten)


# 7 thong ke danh sach sinh vien 
def thong_ke_danh_sach(danh_sach_sinh_vien):
    hsg = 0; hsk = 0; hstb = 0; hsy = 0; tdcl = 0; diem_max = 0 
    sinh_vien = SinhVien()
    for sinh_vien in danh_sach_sinh_vien:
        if sinh_vien.diem >= 8 and sinh_vien.diem <= 10: hsg += 1
        elif sinh_vien.diem >= 6.5 and sinh_vien.diem < 8: hsk += 1
        elif sinh_vien.diem >= 4 and sinh_vien.diem < 6.5: hstb += 1
        else: hsy += 1
        tdcl += sinh_vien.diem
        if(sinh_vien.diem > diem_max): diem_max = sinh_vien.diem

    slsv = len(danh_sach_sinh_vien)
    diem_tbcl = tdcl / slsv
    tl_hsg = (hsg / slsv) * 100
    tl_hsk = (hsk / slsv) * 100
    tl_hstb = (hstb / slsv) * 100
    tl_hsy = (hsy / slsv) * 100
    print(f"\t(!) So luong sinh ca lop: {slsv}")
    print(f"\t(!) Diem trung binh ca lop: {diem_tbcl:.2f}")
    print(f"\t(!) Ty le sinh vien gioi: {tl_hsg:.1f}%")
    print(f"\t(!) Ty le sinh vien kha: {tl_hsk:.1f}%")
    print(f"\t(!) Ty le sinh vien trung binh: {tl_hstb:.1f}%")
    print(f"\t(!) Ty le sinh vien yeu: {tl_hsy:.1f}%")
    ve_bieu_do_cot_cach_deu(danh_sach_sinh_vien)
    print(f"\n\t(+) Danh sach sinh vien cao diem nhat lop - {diem_max} diem")
    print("\t┌─────┬────────────────────────────────┬───────┬────────────┬───────┐")
    print("\t│ STT │ Ho Ten                         │ Tuoi  │ MSSV       │ Diem  │")
    print("\t├─────┼────────────────────────────────┼───────┼────────────┼───────┤")
    for i, sinh_vien in enumerate(danh_sach_sinh_vien, start=1):
        if sinh_vien.diem == diem_max:
            print(f"\t│ {i:<3} │ {sinh_vien.ho_ten:<30} │ {sinh_vien.tuoi:<5} │ {sinh_vien.mssv:<10} │ {sinh_vien.diem:>5.1f} │")
    print("\t└─────┴────────────────────────────────┴───────┴────────────┴───────┘")          

# main
def main():
    while(True):
        os.system("cls")
        banner_chinh()
        print("┌─────")
        print("├ 1 - In theo danh sach")
        print("├ 2 - Them")
        print("├ 3 - Sua")
        print("├ 4 - Xoa")
        print("├ 5 - Tim kiem")
        print("├ 6 - Sap xep")
        print("├ 7 - Thong ke")
        print("├ 8 - Thoat")
        danh_sach_sinh_vien = lay_danh_sach_sinh_vien(duongdan)
        lua_chon = input("└───────➤ Nhap lenh: ")
        if lua_chon == "1":
            print(f"[{lua_chon}] In danh sach sinh vien")
            in_theo_danh_sach(danh_sach_sinh_vien)
        elif lua_chon == "2":
            print(f"[{lua_chon}] Them vao danh sach sinh vien")  
            them_vao_danh_sach(danh_sach_sinh_vien) 
        elif lua_chon == "3":
            print(f"[{lua_chon}] Sua danh sach sinh vien")
            sua_danh_sach(danh_sach_sinh_vien)
        elif lua_chon == "4":
            print(f"[{lua_chon}] Xoa sinh vien khoi danh sach")
            xoa_sinh_vien(danh_sach_sinh_vien)    
        elif lua_chon == "5":
            print(f"[{lua_chon}] Tim kiem sinh vien tu danh sach")
            tim_kiem_sinh_vien(danh_sach_sinh_vien)  
        elif lua_chon == "6":
            print(f"[{lua_chon}] Sap xep sinh vien tu danh sach")
            sap_xep_danh_sach(danh_sach_sinh_vien)
        elif lua_chon == "7":
            print(f"[{lua_chon}] Thong ke danh sach sinh vien")
            thong_ke_danh_sach(danh_sach_sinh_vien)  
        elif lua_chon == "8":
            print(f"[{lua_chon}] Quay lai")
            tiep_tuc()
            dangnhap()
        else:
            print("\nNhap sai vui long nhap lai !")    
        tiep_tuc()   

# dang nhap
def dangnhap():
    while(True):
        os.system("cls")
        banner_chinh()
        print("┌─────")
        print("├ 1 - Dang ky")
        print("├ 2 - Dang nhap")
        print("├ 3 - Xoa tai khoan")
        print("├ 4 - Thoat")
        lua_chon = input("└───────➤ Nhap lenh: ")
        if lua_chon == "1":
            dangkytaikhoan = DangKyTaiKhoan()
        elif lua_chon == "2":
            dangnhaptaikhoan = DangNhapTaiKhoan()   
            xacnhandangnhap = dangnhaptaikhoan.xac_nhan_dang_nhap()
            if xacnhandangnhap:
                main()
        elif lua_chon == "3":
            xoa_tai_khoan = XoaTaiKhoan()
        else :
            banner_tambiet()
            break    

dangnhap()
