import os
import shutil

from DataAccess.user_model import UserModel
from View.home_view import HomeView
from View.login_view import LoginView
from DataAccess.university_model import UniversityModel
from View.registration_view import RegistrationView


def save_image_to_project(image_path: str, destination_folder: str, new_name: str):
    # Kiểm tra xem đường dẫn ảnh có tồn tại không
    if not isinstance(image_path, str) or not os.path.exists(image_path):
        raise ValueError(f"Ảnh không tồn tại hoặc không phải đường dẫn hợp lệ: {image_path}")

    # Kiểm tra xem thư mục đích có tồn tại không, nếu không thì tạo
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Lấy phần mở rộng của ảnh (ví dụ: .jpg, .png)
    file_extension = os.path.splitext(image_path)[1]

    # Tạo đường dẫn đích với tên mới
    destination_path = os.path.join(destination_folder, new_name + file_extension)

    # Sao chép ảnh đến thư mục đích
    shutil.copy(str(image_path), str(destination_path))  # Đảm bảo mọi tham số đều là kiểu str
    print(f"Đã lưu ảnh tại: {destination_path}")
    return True


class AddSchoolController:
    def __init__(self, root, view):
        self.root = root
        self.model = UniversityModel()
        self.dbUser = UserModel()
        self.view = view

    def get_data(self):
        # Lấy dữ liệu từ model
        return self.model.get_all_universities()

    def add_university(self, name, location, region, focus, country_fee, global_fee, SAT, TOEFL, description, idUser, image):
        # Xử lý sự kiện khi nhấn vào item
        try:
            print(name, location, region, focus
                  , country_fee, global_fee, SAT, TOEFL, description, idUser)
            cleaned_path = image.strip().strip("\u202a").strip("\u202c")
            source_image = cleaned_path.replace("\\", "/")
            source_image = os.path.normpath(source_image)
            destination_folder = "./Image"
            new_image_name = f"{len(self.get_data()+1)}"
            save_image_to_project(source_image, destination_folder, new_image_name)
            idAdmin = self.dbUser.get_idAdmin(idUser)
            self.model.add_university(name, location, region, focus
                                      , country_fee, global_fee, SAT, TOEFL, description, idAdmin)
            return True
        except Exception as e:
            print(e)
            return False

    def display_view(self):
        self.view.show()

    def logout(self):
        from Controller.home_controller import HomeController
        from Tmp.user import set_userId
        set_userId(-1)

        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        regis_view = HomeView(self.root, None)  # Ban đầu không truyền Controller
        regis_controller = HomeController(self.root, regis_view)
        regis_view.controller = regis_controller
        self.view = regis_view
        self.display_view()
