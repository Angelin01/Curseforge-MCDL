from PyQt5.QtWidgets import QMainWindow, QApplication
from gui import Ui_MainWindow

class OutLog:
	def __init__(self, txtBox, color=None):
		self.txtBox = txtBox
		self.color = color

	def write(self, m):
		if self.color:
			tc = self.txtBox.textColor()
			self.txtBox.setTextColor(self.color)

		self.txtBox.moveCursor(QtGui.QTextCursor.End)
		self.txtBox.insertPlainText(m)
		
		if self.color:
			self.txtBox.setTextColor(tc)

class AppMainWindow(QMainWindow):
	def closeEvent(self, event):
		print("THIS WORKS")
		super().closeEvent(event)
		
if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	MainWindow = AppMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	#sys.stdout = OutLog(ui.txtConsole)
	#sys.stderr = OutLog(ui.txtConsole, QtGui.QColor(255,0,0))
	MainWindow.show()
	sys.exit(app.exec_())