import sys
from pyside import QtCore, QtGui

class calander_widget(QtGui.QWidget):
    def __init__(self):
        super(calander_widget, self).__init__()
        self.init()

    def init(self):
        c = QtGui.QCalanderWidget(self)
        c.setGridVisible(True)
        c.move(20,20)
        l = QtGui.QLabel(self)
        l.move(200, 50)
        self.setGeomentry(100,100,500,500)
        self.setWindowTitle("Select Date Calander")
        
        def showdata(self, date):
            l.setText(date.toString())
             
        c.clicked[QtCore.QDate].connect(showdata)
        showdata(self, c.selectedDate())
        self.show()

def main():
    app = QtGui.QtApplication(sys.argv)
    ex = calander_widget()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()

    
