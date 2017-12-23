from PyQt5.QtWidgets import QMainWindow, QApplication
from gui import Ui_MainWindow
from os import path
from configparser import ConfigParser

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
	# Overloading the close event to save stuff on exit
	def closeEvent(self, event):
		# Saving "state"
		global ui
		config = ConfigParser()
		config.add_section('General')
		config.set('General', 'modList', ','.join(ui.modList))
		config.set('General', 'downloadDir', ui.downloadDir)
		config.set('General', 'importDir', ui.importDir)
		config.set('General', 'exportDir', ui.exportDir)
		config.set('General', 'cmbMcIndex', str(ui.cmbMcVersion.currentIndex()))
		config.set('General', 'mostRecent', str(ui.radRecent.isChecked()))
		config.set('General', 'releasesOnly', str(ui.radReleases.isChecked()))
		config.set('General', 'optionalDeps', str(ui.chkOptDeps.isChecked()))
		
		with open(path.dirname(path.abspath(__file__)).replace(path.sep, "/") + "/config.cfg", 'w') as configFile:
			config.write(configFile)
			
		super().closeEvent(event)
		
# This is recomended by PyQt to avoid crashes on exit: http://pyqt.sourceforge.net/Docs/PyQt5/gotchas.html#crashes-on-exit
app = None
ui = None

def main():
	import sys
	
	global app
	global ui
	
	app = QApplication(sys.argv)
	MainWindow = AppMainWindow()
	if path.exists(path.dirname(path.abspath(__file__)).replace(path.sep, "/") + "/config.cfg"):
		config = ConfigParser()
		config.read(path.dirname(path.abspath(__file__)).replace(path.sep, "/") + "/config.cfg")
		ui = Ui_MainWindow(config)
	else:
		ui = Ui_MainWindow()
		
	ui.setupUi(MainWindow)
	#sys.stdout = OutLog(ui.txtConsole)
	#sys.stderr = OutLog(ui.txtConsole, QtGui.QColor(255,0,0))
	MainWindow.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()