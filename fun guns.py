from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget
)
from PySide6.QtCore import Qt
import sys


#==============================================
# FUN GUN MENU
#==============================================

class FunGunMenu(QStackedWidget):

    def __init__(self):
        super().__init__()
        self.selected_fungun = None
        self.setWindowTitle("CHOOSE YOUR FUN GUN!")

#==============================================
# FUN GUN SELECTION PAGE 
#==============================================


        self.waterfun_widget = QWidget()
        self.waterfun_layout = QVBoxLayout(self.waterfun_widget)

        self.waterfungun_button = QPushButton("Water Fun Gun")
        self.waterfungun_button.clicked.connect(
            lambda: self.select_fungun("Water Fun Gun")
        )

        self.waterfun_layout.addWidget(self.waterfungun_button)

        #==============================================
        # CONFIRMATION PAGE
        #==============================================

        self.confirm_widget = QWidget()
        self.confirm_layout = QVBoxLayout(self.confirm_widget)

        self.selected_label = QLabel("")
        self.selected_label.setAlignment(Qt.AlignCenter)

        self.confirm_button = QPushButton("CONFIRM")

        self.confirm_button.clicked.connect(self.confirm_fungun)

        self.confirm_layout.addWidget(self.selected_label)
        self.confirm_layout.addWidget(self.confirm_button)

        self.addWidget(self.confirm_widget)

    def confirm_fungun(self):

        print(f"Confirmed Fun Gun: {self.selected_fungun}")


#==============================================
# SELECT FUN GUN
#==============================================
    
    def select_fungun(self, fungun_name):

        self.selected_fungun = fungun_name

        self.selected_label.setText(
            f"YOU CHOSE:\n{fungun_name}"
        )

        self.setCurrentWidget(self.confirm_widget)




#==============================================
# EXIT 
#==============================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    menu = FunGunMenu()
    menu.show()

    sys.exit(app.exec())
    
