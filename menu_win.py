from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel

card_width, card_height = 600, 500
menu_card = QWidget()
menu_card.resize(card_width, card_height)
menu_card.move(0,0)
menu_card.setWindowTitle("Memory card")

menu_card.hide()
