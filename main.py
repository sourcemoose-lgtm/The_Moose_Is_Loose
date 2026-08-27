import sys
from kart_selecter import KartMenu
import ModesMenu

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)


class SpeedemonButton(QPushButton):
    """A concrete button type for character selection with a useful action."""

    def __init__(self, label, selection_callback=None, parent=None):
        super().__init__(label, parent)
        self.selection_callback = selection_callback
        self.clicked.connect(self.handle_click)

    def handle_click(self):
        if self.selection_callback is not None:
            self.selection_callback(self.text())
        else:
            print(f"Selected character: {self.text()}")


class HeavyDemonButton(QPushButton):
    """A concrete button type for a heavy demon selection with a useful action."""

    def __init__(self, label, selection_callback=None, parent=None):
        super().__init__(label, parent)
        self.selection_callback = selection_callback
        self.clicked.connect(self.handle_click)

    def handle_click(self):
        if self.selection_callback is not None:
            self.selection_callback(self.text())
        else:
            print(f"Selected character: {self.text()}")


# ============================================================
# MAIN MENU
# ============================================================

class MooseMenu(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("The Moose Is Loose!")
        self.setMinimumSize(900, 600)

        layout = QVBoxLayout()

        title = QLabel("THE MOOSE IS LOOSE!")

        self.play_button = QPushButton("PLAY DEMO")
        self.settings_button = QPushButton("SETTINGS")
        self.quit_button = QPushButton("QUIT")

        layout.addWidget(title)
        layout.addWidget(self.play_button)
        layout.addWidget(self.settings_button)
        layout.addWidget(self.quit_button)

        self.setLayout(layout)

        # Button connections
        self.play_button.clicked.connect(self.open_roster)
        self.quit_button.clicked.connect(QApplication.quit)

        # Main menu styling
        self.setStyleSheet("""
            QWidget {
                background-color: #09060b;
                color: #f4edf5;
            }

            QLabel {
                color: #f4c43c;
                font-size: 48px;
                font-weight: bold;
            }

            QPushButton {
                background-color: #25122b;
                color: #f4edf5;
                border: 1px solid #6f3675;
                padding: 15px;
                font-size: 16px;
                border-radius: 8px;
            }

            QPushButton:hover {
                background-color: #7d397e;
                border: 1px solid #f4c43c;
            }

            QPushButton:pressed {
                background-color: #f4c43c;
                color: #09060b;
            }
        """)

    # ========================================================
    # UNIVERSE SELECTION
    # ========================================================

    def open_roster(self):

        # Clear the current menu
        for child in self.findChildren(QPushButton):
            child.hide()

        # Change title
        title = self.findChild(QLabel)
        title.setText("CHOOSE YOUR REALITY!")

        # Moose Reality button
        self.moose_reality_button = QPushButton("THE MOOSE IS LOOSE!")
        self.moose_reality_button.clicked.connect(self.open_moose_roster)

        # Bridged Saga - Part 1  button
        self.bridged_saga_button = QPushButton("THE BRIDGED SAGA - Part 1")
        self.bridged_saga_button.clicked.connect(self.open_bridged_roster)

        # Back button
        self.back_button = QPushButton("BACK")
        self.back_button.clicked.connect(self.return_to_main_menu)

        self.layout().addWidget(self.moose_reality_button)
        self.layout().addWidget(self.bridged_saga_button)
        self.layout().addWidget(self.back_button)

    # ========================================================
    # MOOSE REALITY ROSTER
    # ========================================================

    def open_moose_roster(self):

        self.clear_roster()

        title = self.findChild(QLabel)
        title.setText("THE MOOSE IS LOOSE!")

        self.moose_button = QPushButton("Moose")
        self.blue_moose_button = QPushButton("Blue Moose")
        self.differentcoloured_moose_button = QPushButton("Different Coloured Moose")

        # Create sub menu here 

        self.redmoose_button = QPushButton ("Red Moose")
        self.greenmoose_button = QPushButton ( "Green Moose")
        self.auberginemoose_button = QPushButton (" Aubergine Moose")

        self.moose_button.clicked.connect(
            lambda: self.select_character("Moose")
        )

        self.blue_moose_button.clicked.connect(
            lambda: self.select_character("Blue Moose")
        )

        self.differentcoloured_moose_button.clicked.connect(
            lambda: self.open_differentcoloured_moose
        )

        self.redmoose_button.clicked.connect(
            lambda: self.open_red_moose 
        )

        self.greenmoose_button.clicked.connect(
            lambda: self.open_green_moose()
        )



        self.back_button = QPushButton("BACK")
        self.back_button.clicked.connect(self.open_roster)

        self.layout().addWidget(self.moose_button)
        self.layout().addWidget(self.blue_moose_button)
        self.layout().addWidget(self.differentcoloured_moose_button)
        self.layout().addWidget(self.back_button)
        

    

    def open_green_moose(self):

        self.clear_roster()

        title = self.findChild(QLabel)
        title.setText("GREEN MOOSE")

        self.green_moose_button = QPushButton("Green Moose")
        self.even_more_green_moose_button = QPushButton("Emerald Moose")
        self.back_button = QPushButton("BACK")

        self.green_moose_button.clicked.connect(
            lambda: self.select_character("Green Moose")
        )

        self.even_more_green_moose_button.clicked.connect(
            lambda: self.select_character("Emerald Moose")
        )

        self.back_button.clicked.connect(self.open_moose_roster)

        self.layout().addWidget(self.green_moose_button)
        self.layout().addWidget(self.emerald_moose_button)
        self.layout().addWidget(self.back_button)

    # ========================================================
    # THE BRIDGED SAGA ROSTER
    # ========================================================

    def open_bridged_roster(self):

        self.clear_roster()

        title = self.findChild(QLabel)
        title.setText("THE BRIDGED SAGA")

        self.jack_button = QPushButton("Jack Drummond")
        self.aria_button = QPushButton("Aria Drummond")
        self.luka_button = QPushButton("Luka Drummond")
        self.speedemon_button = QPushButton("Speed Demon")
        self.heavydemon_button = QPushButton("Heavy Demon")
        self.ghost_button = QPushButton("Ghost")

        self.jack_button.clicked.connect(
            lambda: self.select_character("Jack Drummond")
        )

        self.aria_button.clicked.connect(
            lambda: self.select_character("Aria Drummond")
        )

        self.luka_button.clicked.connect(
            lambda: self.select_character("Luka Drummond")
        )

        self.speeddemon_button.clicked.conncet(
            lambda: self.select_character("Speed Demon")
        )

        self.heavydemon_button.clicked.connect(
            lambda: self.select_character("Heavy Demon")
        )

        self.gohst_button.clicked.connect(
            lambda: self.select_character("Ghost")
        )

        self.back_button = QPushButton("BACK")
        self.back_button.clicked.connect(self.open_roster)

        self.layout().addWidget(self.jack_button)
        self.layout().addWidget(self.aria_button)
        self.layout().addWidget(self.luka_button)
        self.layout().addWidget(self.speedemon_button)
        self.layout().addWidget(self.heavydemon_button)
        self.layout().addWidget(self.ghost_button)
        self.layout().addWidget(self.back_button)


    # ========================================================
    # CLEAR CURRENT ROSTER
    # ========================================================

    def clear_roster(self):

        for button in self.findChildren(QPushButton):
            button.deleteLater()

    #========================================================
    # Kart and Bike menu 
    #========================================================

    def open_kartandbikemenu(self):

        self.clear_roster()

        title = QLabel("KART AND BIKE MENU")
        self.layout().addWidget(title)

        kart_button = QPushButton("KARTS")
        bike_button = QPushButton("BIKES")

        self.layout().addWidget(kart_button)
        self.layout().addWidget(bike_button)

    # ========================================================
    # RETURN TO MAIN MENU
    # ========================================================

    def return_to_main_menu(self):

        self.close()

        self.new_window = MooseMenu()
        self.new_window.show()


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MooseMenu()
    window.show()

    sys.exit(app.exec())
