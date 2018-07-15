import sys
from PySide2 import QtCore, QtGui, QtWidgets


class CalenderWidget(QtWidgets.QWidget):
    def __init__(self):
        super(CalenderWidget, self).__init__()
        self.init()

    def init(self):
        c = QtWidgets.QCalendarWidget(self)
        c.setGridVisible(True)
        c.move(20, 20)
        l = QtWidgets.QLabel(self)
        l.move(20, 250)
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Select Date Calender")

        def show_data(date):
            l.setText(date.toString())

        c.clicked[QtCore.QDate].connect(show_data)
        show_data(c.selectedDate())
        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = CalenderWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
