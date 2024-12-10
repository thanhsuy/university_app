from PIL import Image
import customtkinter as ctk

from DataAccess.university_model import UniversityModel
from DataAccess.user_model import UserModel


class HomeAdminView:
    def __init__(self, root, controller):
        from Tmp.user import userId
        from Tmp.university import university

        self.root = root
        self.controller = controller
        self.dbUser = UserModel()
        self.dbUniversity = UniversityModel()

        university = university
        try:
            image = Image.open(f"Image/{university[0]}.webp")
        except Exception:
            image = Image.open("1.jpg")
        image = image.resize((150, 150))
        photo = ctk.CTkImage(light_image=image, dark_image=image, size=(150, 150))

        # Thanh điều hướng trên cùng
        self.navbar = ctk.CTkFrame(root, height=50, corner_radius=0, fg_color="#444")
        self.navbar.pack(fill="x")

        buttons = ["Quản lý trường", "So sánh", "Chat bot"]

        self.butXepHang = ctk.CTkButton(self.navbar, text=buttons[0], width=100, fg_color="orange")
        self.butXepHang.pack(side="left", padx=10)

        self.butSoSanh = ctk.CTkButton(self.navbar, text=buttons[1], width=100, fg_color="#555", hover_color="#666")
        self.butSoSanh.pack(side="left", padx=10)

        self.butChatBot = ctk.CTkButton(self.navbar, text=buttons[2], width=100, fg_color="#555", hover_color="#666")
        self.butChatBot.pack(side="left", padx=10)

        self.butLogout = ctk.CTkButton(self.navbar, text="Đăng xuất", width=80, fg_color="orange", command=self.logout)
        self.butLogout.pack(side="right", padx=5)

        username = self.dbUser.get_username(userId)
        self.usernameLabel = ctk.CTkLabel(self.navbar, text=f"Xin chào {username}", width=80, fg_color="#444",
                                          text_color="white")
        self.usernameLabel.pack(side="right", padx=5)

        # Khu vực nội dung
        self.content_frame = ctk.CTkFrame(root, fg_color="#E0E0E0", corner_radius=10)
        self.content_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Thông tin trường học
        ctk.CTkLabel(
            self.content_frame,
            text="Trường học của bạn:",
            font=("Arial", 18, "bold"),
            anchor="w",
        ).grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=10)

        # Ảnh trường học
        ctk.CTkLabel(self.content_frame, image=photo, text="").grid(
            row=1, column=0, rowspan=3, padx=10, pady=10, sticky="w"
        )

        self.entry_ten_truong = ctk.CTkEntry(self.content_frame)
        self.entry_ten_truong.insert(ctk.END, university[1])
        self.entry_ten_truong.configure(state="disabled")

        self.entry_quoc_gia = ctk.CTkEntry(self.content_frame)
        self.entry_quoc_gia.insert(ctk.END, university[2])
        self.entry_quoc_gia.configure(state="disabled")

        self.entry_khu_vuc = ctk.CTkEntry(self.content_frame)
        self.entry_khu_vuc.insert(ctk.END, university[3])
        self.entry_khu_vuc.configure(state="disabled")

        self.entry_mo_ta = ctk.CTkEntry(self.content_frame)
        self.entry_mo_ta.insert(ctk.END, university[33])
        self.entry_mo_ta.configure(state="disabled")

        self.entry_hoc_phi1 = ctk.CTkEntry(self.content_frame)
        if university[17]:
            self.entry_hoc_phi1.insert(ctk.END, university[17])
        self.entry_hoc_phi1.configure(state="disabled")

        self.entry_hoc_phi2 = ctk.CTkEntry(self.content_frame)
        if university[18]:
            self.entry_hoc_phi2.insert(ctk.END, university[18])
        self.entry_hoc_phi2.configure(state="disabled")

        self.entry_yeu_cau1 = ctk.CTkEntry(self.content_frame)
        if university[19]:
            self.entry_yeu_cau1.insert(ctk.END, university[19])
        self.entry_yeu_cau1.configure(state="disabled")

        self.entry_yeu_cau2 = ctk.CTkEntry(self.content_frame)
        if university[20]:
            self.entry_yeu_cau2.insert(ctk.END, university[20])
        self.entry_yeu_cau2.configure(state="disabled")

        self.entry_muc_do = ctk.CTkEntry(self.content_frame)
        if university[5] == "CO":
            self.entry_muc_do.insert(ctk.END, "Comprehensive")
        elif university[5] == "FC":
            self.entry_muc_do.insert(ctk.END, "Full Comprehensive")
        elif university[5] == "FO":
            self.entry_muc_do.insert(ctk.END, "Focused")
        elif university[5] == "SP":
            self.entry_muc_do.insert(ctk.END, "Specialist")
        self.entry_muc_do.configure(state="disabled")

        # Thêm nhãn và các ô nhập liệu tương ứng
        ctk.CTkLabel(self.content_frame, text="Tên trường:", font=("Arial", 14, "bold")).grid(
            row=1, column=1, sticky="w", padx=10, pady=5
        )
        self.entry_ten_truong.grid(row=1, column=2, columnspan=2, sticky="we", padx=10, pady=5)

        ctk.CTkLabel(self.content_frame, text="Quốc gia:", font=("Arial", 14, "bold")).grid(
            row=2, column=1, sticky="w", padx=10, pady=5
        )
        self.entry_quoc_gia.grid(row=2, column=2, sticky="we", padx=10, pady=5)

        ctk.CTkLabel(self.content_frame, text="Khu vực:", font=("Arial", 14, "bold")).grid(
            row=3, column=1, sticky="w", padx=10, pady=5
        )
        self.entry_khu_vuc.grid(row=3, column=2, sticky="we", padx=10, pady=5)

        ctk.CTkLabel(self.content_frame, text="Mô tả:", font=("Arial", 14, "bold")).grid(
            row=4, column=0, sticky="w", padx=10, pady=5
        )
        self.entry_mo_ta.grid(row=4, column=1, columnspan=4, sticky="we", padx=10, pady=5)

        # Học phí và yêu cầu đầu vào - Tách thành hai ô liền kề
        ctk.CTkLabel(self.content_frame, text="Học phí:", font=("Arial", 14, "bold")).grid(
            row=5, column=0, sticky="w", padx=10, pady=5
        )
        self.entry_hoc_phi1.grid(row=5, column=1, sticky="we", padx=10, pady=5)
        self.entry_hoc_phi2.grid(row=6, column=1, sticky="we", padx=10, pady=5)

        ctk.CTkLabel(self.content_frame, text="Yêu cầu đầu vào:", font=("Arial", 14, "bold")).grid(
            row=5, column=2, sticky="w", padx=10, pady=5
        )
        self.entry_yeu_cau1.grid(row=5, column=3, sticky="we", padx=10, pady=5)
        self.entry_yeu_cau2.grid(row=6, column=3, sticky="we", padx=10, pady=5)

        # Mức độ tập trung chuyên ngành
        ctk.CTkLabel(self.content_frame, text="Mức độ tập trung chuyên ngành:", font=("Arial", 14, "bold")).grid(
            row=7, column=0, sticky="w", padx=10, pady=5
        )
        self.entry_muc_do.grid(row=7, column=1, columnspan=2, sticky="we", padx=10, pady=5)

        # Nút "Chỉnh sửa"
        edit_button = ctk.CTkButton(
            self.content_frame, text="Chỉnh sửa", fg_color="orange", command=self.edit_info
        )
        edit_button.grid(row=8, column=1, columnspan=2, pady=30)

        # Cấu hình lưới
        self.content_frame.grid_rowconfigure(4, weight=1)
        self.content_frame.grid_columnconfigure(2, weight=1)  # Các trường nhập liệu mở rộng

    def show(self):
        # Cập nhật giao diện nếu cần thiết
        pass

    def edit_info(self):
        self.controller.edit_university()

    def logout(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.logout()
