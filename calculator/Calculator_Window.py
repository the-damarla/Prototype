from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

from nodeeditor.node_editor_window import NodeEditorWindow
from examples.calculator.calc_sub_window import CalculatorSubWindow
from nodeeditor.utils import dumpException
from examples.tictac.tictac import ticWindow


class CalculatorWindow(NodeEditorWindow):

    def initUI(self):

        self.name_company = 'Vijay sai Nag'
        self.name_product = 'Calculator'

        self.mdiArea = QMdiArea()
        self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdiArea)

        self.mdiArea.subWindowActivated.connect(self.updateMenus)
        self.windowMapper = QSignalMapper(self)
        self.windowMapper.mapped[QWidget].connect(self.setActiveSubWindow)

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.updateMenus()

        self.createNodesDock()


        self.readSettings()

        self.setWindowTitle("Vijay Calculator")

    def closeEvent(self, event):
        def closeEvent(self, event):
            self.mdiArea.closeAllSubWindows()
            if self.mdiArea.currentSubWindow():
                event.ignore()
            else:
                self.writeSettings()
                event.accept()

    def updateMenus(self):
        pass

    def createMenus(self):
        super().createMenus()

        self.windowMenu = self.menuBar().addMenu("&Window")
        self.updateWindowMenu()
        self.windowMenu.aboutToShow.connect(self.updateWindowMenu)

        self.menuBar().addSeparator()

        self.games = self.menuBar().addMenu("&Games")
        self.games.addAction(self.gameact)

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)


    def tictic(self):
        try:
            self.ui = ticWindow()
            self.window()
        except Exception as e: dumpException(e)

    def updateWindowMenu(self):
        self.windowMenu.clear()
        self.windowMenu.addAction(self.closeAct)
        self.windowMenu.addAction(self.closeAllAct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.tileAct)
        self.windowMenu.addAction(self.cascadeAct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.nextAct)
        self.windowMenu.addAction(self.previousAct)
        self.windowMenu.addAction(self.separatorAct)

        windows = self.mdiArea.subWindowList()
        self.separatorAct.setVisible(len(windows) != 0)

        for i, window in enumerate(windows):
            child = window.widget()

            text = "%d %s" % (i + 1, child.getUserFriendlyFilename())
            if i < 9:
                text = '&' + text

            action = self.windowMenu.addAction(text)
            action.setCheckable(True)
            action.setChecked(child is self.activeMdiChild())
            action.triggered.connect(self.windowMapper.map)
            self.windowMapper.setMapping(action, window)

    def createActions(self):
        super().createActions()

        self.closeAct = QAction("Cl&ose", self,
                                statusTip="Close the active window",
                                triggered=self.mdiArea.closeActiveSubWindow)

        self.closeAllAct = QAction("Close &All", self,
                                   statusTip="Close all the windows",
                                   triggered=self.mdiArea.closeAllSubWindows)

        self.tileAct = QAction("&Tile", self, statusTip="Tile the windows",
                               triggered=self.mdiArea.tileSubWindows)

        self.cascadeAct = QAction("&Cascade", self,
                                  statusTip="Cascade the windows",
                                  triggered=self.mdiArea.cascadeSubWindows)

        self.nextAct = QAction("Ne&xt", self, shortcut=QKeySequence.NextChild,
                               statusTip="Move the focus to the next window",
                               triggered=self.mdiArea.activateNextSubWindow)

        self.previousAct = QAction("Pre&vious", self,
                                   shortcut=QKeySequence.PreviousChild,
                                   statusTip="Move the focus to the previous window",
                                   triggered=self.mdiArea.activatePreviousSubWindow)

        self.separatorAct = QAction(self)
        self.separatorAct.setSeparator(True)

        self.aboutAct = QAction("&About", self,
                                statusTip="Show the application's About box",
                                triggered=self.about)

        self.gameact = QAction("&Tictac", self,
                               statusTip="you can play the game",
                               triggered=self.tictic)

    def onFileNew(self):
        subwnd = self.createMdiChild()
        subwnd.show()

    def onFileNew(self):
        try:
            subwnd = self.createMdiChild()
            subwnd.show()
        except Exception as e: dumpException(e)

    def about(self):
        QMessageBox.about(self, "About MDI",
                "The <b>Vijay Calculator</b> example demonstrates how to Calculate various "
                "values Using Qt and Node Editor.")

    def createToolBars(self):
        pass

    def createNodesDock(self):
        self.listWidget = QListWidget()
        self.listWidget.addItem("Add")
        self.listWidget.addItem("Subtract")
        self.listWidget.addItem("Multiply")
        self.listWidget.addItem("Divide")

        self.items = QDockWidget("Nodes")
        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)

        self.addDockWidget(Qt.RightDockWidgetArea, self.items)

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def createMdiChild(self):
        nodeeditor = CalculatorSubWindow()
        subwnd = self.mdiArea.addSubWindow(nodeeditor)
        return subwnd

    def activeMdiChild(self):
        activeSubWindow = self.mdiArea.activeSubWindow()
        if activeSubWindow:
            return activeSubWindow.widget()
        return None

    def setActiveSubWindow(self, window):
        if window:
            self.mdiArea.setActiveSubWindow(window)


