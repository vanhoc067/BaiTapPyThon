class Cau3:
    def Add(self, key, value):
        dict = {
            "Information Technology": "Cong nghe thong tin",
            "Software Testing": "Kiem thu phan mem",
            "Data Mining": "Khai pha du lieu",
            "Computer Vision": "Thi giac may tinh"
        }
        if (key not in dict.keys()):
            dict[key] = value

    def ShowAll(self):
        dict = {
            "Information Technology": "Cong nghe thong tin",
            "Software Testing": "Kiem thu phan mem",
            "Data Mining": "Khai pha du lieu",
            "Computer Vision": "Thi giac may tinh"
        }
        print(dict.items())
        print("So tu: ", len(dict))

    def Search(self, keyword):
        dict = {
            "Information Technology": "Cong nghe thong tin",
            "Software Testing": "Kiem thu phan mem",
            "Data Mining": "Khai pha du lieu",
            "Computer Vision": "Thi giac may tinh"
        }
        for k in dict.keys():
            if (k == keyword):
                print("key: ", str(keyword), " co gia tri: ", str(dict[keyword]))

    def DeleteItem(self, keyword):
        dict = {
            "Information Technology": "Cong nghe thong tin",
            "Software Testing": "Kiem thu phan mem",
            "Data Mining": "Khai pha du lieu",
            "Computer Vision": "Thi giac may tinh"
        }
        for k in dict.keys():
            if (k == keyword):
                del dict[keyword]
                print("Xoa thanh cong")
            else:
                print("Khong co tu can xoa")


testCau3 = Cau3()

key = str(input('Nhap tu tieng Anh can them: '))
value = str(input('Nhap y nghia: '))
testCau3.Add(key=key, value=value)

testCau3.ShowAll()
