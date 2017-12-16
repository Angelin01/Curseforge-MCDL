# ----------
# Mod Item
# ----------

class ModItem(object):
    def __init__(self, name):
        self.name = name
        self.progress = QtWidgets.QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.progress.setFixedHeight(15)

    def addToTree(self, tree):
        self.item = QtWidgets.QTreeWidgetItem(tree)
        tree.setItemWidget(self.item, 0, self.progress)
        self.item.setText(1, self.name)

    def updateProgress(self, current, total):
        if current > 0:
            percent = current/total * 100
        else:
            percent = 0
        self.progress.setValue(percent)