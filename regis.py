from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QRadioButton, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox,
    QCheckBox, QDateEdit, QMessageBox, QTabWidget, QProgressBar, QSlider
)
from PyQt6.QtGui import QIcon, QPixmap, QFont, QColor
from PyQt6.QtCore import Qt, QDate
import sys

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("✨ Interactive User Registration Form")
        self.setGeometry(100, 100, 550, 600)

        # Tab widget untuk navigasi yang lebih baik
        self.tab_widget = QTabWidget()
        
        # Tab untuk data pribadi
        self.personal_tab = QWidget()
        self.create_personal_tab()
        self.tab_widget.addTab(self.personal_tab, "👤 Personal Info")
        
        # Tab untuk preferensi
        self.preferences_tab = QWidget()
        self.create_preferences_tab()
        self.tab_widget.addTab(self.preferences_tab, "⚙️ Preferences")
        
        # Tab untuk konfirmasi
        self.confirmation_tab = QWidget()
        self.create_confirmation_tab()
        self.tab_widget.addTab(self.confirmation_tab, "✓ Confirmation")
        
        # Layout utama
        main_layout = QVBoxLayout()
        
        # Header dengan logo
        header_layout = QHBoxLayout()
        logo_label = QLabel()
        logo_label.setFixedSize(80, 80)

        # Gunakan placeholder untuk logo
        logo_label.setText("🌟 LOGO")
        logo_label.setStyleSheet("background-color: #1976D2; color: white; border-radius: 10px; font-size: 16px; font-weight: bold; padding: 5px;")
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        title_label = QLabel("Interactive Registration System")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #0D47A1;")
        
        header_layout.addWidget(logo_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        # Progress indicator
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(33)  # Tab pertama = 33%
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFormat("Progress: %p%")
        
        # Connect tab change dengan progress bar
        self.tab_widget.currentChanged.connect(self.update_progress)

        # Menambahkan semua bagian ke layout utama
        main_layout.addLayout(header_layout)
        main_layout.addWidget(QLabel("Complete all tabs to finish registration"))
        main_layout.addWidget(self.progress_bar)
        main_layout.addWidget(self.tab_widget)
        
        # Footer dengan identitas
        footer_group = QGroupBox("👤 Student Information")
        footer_layout = QHBoxLayout()
        footer_layout.addWidget(QLabel("📛 Nama : nama_anda"))
        footer_layout.addWidget(QLabel("🎓 NIM  : nim_anda"))
        footer_layout.addWidget(QLabel("🏫 Kelas: kelas_anda"))
        footer_group.setLayout(footer_layout)
        main_layout.addWidget(footer_group)
        
        # Action buttons
        action_layout = QHBoxLayout()
        self.back_btn = QPushButton("⬅️ Back")
        self.next_btn = QPushButton("Next ➡️")
        self.submit_btn = QPushButton("✅ Submit Registration")
        self.submit_btn.setVisible(False)
        
        self.back_btn.clicked.connect(self.go_back)
        self.next_btn.clicked.connect(self.go_next)
        self.submit_btn.clicked.connect(self.submit_form)
        
        action_layout.addWidget(self.back_btn)
        action_layout.addStretch()
        action_layout.addWidget(self.next_btn)
        action_layout.addWidget(self.submit_btn)
        
        main_layout.addLayout(action_layout)

        self.setLayout(main_layout)
        self.setStyleSheet(self.load_styles())
        
        # Inisialisasi state tombol
        self.update_button_state()

    def create_personal_tab(self):
        layout = QVBoxLayout()
        
        # Formulir pendaftaran dengan placeholder
        form_group = QGroupBox("📋 Personal Information")
        form_layout = QFormLayout()
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your full name...")
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email address...")
        
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter your phone number...")
        
        # Gender dengan radio button yang lebih menarik
        gender_group = QGroupBox("Gender")
        gender_layout = QHBoxLayout()
        self.gender_male = QRadioButton("👨 Male")
        self.gender_female = QRadioButton("👩 Female")
        self.gender_other = QRadioButton("⚧️ Other")
        gender_layout.addWidget(self.gender_male)
        gender_layout.addWidget(self.gender_female)
        gender_layout.addWidget(self.gender_other)
        gender_group.setLayout(gender_layout)
        
        # Tanggal lahir
        self.birth_date = QDateEdit()
        self.birth_date.setDisplayFormat("dd MMMM yyyy")
        self.birth_date.setCalendarPopup(True)
        self.birth_date.setDate(QDate.currentDate().addYears(-20))  # Default 20 tahun lalu
        
        # Dropdown country yang lebih menarik dengan ikon
        self.country_combo = QComboBox()
        self.country_combo.addItems([
            "🇮🇩 Indonesia", 
            "🇲🇾 Malaysia", 
            "🇸🇬 Singapore", 
            "🇹🇭 Thailand",
            "🇯🇵 Japan",
            "🇰🇷 South Korea",
            "🇺🇸 United States",
            "🇦🇺 Australia"
        ])
        
        form_layout.addRow("📝 Full Name:", self.name_input)
        form_layout.addRow("📧 Email:", self.email_input)
        form_layout.addRow("📞 Phone:", self.phone_input)
        form_layout.addRow("⚤ Gender:", gender_group)
        form_layout.addRow("🎂 Birth Date:", self.birth_date)
        form_layout.addRow("🌎 Country:", self.country_combo)
        
        form_group.setLayout(form_layout)
        layout.addWidget(form_group)
        
        # Tips
        tips_label = QLabel("💡 Tips: Make sure to use a valid email address for verification.")
        tips_label.setStyleSheet("font-style: italic; color: #555;")
        layout.addWidget(tips_label)
        
        layout.addStretch()
        self.personal_tab.setLayout(layout)

    def create_preferences_tab(self):
        layout = QVBoxLayout()
        
        # Preferensi notifikasi
        notification_group = QGroupBox("🔔 Notification Preferences")
        notification_layout = QVBoxLayout()
        
        self.email_notify = QCheckBox("📧 Receive email notifications")
        self.sms_notify = QCheckBox("📱 Receive SMS notifications")
        self.promo_notify = QCheckBox("🎁 Receive promotional offers")
        
        notification_layout.addWidget(self.email_notify)
        notification_layout.addWidget(self.sms_notify)
        notification_layout.addWidget(self.promo_notify)
        
        notification_group.setLayout(notification_layout)
        
        # Tema aplikasi
        theme_group = QGroupBox("🎨 Application Theme")
        theme_layout = QVBoxLayout()
        
        self.theme_light = QRadioButton("☀️ Light Theme")
        self.theme_dark = QRadioButton("🌙 Dark Theme")
        self.theme_auto = QRadioButton("🔄 Auto (System Default)")
        
        self.theme_light.setChecked(True)
        
        theme_layout.addWidget(self.theme_light)
        theme_layout.addWidget(self.theme_dark)
        theme_layout.addWidget(self.theme_auto)
        
        theme_group.setLayout(theme_layout)
        
        # Font size slider
        font_group = QGroupBox("🔤 Font Size")
        font_layout = QVBoxLayout()
        
        self.font_slider = QSlider(Qt.Orientation.Horizontal)
        self.font_slider.setRange(10, 24)
        self.font_slider.setValue(14)
        self.font_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.font_slider.setTickInterval(2)
        
        self.font_size_label = QLabel("Current size: 14px")
        self.font_slider.valueChanged.connect(self.update_font_size_label)
        
        font_layout.addWidget(self.font_slider)
        font_layout.addWidget(self.font_size_label)
        
        font_group.setLayout(font_layout)
        
        layout.addWidget(notification_group)
        layout.addWidget(theme_group)
        layout.addWidget(font_group)
        layout.addStretch()
        
        self.preferences_tab.setLayout(layout)

    def create_confirmation_tab(self):
        layout = QVBoxLayout()
        
        # Summary
        summary_group = QGroupBox("📃 Registration Summary")
        summary_layout = QVBoxLayout()
        
        self.summary_label = QLabel("Please complete the previous tabs to see your registration summary.")
        self.summary_label.setWordWrap(True)
        
        summary_layout.addWidget(self.summary_label)
        summary_group.setLayout(summary_layout)
        
        # Terms and conditions
        terms_group = QGroupBox("📜 Terms and Conditions")
        terms_layout = QVBoxLayout()
        
        terms_text = QLabel(
            "By submitting this form, you agree to our Terms of Service and Privacy Policy. "
            "We will handle your personal information as described in our Privacy Policy."
        )
        terms_text.setWordWrap(True)
        
        self.terms_checkbox = QCheckBox("I agree to the Terms and Conditions")
        
        terms_layout.addWidget(terms_text)
        terms_layout.addWidget(self.terms_checkbox)
        
        terms_group.setLayout(terms_layout)
        
        # Final notes
        notes_label = QLabel(
            "Thank you for registering with our service! After submission, "
            "you will receive a confirmation email with further instructions."
        )
        notes_label.setWordWrap(True)
        notes_label.setStyleSheet("font-style: italic; color: #555;")
        
        layout.addWidget(summary_group)
        layout.addWidget(terms_group)
        layout.addWidget(notes_label)
        layout.addStretch()
        
        self.confirmation_tab.setLayout(layout)

    def update_progress(self, index):
        # Update progress bar based on current tab
        progress = (index + 1) * 100 // 3
        self.progress_bar.setValue(progress)
        
        # Update buttons
        self.update_button_state()
        
        # Update summary in confirmation tab if on last tab
        if index == 2:
            self.update_summary()

    def update_button_state(self):
        current_tab = self.tab_widget.currentIndex()
        
        # Back button visibility
        self.back_btn.setEnabled(current_tab > 0)
        
        # Next button visibility
        if current_tab == 2:  # Last tab
            self.next_btn.setVisible(False)
            self.submit_btn.setVisible(True)
        else:
            self.next_btn.setVisible(True)
            self.submit_btn.setVisible(False)

    def update_font_size_label(self, value):
        self.font_size_label.setText(f"Current size: {value}px")

    def update_summary(self):
        # Hanya menampilkan ringkasan jika memiliki nama
        if hasattr(self, 'name_input') and self.name_input.text():
            summary_text = f"""
            <h3>Registration Information:</h3>
            <p><b>Name:</b> {self.name_input.text() or "Not provided"}</p>
            <p><b>Email:</b> {self.email_input.text() or "Not provided"}</p>
            <p><b>Phone:</b> {self.phone_input.text() or "Not provided"}</p>
            <p><b>Country:</b> {self.country_combo.currentText()}</p>
            <p><b>Birth Date:</b> {self.birth_date.date().toString("dd MMMM yyyy")}</p>
            
            <h3>Preferences:</h3>
            <p><b>Email Notifications:</b> {"Yes" if self.email_notify.isChecked() else "No"}</p>
            <p><b>SMS Notifications:</b> {"Yes" if self.sms_notify.isChecked() else "No"}</p>
            <p><b>Theme:</b> {"Light" if self.theme_light.isChecked() else "Dark" if self.theme_dark.isChecked() else "Auto"}</p>
            """
            self.summary_label.setText(summary_text)

    def go_back(self):
        current_tab = self.tab_widget.currentIndex()
        if current_tab > 0:
            self.tab_widget.setCurrentIndex(current_tab - 1)

    def go_next(self):
        current_tab = self.tab_widget.currentIndex()
        if current_tab < self.tab_widget.count() - 1:
            self.tab_widget.setCurrentIndex(current_tab + 1)

    def submit_form(self):
        if not self.terms_checkbox.isChecked():
            QMessageBox.warning(self, "Terms Required", "You must agree to the Terms and Conditions to continue.")
            return
            
        if not self.name_input.text() or not self.email_input.text():
            QMessageBox.warning(self, "Incomplete Information", "Please provide at least your name and email address.")
            return
            
        QMessageBox.information(
            self, 
            "Registration Successful",
            f"Thank you, {self.name_input.text()}!\nYour registration was successful.\nA confirmation email has been sent to {self.email_input.text()}"
        )

    def load_styles(self):
        return """
        QWidget {
            font-size: 14px;
            font-family: 'Segoe UI', 'Arial', sans-serif;
            background-color: #f9f9f9;
        }
        QTabWidget::pane {
            border: 2px solid #3F51B5;
            border-radius: 8px;
            background-color: white;
        }
        QTabBar::tab {
            background-color: #E8EAF6;
            border: 1px solid #C5CAE9;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            padding: 8px 12px;
            margin-right: 4px;
        }
        QTabBar::tab:selected {
            background-color: #3F51B5;
            color: white;
            font-weight: bold;
        }
        QGroupBox {
            font-weight: bold;
            border: 2px solid #3F51B5;
            border-radius: 8px;
            margin-top: 12px;
            padding: 15px;
            background-color: white;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top center;
            padding: 0 10px;
            color: #3F51B5;
        }
        QLineEdit, QComboBox, QDateEdit {
            border: 2px solid #9FA8DA;
            border-radius: 5px;
            padding: 8px;
            background-color: #F5F5F5;
        }
        QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
            border-color: #3F51B5;
            background-color: #E8EAF6;
        }
        QPushButton {
            background-color: #3F51B5;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            font-weight: bold;
            font-size: 14px;
            min-width: 100px;
        }
        QPushButton:hover {
            background-color: #303F9F;
        }
        QPushButton:pressed {
            background-color: #1A237E;
        }
        QPushButton:disabled {
            background-color: #9E9E9E;
        }
        QRadioButton, QCheckBox {
            spacing: 8px;
            font-size: 14px;
        }
        QRadioButton:hover, QCheckBox:hover {
            color: #3F51B5;
        }
        QProgressBar {
            border: 2px solid #C5CAE9;
            border-radius: 5px;
            text-align: center;
            height: 20px;
        }
        QProgressBar::chunk {
            background-color: #3F51B5;
            border-radius: 5px;
        }
        QSlider::groove:horizontal {
            border: 1px solid #C5CAE9;
            height: 8px;
            background: #E8EAF6;
            margin: 2px 0;
            border-radius: 4px;
        }
        QSlider::handle:horizontal {
            background: #3F51B5;
            border: 1px solid #3F51B5;
            width: 18px;
            height: 18px;
            margin: -5px 0;
            border-radius: 9px;
        }
        QLabel {
            color: #212121;
        }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())