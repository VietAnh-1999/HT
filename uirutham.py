import tkinter as tk
from tkinter import messagebox
import random

# Tạo tập hợp chứa các mã dự thưởng
Thung = set()

# Hàm thêm mã dự thưởng
def them_ma():
    ma = entry_ma.get().strip()
    if not ma:
        messagebox.showwarning("Lỗi", "Vui lòng nhập mã dự thưởng!")
        return

    if ma in Thung:
        messagebox.showwarning("Thông báo", f"Mã '{ma}' đã tồn tại!")
    else:
        Thung.add(ma)
        cap_nhat_danh_sach()
        messagebox.showinfo("Thành công", f"Đã thêm mã '{ma}'!")

    entry_ma.delete(0, tk.END)

# Hàm xóa mã dự thưởng
def xoa_ma():
    ma = entry_ma.get().strip()
    if ma in Thung:
        Thung.remove(ma)
        cap_nhat_danh_sach()
        messagebox.showinfo("Thành công", f"Đã xóa mã '{ma}'!")
    else:
        messagebox.showwarning("Lỗi", f"Mã '{ma}' không tồn tại!")

    entry_ma.delete(0, tk.END)

# Hàm quay số ngẫu nhiên
def quay_so():
    if not Thung:
        messagebox.showwarning("Lỗi", "Thùng phiếu rỗng, không thể quay số!")
        return
    
    ma_trung_thuong = random.choice(list(Thung))  # Lấy ngẫu nhiên một phần tử
    messagebox.showinfo("Chúc mừng!", f"Mã '{ma_trung_thuong}' đã trúng thưởng!")
    Thung.remove(ma_trung_thuong)  # Xóa mã trúng thưởng khỏi danh sách
    cap_nhat_danh_sach()

# Hàm cập nhật danh sách mã trên giao diện
def cap_nhat_danh_sach():
    listbox_ma.delete(0, tk.END)
    for ma in Thung:
        listbox_ma.insert(tk.END, ma)

# Hàm thoát chương trình
def thoat():
    root.destroy()

# Tạo cửa sổ giao diện chính
root = tk.Tk()
root.title("Chương trình Rút Thăm Trúng Thưởng")
root.geometry("1200x850")
root.resizable(False, False)

# Tiêu đề
label_title = tk.Label(root, text="🎉 Rút Thăm Trúng Thưởng 🎉", font=("Arial", 20, "bold"))
label_title.pack(pady=10)

# Nhập mã dự thưởng
frame_input = tk.Frame(root)
frame_input.pack(pady=5)
label_ma = tk.Label(frame_input, text="Nhập mã:", font=("Arial", 12))
label_ma.pack(side=tk.LEFT, padx=5)
entry_ma = tk.Entry(frame_input, font=("Arial", 12), width=20)
entry_ma.pack(side=tk.LEFT)

# Nút Thêm & Xóa
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)
btn_them = tk.Button(frame_buttons, text="Thêm", font=("Arial", 12), command=them_ma)
btn_them.pack(side=tk.LEFT, padx=5)
btn_xoa = tk.Button(frame_buttons, text="Xóa", font=("Arial", 12), command=xoa_ma)
btn_xoa.pack(side=tk.LEFT, padx=5)

# Danh sách mã dự thưởng
label_ds = tk.Label(root, text="📋 Danh sách mã dự thưởng:", font=("Arial", 12, "bold"))
label_ds.pack()
listbox_ma = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
listbox_ma.pack(pady=5)

# Nút Quay Số & Thoát
frame_actions = tk.Frame(root)
frame_actions.pack(pady=5)
btn_quay = tk.Button(frame_actions, text="🎲 Quay Số", font=("Arial", 12, "bold"), command=quay_so)
btn_quay.pack(side=tk.LEFT, padx=10)
btn_thoat = tk.Button(frame_actions, text="❌ Thoát", font=("Arial", 12), command=thoat)
btn_thoat.pack(side=tk.LEFT, padx=10)

# Chạy giao diện
root.mainloop()
