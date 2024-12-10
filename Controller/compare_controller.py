from View.home_view import HomeView
from View.login_view import LoginView
from DataAccess.university_model import UniversityModel
from View.registration_view import RegistrationView


class CompareController:
    def __init__(self, root, view):
        self.root = root
        self.model = UniversityModel()
        self.view = view

    def display_view(self):
        self.view.show()

    def login(self):
        from Controller.login_controller import LoginController
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        login_view = LoginView(self.root, None)  # Ban đầu không truyền Controller
        login_controller = LoginController(self.root, login_view)
        login_view.controller = login_controller
        self.view = login_view
        self.display_view()

    def regis(self):
        from Controller.registration_controller import RegistrationController
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        regis_view = RegistrationView(self.root, None)  # Ban đầu không truyền Controller
        regis_controller = RegistrationController(self.root, regis_view)
        regis_view.controller = regis_controller
        self.view = regis_view
        self.display_view()