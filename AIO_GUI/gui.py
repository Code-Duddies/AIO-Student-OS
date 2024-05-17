import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.tab_widget = QTabWidget()
        
        # Set tabs to the right side
        self.tab_widget.setTabPosition(QTabWidget.East)  
        self.setCentralWidget(self.tab_widget)

        for i in range(5):
            tab = QWidget()
            layout = QVBoxLayout()
            tab.setLayout(layout)
            self.tab_widget.addTab(tab, f'Tab {i+1}')

        # Sets the size of the window
        self.setGeometry(100, 100, 800, 600)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
