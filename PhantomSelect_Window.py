from PyQt5 import QtCore, QtGui, QtWidgets
from PhantomSelect import Ui_Wid_PhantomSelect
import os,os.path



class selectPhantom(Ui_Wid_PhantomSelect):

    #Initialisation
    def __init__(self, widget):
        Ui_Wid_PhantomSelect.__init__(self)
        self.setupUi(widget)
        self.listwidload


    def listwidload(self):

        i = 1
        j = 1
        path = "Resources"
        files = []
        for dirpath, _, filenames in os.walk(path):
            for file in filenames:
                if file.endswith(".png"):
                    files.append(os.path.abspath(os.path.join(dirpath, file)))

        Phantom_Path = {}
        for x in files:
            Phantom_Path["Phantom"+str(i)]  = x
            i=i+1


        for x in files:
            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(x), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setText("Phantom"+str(j))
            j+=1
            self.ListWid_SelectPhantom.setSelectionMode( QtWidgets.QAbstractItemView.ExtendedSelection )
            self.ListWid_SelectPhantom.addItem(item)
            self.ListWid_SelectPhantom.setIconSize(QtCore.QSize(200,200))

        return Phantom_Path

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    wid_PhanWindow = QtWidgets.QWidget()
    ui = selectPhantom(wid_PhanWindow )
    ui.setupUi(wid_PhanWindow)
    wid_PhanWindow.show()
    sys.exit(app.exec_())
