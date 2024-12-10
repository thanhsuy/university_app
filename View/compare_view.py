import customtkinter as ctk


class CompareView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Thanh điều hướng
        self.navbar = ctk.CTkFrame(root, height=50, corner_radius=0, fg_color="#444")
        self.navbar.pack(fill="x")

        # Nút điều hướng
        self.butXepHang = ctk.CTkButton(self.navbar, text="Xếp hạng", width=100, fg_color="#555", hover_color="#666")
        self.butXepHang.pack(side="left", padx=10)

        self.butSoSanh = ctk.CTkButton(self.navbar, text="So sánh", width=100, fg_color="orange", hover_color="#666")
        self.butSoSanh.pack(side="left", padx=10)

        self.butChatBot = ctk.CTkButton(self.navbar, text="Chat bot", width=100, fg_color="#555", hover_color="#666")
        self.butChatBot.pack(side="left", padx=10)

        self.butLogin = ctk.CTkButton(self.navbar, text="Đăng nhập", width=80, fg_color="orange")
        self.butLogin.pack(side="right", padx=5)

        self.butRegister = ctk.CTkButton(self.navbar, text="Đăng ký", width=80, fg_color="orange")
        self.butRegister.pack(side="right", padx=5)

        # Thanh tìm kiếm
        self.search_frame = ctk.CTkFrame(root, height=50)
        self.search_frame.pack(fill="x", pady=10, padx=10)

        # Hai ô tìm kiếm
        self.search_entry_1 = ctk.CTkEntry(self.search_frame, placeholder_text="Nhập giá trị 1")
        self.search_entry_1.pack(side="left", fill="x", expand=True, padx=10)

        self.search_entry_2 = ctk.CTkEntry(self.search_frame, placeholder_text="Nhập giá trị 2")
        self.search_entry_2.pack(side="left", fill="x", expand=True, padx=10)

        # Khu vực nội dung chính
        self.content_frame = ctk.CTkFrame(root, height=300, bg_color="gray")
        self.content_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Hàng nút chỉ số
        self.indicator_frame1 = ctk.CTkFrame(root, height=50)
        self.indicator_frame1.pack(fill="x", pady=10)

        self.indicator_frame2 = ctk.CTkFrame(root, height=50)
        self.indicator_frame2.pack(fill="x", pady=10)

        # Các nút "Chỉ số 1"
        for i in range(5):  # Hiển thị 8 nút
            ctk.CTkButton(self.indicator_frame1, text=f"Chỉ số 1", fg_color="orange", width=115).pack(side="left", padx=15)

        for i in range(5):  # Hiển thị 8 nút
            ctk.CTkButton(self.indicator_frame2, text=f"Chỉ số 1", fg_color="orange", width=115).pack(side="left", padx=15)

    def show(self):
        # Hiển thị thông báo nếu cần (có thể mở rộng)
        pass

    def login(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.login()

    def regis(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.regis()


