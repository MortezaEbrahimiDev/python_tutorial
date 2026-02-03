# imports and variables
import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QLabel,QLineEdit,QPushButton
from PyQt6.QtCore import QSize, Qt
# logics
def calculate_bmi():
    result = None
    w=float(weight_entry.text())
    h= float(height_entry.text())
    bmi=(w)/(h**2)

    if bmi<18.5:
        result= "Under weight"
    elif bmi<24.9:
        result= "Normal"
    elif bmi<29.9:
        result= "Over weight"
    elif bmi<34.9:
        result= "Obese"
    else:
        result= "Extermely obese"

    result_label.setText(f"Result: {result}")



# ui design

app=QApplication(sys.argv)

# window=QWidget()
window=QMainWindow()
window.setWindowTitle("GUI BMI Calculator")
window.setFixedSize(QSize(400,300))

widget=QWidget()

layout = QVBoxLayout()

height_label=QLabel("Height (m):")
height_entry=QLineEdit()


weight_label=QLabel("Weight (kg):")
weight_entry=QLineEdit()


calculate_button=QPushButton(text="Calculate")
calculate_button.clicked.connect(calculate_bmi)
result_label=QLabel("Result:")






layout.addWidget(height_label)
layout.addWidget(height_entry)


layout.addWidget(weight_label)
layout.addWidget(weight_entry)


layout.addWidget(calculate_button)


layout.addWidget(result_label)
widget.setLayout(layout)

window.setCentralWidget(widget)
window.show()





# run the app
 
app.exec()