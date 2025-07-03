import hashlib, json, time  

def hash_du_lieu(data):
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

def tiep_tuc():
    input("\nPress any key to continue ...")
    return 

class DangKyTaiKhoan:
    def __init__(self):
        self.path = "D:\\ChuongTrinh_Python\\QuanLySinhVien\\taikhoan.txt"
        self.file_rong = self.kiem_tra_file_rong()
        if not self.file_rong:
            print("\t(!) Da co tai khoan ! Vui long dang nhap")
            tiep_tuc()
            return 
        self.ten_dang_ky = self.nhap_ten_dang_ky()
        self.mat_khau = self.nhap_mat_khau()
        self.ghi_vao_file = self.ghi_vao_file()

    def kiem_tra_file_rong(self):
        with open(self.path, "r", encoding="utf-8") as file:
            return file.read().strip() == ""  

    def nhap_ten_dang_ky(self):
        ten_dang_nhap = input("(?) Nhap ten dang nhap: ").strip()
        if len(ten_dang_nhap) < 1:
            print("\t(!) Ten dang nhap khong hop le !")
            return 
        with open(self.path, "r", encoding="utf-8") as file:
            for dong in file:
                phan = dong.strip().split(";")
                if hash_du_lieu(phan[0]) == hash_du_lieu(ten_dang_nhap):
                    print("\t(!) Ten dang nhap ton tai !")
                    return self.nhap_ten_dang_ky() 
        return hash_du_lieu(ten_dang_nhap)
        
    def nhap_mat_khau(self):
        mat_khau = input("(?) Nhap mat khau: ").strip()
        if len(mat_khau) < 8:
            print("\t(!) Ma khau phai tu 8 ky tu tro len !")
            return self.nhap_mat_khau()
        return hash_du_lieu(mat_khau)
        
    def ghi_vao_file(self):
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(self.ten_dang_ky + ";" + self.mat_khau) 
        print("\t(*) Da them tai khoan thanh cong !")          
        tiep_tuc()                 

class DangNhapTaiKhoan:
    def __init__(self):
        self.path = "D:\\ChuongTrinh_Python\\QuanLySinhVien\\taikhoan.txt"
        self.file_rong = self.kiem_tra_file_rong()
        if self.file_rong:
            print("\t(!) Chua co tai khoan ! Vui long dang ky")
            tiep_tuc()
            self.ten_dang_nhap = None
            self.mat_khau = None
            return 
        self.ten_dang_nhap, self.ten_dang_nhap1 = self.nhap_ten_dang_nhap()
        if not self.ten_dang_nhap:
            self.mat_khau = None
            return
        self.mat_khau = self.nhap_mat_khau()

    def kiem_tra_file_rong(self):
        with open(self.path, "r", encoding="utf-8") as file:
            return file.read().strip() == ""  

    def nhap_ten_dang_nhap(self):
        ten_dang_nhap = input("(?) Nhap ten dang nhap: ").strip()
        if len(ten_dang_nhap) < 1:
            print("\t(!) Ten dang nhap khong hop le !")
            return self.nhap_ten_dang_nhap()
        with open(self.path, "r", encoding="utf-8") as file:
            for dong in file:
                phan = dong.strip().split(";")
                if phan[0] != hash_du_lieu(ten_dang_nhap):
                    print("\t(!) Ten dang nhap sai hoac khong ton tai ! Vui long dang ky tai khoan")
                    return self.nhap_ten_dang_nhap()                      
        return True, ten_dang_nhap

    def nhap_mat_khau(self):
        mat_khau = input("(?) Nhap mat khau: ").strip()
        if len(mat_khau) < 8:
            print("\t(!) Ma khau phai tu 8 ky tu tro len !")
            return self.nhap_mat_khau()
        with open(self.path, "r", encoding="utf-8") as file:
            for dong in file:
                phan = dong.strip().split(";")
                if phan[1] != hash_du_lieu(mat_khau):
                    print("\t(!) Mat khau sai ! Vui long nhap lai")
                    return self.nhap_mat_khau()
        return True

    def xac_nhan_dang_nhap(self):
        if(self.ten_dang_nhap and self.mat_khau):
            print("\t(*) Dang nhap thanh cong !")
            tiep_tuc()
            return True
        else :
            return False   

class XoaTaiKhoan:
    def __init__(self):
        self.path = "D:\\ChuongTrinh_Python\\QuanLySinhVien\\taikhoan.txt"
        self.file_rong = self.kiem_tra_file_rong()
        self.ten_dang_nhap = self.nhap_ten_dang_nhap()
        self.mat_khau = self.nhap_mat_khau()
        self.xoa_tai_khoan = self.xoa_tai_khoan()

    def kiem_tra_file_rong(self):
        with open(self.path, "r", encoding="utf-8") as file:
            return file.read().strip() == ""  

    def nhap_ten_dang_nhap(self):
        ten_dang_nhap = input("(?) Nhap ten dang nhap: ").strip()
        if len(ten_dang_nhap) < 1:
            print("\t(!) Ten dang nhap khong hop le !")
            return self.nhap_ten_dang_nhap()
        with open(self.path, "r", encoding="utf-8") as file:
            for dong in file:
                phan = dong.strip().split(";")
                if phan[0] != hash_du_lieu(ten_dang_nhap):
                    print("\t(!) Ten dang nhap khong ton tai ! Vui long dang ky tai khoan")
                    return self.nhap_ten_dang_nhap()   
        return True

    def nhap_mat_khau(self):
        mat_khau = input("(?) Nhap mat khau: ").strip()
        if len(mat_khau) < 8:
            print("\t(!) Ma khau phai tu 8 ky tu tro len !")
            return self.nhap_mat_khau()
        with open(self.path, "r", encoding="utf-8") as file:
            for dong in file:
                phan = dong.strip().split(";")
                if phan[1] != hash_du_lieu(mat_khau):
                    print("\t(!) Mat khau sai ! Vui long nhap lai")
                    return self.nhap_mat_khau()
        return True 

    def xoa_tai_khoan(self):
        if(self.ten_dang_nhap and self.mat_khau):
            with open(self.path, "w", encoding="utf-8") as file:
                pass
        print("\t(*) Xoa tai khoan thanh cong !")  
        tiep_tuc()       
