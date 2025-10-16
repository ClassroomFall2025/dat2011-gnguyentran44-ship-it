menu={
    "1":"Nhập danh sách sinh vien",
    "2":"In danh sách sinh viên",
    "3":"Sắp xếp danh sách sinh viên có học lực giỏi",
    "4":"Sắp xếp danh sách sinh viên theo điểm",
    "5":"Kết thúc"

}
while True:
    for key in menu.keys():
        print(f"{key}: {menu[key]}")
    choice = input("Mời bạn chọn chức năng:")
    if choice == "5":
        break
match choice:
    case "1":
        print("Chương trình kết thúc")
    case "2":
        print("Nhập danh sách sinh viên:")
    case "3":
        print("Sắp xếp danh sách sinh viên có học lực giỏi:")
    case "4":
        print("Sắp xếp danh sách sinh viên theo điểm:")