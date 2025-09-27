from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem, QCheckBox, QMessageBox
from PyQt5.QtGui import QFont

app = QApplication([])
List = QWidget()
List.setWindowTitle("CREATING TO-DO LIST")
List.setFixedSize(720,680)
title = QLabel("TO-DO LIST")
title.setFont(QFont("Times New Roman", 36, QFont.Bold))
button1 = QPushButton("ADD")
button1.setStyleSheet("""
    QPushButton {
        font-size: 18px;
        font-family: Times New Roman;
        font-weight: bold;
        background-color: #f0f0f0;
        border: 1px solid gray;
        border-radius: 6px;
        padding: 6px;
    }
    QPushButton:hover {
        background-color: #00ffff;
    }
    QPushButton:pressed {
        background-color: #000000;
        color: #ffffff;
    }
""")
button2 = QPushButton("Delete")
button2.setStyleSheet("""
    QPushButton {
        font-size: 18px;
        font-family: Times New Roman;
        font-weight: bold;
        background-color: #f0f0f0;
        border: 1px solid gray;
        border-radius: 6px;
        padding: 6px;
    }
    QPushButton:hover {
        background-color: #00ffff;
    }
    QPushButton:pressed {
        background-color: #000000;
        color: #ffffff;
    }
""")
button3 = QPushButton("EXPORT TO TXT")

button3.setStyleSheet("""
    QPushButton {
        font-size: 18px;
        font-family: Times New Roman;
        font-weight: bold;
        background-color: #f0f0f0;
        border: 1px solid gray;
        border-radius: 6px;
        padding: 6px;
    }
    QPushButton:hover {
        background-color: #00ffff;
    }
    QPushButton:pressed {
        background-color: #000000;
        color: #ffffff;
    }
""")
task_list = QListWidget()

line1 = QVBoxLayout()
line1.addWidget(title, alignment = Qt.AlignCenter)

line2 = QHBoxLayout()
line2.addWidget(button1, alignment = Qt.AlignLeft)
line2.addWidget(button2, alignment = Qt.AlignRight)\

line3 = QVBoxLayout()
line3.addWidget(task_list)

line4 = QVBoxLayout()
line4.addWidget(button3, alignment = Qt.AlignRight)

line5 = QVBoxLayout()
line5.addLayout(line1)
line5.addLayout(line2)
line5.addLayout(line3)
line5.addLayout(line4)

List.setLayout(line5)

def AddText() :
    row_widget = QWidget()
    row_layout = QHBoxLayout()
    row_layout.setContentsMargins(5, 5, 5, 5)
    row_layout.setSpacing(10)

    checkbox = QCheckBox()

    item = QLineEdit()
    item.setPlaceholderText("Enter task...")
    row_layout.addWidget(checkbox)
    row_layout.addWidget(item)
    row_widget.setLayout(row_layout)
    new_item = QListWidgetItem(task_list)
    new_item.setSizeHint(row_widget.sizeHint())
    task_list.setItemWidget(new_item, row_widget)

def DeleteText() :
    for i in range(task_list.count() - 1, -1, -1) :
        item = task_list.item(i)
        row_widget = task_list.itemWidget(item)
        if row_widget :
            checkbox = row_widget.findChild(QCheckBox)
            if checkbox and checkbox.isChecked() :
                task_list.takeItem(i)

def ExportText() :
    with open("TO DO LIST.txt", "a") as f :
        for i in range(task_list.count()) :
            item = task_list.item(i)
            row_widget = task_list.itemWidget(item)
            if row_widget :
                checkbox = row_widget.findChild(QCheckBox)
                lineedit = row_widget.findChild(QLineEdit)
                if checkbox and checkbox.isChecked() and lineedit :
                    text = lineedit.text().strip()
                    f.write(text + "\n")
    message = QMessageBox()
    message.setText("Your List Are Added")
    message.exec_()


button1.clicked.connect(AddText)
button2.clicked.connect(DeleteText)
button3.clicked.connect(ExportText)

List.show()
app.exec_()