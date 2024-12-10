import mysql.connector


class UniversityModel:
    def __init__(self):
        # Kết nối đến cơ sở dữ liệu MySQL
        self.conn = mysql.connector.connect(
            host="localhost",          # Thay bằng địa chỉ server MySQL
            user="root",      # Thay bằng username của bạn
            password="13092003aA@",  # Thay bằng mật khẩu của bạn
            database="universitymanagement"  # Tên cơ sở dữ liệu
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Tạo bảng nếu chưa tồn tại
        query = """
        CREATE TABLE IF NOT EXISTS university (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            location VARCHAR(255) NOT NULL
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def get_all_universities(self):
        # Lấy tất cả các trường
        query = "SELECT * FROM university"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_universities_by_user(self, idUser):
        # Lấy tất cả các trường
        query = "SELECT * FROM university WHERE idAdmin = %s"
        self.cursor.execute(query, (idUser, ))
        result = self.cursor.fetchone()
        self.cursor.fetchall()
        return result

    def add_university(self, name, location, region, focus, country_fee, global_fee, SAT, TOEFL, description, idUser):
        # Thêm một trường mới
        query = ("INSERT INTO `universitymanagement`.`university` (`nameUniversity`, `location`, `region`, `size`, "
                 "`focus`, `res`, `status`, `academicReputation`, `employerReputation`, `facultyStudent`, "
                 "`citationsPerFaculty`, `internationalFaculty`, `internationalStudents`, "
                 "`internationalResearchNetwork`, `employeeOutcomes`, `sustainability`, `domesticStudentsFee`, "
                 "`internationalStudentsFee`, `SAT`, `TOEFL`, `description`, `idAdmin`) VALUES (%s, %s, %s, "
                 "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                 "%s);")
        self.cursor.execute(query, (name, location, region, "M", focus, "MD", "A", 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    country_fee, global_fee, SAT, TOEFL, description, idUser))
        self.conn.commit()


# Sử dụng class
if __name__ == "__main__":
    model = UniversityModel()

    # Thêm một trường mới
    # model.add_university("University A", "New York")
    # model.add_university("University B", "California")

    # Lấy và in danh sách các trường
    universities = model.get_all_universities()
    for uni in universities:
        print(uni)
