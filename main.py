import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLineEdit, QFrame, QPushButton, QLabel, QDialog, QVBoxLayout
from PyQt6.QtGui import QIntValidator, QIcon
from ui_sudokuGraphia import Ui_SudokuGraphia
from model.sudokuModel import SudokuModel, Algo


from PyQt6 import QtCore

class CustomPopup(QDialog):
    def __init__(self, titleFrame, msg: str):
        super(CustomPopup, self).__init__()

        # Créer les composants de la popup
        label = QLabel(msg)
        label.setStyleSheet("font-size: 12pt;")
        ok_button = QPushButton("Ok")
        ok_button.setStyleSheet("font-size: 12pt;")
        ok_button.clicked.connect(self.accept)

        # Créer une mise en page et ajouter les composants
        layout = QVBoxLayout(self)
        self.setWindowTitle(titleFrame)
        self.setMaximumSize(QtCore.QSize(0, 0))
        self.setMinimumSize(QtCore.QSize(100, 200))
        self.setWindowIcon(QIcon("./icon.ico"))
        layout.addWidget(label)
        layout.addWidget(ok_button)


class MainWindow(QtWidgets.QMainWindow):

    # CONSTRUCTEURS

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        
        QtWidgets.QApplication.instance().focusChanged.connect(self.on_focusChanged)
        
        self.ui = Ui_SudokuGraphia()
        self.ui.setupUi(self)
        self.setWindowTitle("SudokuGraphia")
        self.setWindowIcon(QIcon("./icon.ico"))
        # mise en place du model
        self.model = SudokuModel()
        # mise en place des controlleurs
        self.addControleur()
        self.resetSudoLines()

        self.currl = -1
        self.pastl = -1
        self.currc = -1
        self.pastc = -1
        
        self.popup = None
        self.refresh()
        
        self.model.setAlgo(Algo.NO_ALGO)
        self.ui.encourt.setStyleSheet('background-color: #456C85;')
        self.ui.resolveButton.setText("Vérifier")
        self.ui.desc.setText(str(self.model.getAlgo()))
        
    
    @QtCore.pyqtSlot("QWidget*", "QWidget*")
    def on_focusChanged(self, old, now):
        ql = self.getListSudoku()
        for ligne in range(9):
            for colonne in range(9):
                if ql[ligne * 9 + colonne] == now:
                    self.currl = (int(ql[ligne * 9 + colonne].objectName()[1:]) - 1) // 9
                    self.currc = (int(ql[ligne * 9 + colonne].objectName()[1:]) - 1) % 9
            for colonne in range(9):
                if ql[ligne * 9 + colonne] == old:
                    self.pastl = (int(ql[ligne * 9 + colonne].objectName()[1:]) - 1) // 9
                    self.pastc = (int(ql[ligne * 9 + colonne].objectName()[1:]) - 1) % 9
        if self.pastl != -1 and self.currl != self.pastl:
            for i in range(9):
                ql[self.pastl * 9 + i].setStyleSheet(ql[self.pastl * 9 + i].styleSheet().replace("background-color: #abc0ce;", ""))
        if self.pastc != -1 and self.currc != self.pastc:
            for i in range(9):
                ql[self.pastc + i * 9].setStyleSheet(ql[self.pastc + i * 9].styleSheet().replace("background-color: #abc0ce;", ""))
        if self.pastl != -1:
            cube_x = 3 * (self.pastc // 3)
            cube_y = 3 * (self.pastl // 3)
            for x in range(3):
                for y in range(3):
                    ql[(cube_x + x) + (cube_y + y) * 9].setStyleSheet(ql[(cube_x + x) + (cube_y + y) * 9].styleSheet().replace("background-color: #abc0ce;", ""))
                    ql[(cube_x + x) + (cube_y + y) * 9].setStyleSheet(ql[(cube_x + x) + (cube_y + y) * 9].styleSheet().replace("background-color: #BBDEFB;", ""))
        if self.currl != -1:
            cube_x = 3 * (self.currc // 3)
            cube_y = 3 * (self.currl // 3)
            for x in range(3):
                for y in range(3):
                    ql[(cube_x + x) + (cube_y + y) * 9].setStyleSheet(ql[(cube_x + x) + (cube_y + y) * 9].styleSheet() + "\nbackground-color: #abc0ce;")
        if self.currl != -1:
            for i in range(9):
                ql[self.currl * 9 + i].setStyleSheet(ql[self.currl * 9 + i].styleSheet() + "\nbackground-color: #abc0ce;")
                if i == self.currc:
                    for j in range(9):
                        ql[self.currc + j * 9].setStyleSheet(ql[self.currc + j * 9].styleSheet() + "\nbackground-color: #abc0ce;")
            ql[self.currl * 9 + self.currc].setStyleSheet(ql[self.currl * 9 + self.currc].styleSheet() + "\nbackground-color: #BBDEFB;")

    def addControleur(self):
        #on gère le button de changement d'algorithme
        self.ui.powel.clicked.connect(self.changeAlgo)
        self.ui.bck.clicked.connect(self.changeAlgo)
        self.ui.gl.clicked.connect(self.changeAlgo)
        self.ui.encourt.clicked.connect(self.manuelle)

        #on met en place le button de reset
        self.ui.reset.clicked.connect(self.resetSudoLines)
        #on met en place le button de génération
        self.ui.generate.clicked.connect(self.gen)
        #on met en place le button de résolution/ vérification
        self.ui.resolveButton.clicked.connect(self.resolve)
        
        #mise en place de l'input d'une case
        for input in self.getListSudoku():
            input.textChanged.connect(self.textChange)


    def refresh(self):
        if self.model.getAlgo() == Algo.NO_ALGO:
            self.ui.frame_sudo.setEnabled(True)
        else: 
            self.ui.frame_sudo.setEnabled(False)
        if self.model.isGenerated():
            sudoku = self.model.getSudoku()
            list_input = self.getListSudoku()
            for i in range(len(sudoku)):
                for j in range(len(sudoku)):
                    list_input[ i * len(sudoku) + j].setText(str(sudoku[i][j]))

    # OUTILS
    
    def textChange(self):
        button = self.sender()
        if len(button.text()) == 0:
            return
        self.model.setValue(int(button.objectName()[1:]), int(button.text()))

    def resolve(self):
        if not self.model.isGenerated():
            self.popup = CustomPopup("Erreur !", "❌ Un sudoku doit être générer avant de pouvoir être résolue ! 👽")
            self.popup.show()
        elif self.model.getAlgo() == Algo.NO_ALGO:
            if self.model.isSolve():
                self.popup = CustomPopup("Resultat", "✅ Bravo !!\nTu as réussit à résoudre le sudoku ! 🤯\nN'hésite pas a rejouer ! ✅")
                self.popup.show()
            elif not self.model.solve():
                self.popup = CustomPopup("Erreur !", "❌Vos réponse ne sont pas possible, il y a une erreur ! 🤡")
                self.popup.show()
            else:
                self.popup = CustomPopup("Resultat", "✋Le Sudoku n'est pas compléter. 🤨\nCependant, il n'y a pour l'instant aucune d'erreur ! 😼")
                self.popup.show()
        elif  not self.model.solve():
            self.popup = CustomPopup("Erreur !", "❌ Ce sudoku ne peut pas être résolu avec l'algorithme {}! ❌".format(self.model.getAlgo().name))
            self.popup.show()
        else:
            self.popup = CustomPopup("Resultat", "💪Ce Sudoku a pu être résolu grace à l'algorithme {}, n'hésite pas à lire la note de cet algorithme💯".format(self.model.getAlgo().name))
            self.popup.show()
        self.refresh()
    
    def gen(self):
        self.resetSudoLines()
        self.model.generate(0.5)
        sudoku = self.model.getSudoku()
        list_input = self.getListSudoku()
        for i in range(len(sudoku)):
            for j in range(len(sudoku)):
                val = sudoku[i][j]
                if val != 0:
                    list_input[ i * len(sudoku) + j].setReadOnly(True)
                    list_input[ i * len(sudoku) + j].setStyleSheet("color: red;")
                else:
                    list_input[ i * len(sudoku) + j].setReadOnly(False)
                list_input[ i * len(sudoku) + j].setText(str(val))
        if self.model.getAlgo() == Algo.NO_ALGO:
            self.ui.frame_sudo.setEnabled(True)
        else: 
            self.ui.frame_sudo.setEnabled(False)
    
    def getListSudoku(self):
        return sorted(self.ui.frame_sudo.findChildren(QLineEdit), key=lambda x : int(x.objectName()[1:]))

    def resetSudoLines(self):
        self.model.resetSudoku()
        self.ui.frame_sudo.setEnabled(False)
        listFrame = self.ui.frame_sudo.findChildren(QFrame)
        for f in listFrame:
            listsMyQLineEdit = f.findChildren(QLineEdit)
            for myQLineEdit in listsMyQLineEdit:
                myQLineEdit.setText("")
                myQLineEdit.setReadOnly(False)
                myQLineEdit.setStyleSheet("")
                myQLineEdit.setMaxLength(1)
                myQLineEdit.setValidator(QIntValidator())

    def changeAlgo(self):
        for btn in self.ui.groupBox_algo.findChildren(QPushButton):
            btn.setStyleSheet("")

        self.sender().setStyleSheet('background-color: #456C85;')
        match self.sender().objectName():
            case "powel":
                self.model.setAlgo(Algo.POWELL)
                self.ui.frame_sudo.setEnabled(False)
                pass
            case "bck":
                self.model.setAlgo(Algo.BACKTRACKING)
                self.ui.frame_sudo.setEnabled(False)
                pass
            case "gl":
                self.model.setAlgo(Algo.GREEDY)
                self.ui.frame_sudo.setEnabled(False)
                pass
            case "encourt":
                self.model.setAlgo(Algo.NO_ALGO)
                self.ui.frame_sudo.setEnabled(True)
                pass
        self.ui.desc.setText(str(self.model.getAlgo()))
        self.ui.resolveButton.setText("Résoudre")

    def manuelle(self):
        self.changeAlgo()
        self.ui.resolveButton.setText("Vérifier")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
