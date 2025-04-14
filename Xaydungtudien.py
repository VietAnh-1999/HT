#xay dung tu dien
Tudien ={}
while True:
    print('*******************************Menu**************************')
    print('1- Them tu vung vao tu dien')
    print('2- Tra cuu y nghia 1 tu vung')
    print('3- Cap nhat y nghia 1 tu vung')
    print('4- Xoa 1 tu vung trong tu dien')
    print('5- Xoa toan bo tu vung')
    print('6- In ra toan bo tu vung')
    print('7- In ra toan bo tu vung theo  cau truc ;"Tu vung": "Y ngia"')
    print('8- Ket thuc chuong trinh')

    while True:
        luachon = input("Nhap vao lua chon cua ban: ")
        if luachon.isdigit():
            luachon = int(luachon)
            break
        print("Lua chon khong hop le", end = ", "); print("Vui long nhap lai lua chon cua ban")

    if luachon == 1:
        while True:
            i = input("Nhan phim bat ky de tiep tuc nhap, nhap 'Stop' de dung nhap")
            if i == "Stop":
                break
            else:
                while True:
                    key = input("Nhap vao tu vung: ")
                    if len(key) > 2 and key not in Tudien:
                        print("Can nhap y nghia cho tu vung: {}".format(key))
                        break
                    else:
                        print("Tu vung ban nhap khong hop le")
                while True:
                    value = input("Nhap vao y nghia cua tu vung: ")
                    if len(value) > 1:
                        Tudien.update({key:value})
                        break
                    else:
                        print("Y nghia Tu vung ban nhap khong hop le")
                print("Tu moi duoc them vao tu dien la: ({0} : {1})".format(key,value))

    elif luachon == 2:
        while True:
            word = input('Hay nhap tu can tra: ')
            if word in Tudien:
                print('Y ngia tu {} la:  ({} : {})'.format(word,word,Tudien[word]))
                break
            else:
                print("Tu ban tra khong co trong tu dien, ban hay kiem tra lai")
                print("Nhap 1 de ngung tra \nNhap 0 de tiep tuc tra")
                i = int(input("Nhap:"))
                if i == 1:
                    break

    elif luachon == 3:
        while True:
            word_update = input('Hay nhap tu can cap nhat: ')
            
            if word_update in Tudien: 
                while True:
                    Selection = input("Ban muon Update Keys(K) hay Values(V): ")
                    if Selection == "V":
                        value_change = input('Hay nhap y nghia thay doi cho tu {}: '.format(word_update))
                        Tudien[word_update] = value_change
                        print('Y ngia tu moi duoc thay doi la:  ({} : {})'.format(word_update,Tudien[word_update]))
                        break
                    elif Selection == "K":
                        key_change = input("Hay nhap vao thay doi cho  tu {} : {} :  ".format(word_update, Tudien[word_update]))
                        Tudien[key_change] = Tudien[word_update]
                        Tudien.pop(word_update)
                        break
                break
                
            else:
                print("Tu ban can thay doi khong co trong tu dien, ban hay kiem tra lai")
                print("Nhap 1 de ngung thay doi \nNhap 0 de tiep tuc thay doi")
                i = int(input("Nhap:"))
                if i == 1:
                    break

    elif luachon == 4:
        while True:
            word_delete = input('Hay nhap tu can xóa: ')
            
            if word_delete in Tudien:
                Tudien.pop(word_delete)
                print('Tu moi duoc xoa la:  {}'.format(word_delete))
                break
            else:
                print("Tu ban can thay doi khong co trong tu dien, ban hay kiem tra lai")
                print("Nhap 1 de ngung thay doi \nNhap 0 de tiep tuc thay doi")
                i = int(input("Nhap:"))
                if i == 1:
                    break

    elif luachon == 5:
        while True:
            Submit_Action = input('Ban co chac chan muon xoa toan bo thu vien khong (Y/N): ')
            
            if Submit_Action == "Y":
                Tudien.clear()
                print("Da xoa toan bo thu vien")
                break
            elif Submit_Action == "N":
                break
            else:
                print("Ban da nhap sai yeu cau vui long nhap lai")

    elif luachon == 6:
        while True:
            Submit_print = input('Ban co chac chan muon in toan bo thu vien khong (Y/N): ')
            if Submit_print == "Y":
                print("Tu dien duoc in ra: "); print(Tudien)
                break
            elif Submit_print == "N":
                break
            else:
                print("Ban da nhap sai yeu cau vui long nhap lai")

    elif luachon == 7:
        while True:
            Submit_print_Format = input('Ban co chac chan muon in toan bo thu vien theo format khong (Y/N): ')
            if Submit_print_Format == "Y":
                print("Toan bo tu dien la: ")
                for x,y in Tudien.items():
                    print("{} : {}".format(x,y))
                break
            elif Submit_print_Format == "N":
                break
            else:
                print("Ban da nhap sai yeu cau vui long nhap lai")

    elif luachon == 8:
        print("Ket thuc chuong trinh!")
        break
    #print(Tudien)
    x = input("nhan phim bat ky de tiep tuc")       