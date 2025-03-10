from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QRadioButton, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox
)
import sys

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Week 2: Layout - User Registration Form")
        self.setGeometry(100, 100, 400, 300)

        main_layout = QVBoxLayout()

        identity_group = QGroupBox("Identitas")
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama : Rafli"))
        identity_layout.addWidget(QLabel("NIM  : F1D022022"))
        identity_layout.addWidget(QLabel("Kelas: D"))
        identity_group.setLayout(identity_layout)

        nav_group = QGroupBox("Navigation")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)

        form_group = QGroupBox("User Registration")
        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.gender_male = QRadioButton("Male")
        self.gender_female = QRadioButton("Female")
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.gender_male)
        gender_layout.addWidget(self.gender_female)
        self.country_combo = QComboBox()
        self.country_combo.addItems(["Indonesia", "Malaysia", "Singapore", "Thailand"])

        form_layout.addRow("Full Name:", self.name_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Phone:", self.phone_input)
        form_layout.addRow("Gender:", gender_layout)
        form_layout.addRow("Country:", self.country_combo)
        form_group.setLayout(form_layout)

        action_group = QGroupBox("Actions")
        action_layout = QHBoxLayout()
        submit_button = QPushButton("Submit")
        cancel_button = QPushButton("Cancel")
        action_layout.addWidget(submit_button)
        action_layout.addWidget(cancel_button)
        action_group.setLayout(action_layout)

        main_layout.addWidget(identity_group)
        main_layout.addWidget(nav_group)
        main_layout.addWidget(form_group)
        main_layout.addWidget(action_group)

        self.setLayout(main_layout)
        self.setStyleSheet(self.load_styles())

    def load_styles(self):
        return """
        QWidget {
            font-size: 14px;
        }
        QGroupBox {
            font-weight: bold;
            border: 1px solid gray;
            border-radius: 5px;
            margin-top: 10px;
            padding: 10px;
        }
        QPushButton {
            background-color: #4CAF50;
            color: white;
            padding: 5px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())
