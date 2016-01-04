# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1026, 695)
        MainWindow.setStyleSheet(_fromUtf8("background-color: #0F2D40;\n"
"color: #2ecc71;\n"
"font: 10pt \"MS Shell Dlg 2\";"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("QWidget#centralwidget {\n"
"background-color: #0F2D40;\n"
"color: #2ecc71;\n"
"border-radius: 3px;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #194759;\n"
"     width: 10px;\n"
"     margin: 22px 0 22px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"     background: #2ecc71;\n"
"     min-height: 20px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #32CC99;\n"
"     height: 16px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #32CC99;\n"
"     height: 16px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     border-radius: 2px;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"     background: white;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar:horizontal {\n"
"border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #194759;\n"
"     height: 10px;\n"
"     margin: 0px 40px 0 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #2ecc71;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    background: #32CC99;\n"
"    width: 16px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    background: #32CC99;\n"
"    width: 16px;\n"
"    subcontrol-position: top right;\n"
"    subcontrol-origin: margin;\n"
"    position: absolute;\n"
"    right: 20px;\n"
"}\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: pink;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.clientButtonsGroup = QtGui.QGroupBox(self.centralwidget)
        self.clientButtonsGroup.setStyleSheet(_fromUtf8("border: 1px ridge;\n"
"border-color: #0F2D40;\n"
"background-color: #0F2D40;"))
        self.clientButtonsGroup.setTitle(_fromUtf8(""))
        self.clientButtonsGroup.setCheckable(False)
        self.clientButtonsGroup.setObjectName(_fromUtf8("clientButtonsGroup"))
        self.gridLayout = QtGui.QGridLayout(self.clientButtonsGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startListenButton = QtGui.QPushButton(self.clientButtonsGroup)
        self.startListenButton.setMinimumSize(QtCore.QSize(70, 32))
        self.startListenButton.setMaximumSize(QtCore.QSize(70, 32))
        self.startListenButton.setStyleSheet(_fromUtf8("QPushButton#startListenButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#startListenButton:checked {\n"
"            background: #0B202E;\n"
"            color: grey;\n"
"            border: 1px outset;\n"
"            border-color: #0B202E;\n"
"            }"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startListenButton.setIcon(icon)
        self.startListenButton.setIconSize(QtCore.QSize(22, 22))
        self.startListenButton.setCheckable(True)
        self.startListenButton.setObjectName(_fromUtf8("startListenButton"))
        self.horizontalLayout.addWidget(self.startListenButton)
        self.stopListenButton = QtGui.QPushButton(self.clientButtonsGroup)
        self.stopListenButton.setMinimumSize(QtCore.QSize(70, 32))
        self.stopListenButton.setMaximumSize(QtCore.QSize(70, 32))
        self.stopListenButton.setStyleSheet(_fromUtf8("QPushButton#stopListenButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#stopListenButton:checked {\n"
"            background: #0B202E;\n"
"            color: grey;\n"
"            border: 1px outset;\n"
"            border-color: #0B202E;\n"
"            }"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopListenButton.setIcon(icon1)
        self.stopListenButton.setIconSize(QtCore.QSize(20, 20))
        self.stopListenButton.setCheckable(True)
        self.stopListenButton.setChecked(True)
        self.stopListenButton.setObjectName(_fromUtf8("stopListenButton"))
        self.horizontalLayout.addWidget(self.stopListenButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.clientSettingsButton = QtGui.QPushButton(self.clientButtonsGroup)
        self.clientSettingsButton.setMinimumSize(QtCore.QSize(120, 32))
        self.clientSettingsButton.setMaximumSize(QtCore.QSize(120, 32))
        self.clientSettingsButton.setStyleSheet(_fromUtf8("QPushButton#clientSettingsButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            color: white;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#clientSettingsButton:pressed {\n"
"            background: #0B202E;\n"
"            color: grey;\n"
"            border: 1px outset;\n"
"            border-color: #0B202E;\n"
"            }"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clientSettingsButton.setIcon(icon2)
        self.clientSettingsButton.setIconSize(QtCore.QSize(20, 20))
        self.clientSettingsButton.setObjectName(_fromUtf8("clientSettingsButton"))
        self.horizontalLayout.addWidget(self.clientSettingsButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.clientButtonsGroup, 0, 0, 1, 1)
        self.MainTabWidget = QtGui.QTabWidget(self.centralwidget)
        self.MainTabWidget.setStyleSheet(_fromUtf8(" QTabBar::tab {\n"
"  background-color: #194759;\n"
"  padding: 10px;\n"
"  color: white;\n"
"  padding-left: 15px;\n"
"  width: 70%;\n"
"  border: 1px ridge;\n"
"  border-color: #0F2D40;\n"
"  border-bottom: none;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"   background: #0F2D40;;\n"
" }\n"
"\n"
" QTabBar::pane {\n"
"   background-color: #194759;\n"
" }\n"
"\n"
"QTabWidget::pane {\n"
"    color: rgb(246, 246, 244);\n"
"    margin: 0px,1px,1px,1px;\n"
"    border: 1px ridge;\n"
"    border-color: #0F2D40;\n"
"    background-color: #194759;\n"
"    background-position: center;\n"
"      }"))
        self.MainTabWidget.setObjectName(_fromUtf8("MainTabWidget"))
        self.serversTab = QtGui.QWidget()
        self.serversTab.setObjectName(_fromUtf8("serversTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.serversTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.serversTable = QtGui.QTableWidget(self.serversTab)
        self.serversTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #194759;\n"
"    padding: 2px;\n"
"    color: white;\n"
"    font: 9pt \"MS Shell Dlg 2\";\n"
"    border: 1px ridge;\n"
"}\n"
"\n"
"QTableWidget#serversTable {\n"
"    background-position: center;\n"
"    border: 1px ridge;\n"
"    padding: 5px;\n"
"    outline: 0;\n"
"    border-color: #0F2D40;\n"
"    border-radius: 2px;\n"
"    font: 9pt \"MS Shell Dlg 2\";\n"
"    background-color: #081621;\n"
"}\n"
"\n"
"QTableWidget#serversTable:item:selected {\n"
"background-color: #194759;\n"
"color: white;\n"
"}"))
        self.serversTable.setFrameShadow(QtGui.QFrame.Plain)
        self.serversTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.serversTable.setDragDropOverwriteMode(False)
        self.serversTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.serversTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.serversTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.serversTable.setShowGrid(False)
        self.serversTable.setGridStyle(QtCore.Qt.NoPen)
        self.serversTable.setWordWrap(False)
        self.serversTable.setCornerButtonEnabled(False)
        self.serversTable.setObjectName(_fromUtf8("serversTable"))
        self.serversTable.setColumnCount(7)
        self.serversTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(6, item)
        self.serversTable.horizontalHeader().setCascadingSectionResizes(True)
        self.serversTable.horizontalHeader().setDefaultSectionSize(100)
        self.serversTable.horizontalHeader().setSortIndicatorShown(False)
        self.serversTable.horizontalHeader().setStretchLastSection(True)
        self.serversTable.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.serversTable, 0, 0, 2, 1)
        self.panelGroup = QtGui.QGroupBox(self.serversTab)
        self.panelGroup.setMinimumSize(QtCore.QSize(320, 320))
        self.panelGroup.setMaximumSize(QtCore.QSize(320, 16777215))
        self.panelGroup.setStyleSheet(_fromUtf8("background-color: #081621;\n"
"border: 1px outset;\n"
"border-color: #0F2D40;"))
        self.panelGroup.setTitle(_fromUtf8(""))
        self.panelGroup.setFlat(False)
        self.panelGroup.setObjectName(_fromUtf8("panelGroup"))
        self.gridLayout_6 = QtGui.QGridLayout(self.panelGroup)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.remoteShellButton = QtGui.QPushButton(self.panelGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remoteShellButton.sizePolicy().hasHeightForWidth())
        self.remoteShellButton.setSizePolicy(sizePolicy)
        self.remoteShellButton.setMinimumSize(QtCore.QSize(0, 24))
        self.remoteShellButton.setMaximumSize(QtCore.QSize(150, 24))
        self.remoteShellButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.remoteShellButton.setAcceptDrops(False)
        self.remoteShellButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remoteShellButton.setAutoFillBackground(False)
        self.remoteShellButton.setStyleSheet(_fromUtf8("QPushButton#remoteShellButton {\n"
"            border-bottom: none;\n"
"            background-color: #0F2D40;\n"
"            border-radius: 1px;\n"
"            padding-left: 5px;\n"
"            text-align: left;\n"
"            }\n"
"\n"
"QPushButton#remoteShellButton:pressed {\n"
"            background: #0B202E;\n"
"            border: 1px outset;\n"
"            border-color: #0B202E;\n"
"            }\n"
"\n"
"QPushButton#remoteShellButton:disabled {\n"
"            background: #0B202E;\n"
"            border: 1px outset;\n"
"            color: grey;\n"
"            border-color: #0B202E;\n"
"            }"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mshell.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remoteShellButton.setIcon(icon3)
        self.remoteShellButton.setIconSize(QtCore.QSize(18, 18))
        self.remoteShellButton.setAutoRepeat(False)
        self.remoteShellButton.setAutoExclusive(False)
        self.remoteShellButton.setAutoDefault(False)
        self.remoteShellButton.setDefault(False)
        self.remoteShellButton.setFlat(False)
        self.remoteShellButton.setObjectName(_fromUtf8("remoteShellButton"))
        self.gridLayout_6.addWidget(self.remoteShellButton, 4, 0, 1, 2)
        self.remoteExplorerButton = QtGui.QPushButton(self.panelGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remoteExplorerButton.sizePolicy().hasHeightForWidth())
        self.remoteExplorerButton.setSizePolicy(sizePolicy)
        self.remoteExplorerButton.setMinimumSize(QtCore.QSize(150, 24))
        self.remoteExplorerButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.remoteExplorerButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remoteExplorerButton.setStyleSheet(_fromUtf8("QPushButton#remoteExplorerButton {\n"
"            border-bottom: none;\n"
"            background-color: #0F2D40;\n"
"            border-radius: 1px;\n"
"            padding-left: 5px;\n"
"            text-align: left;\n"
"            }\n"
"\n"
"QPushButton#remoteExplorerButton:pressed {\n"
"            background: #0B202E;\n"
"            border: 1px outset;\n"
"            border-color: #0B202E;\n"
"            }\n"
"\n"
"QPushButton#remoteExplorerButton:disabled {\n"
"            background: #0B202E;\n"
"            border: 1px outset;\n"
"            color: grey;\n"
"            border-color: #0B202E;\n"
"            }"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mexplorer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remoteExplorerButton.setIcon(icon4)
        self.remoteExplorerButton.setIconSize(QtCore.QSize(18, 18))
        self.remoteExplorerButton.setObjectName(_fromUtf8("remoteExplorerButton"))
        self.gridLayout_6.addWidget(self.remoteExplorerButton, 4, 2, 1, 1)
        self.unlockServerButton = QtGui.QPushButton(self.panelGroup)
        self.unlockServerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.unlockServerButton.setStyleSheet(_fromUtf8("QPushButton#unlockServerButton {\n"
"            border-bottom: none;\n"
"            background-color: #0F2D40;\n"
"            border-radius: 1px;\n"
"            }\n"
"\n"
"QPushButton#unlockServerButton:pressed {\n"
"            background: #0B202E;\n"
"            border: 1px outset;\n"
"            border-color: #0B202E;\n"
"            }\n"
"\n"
"QPushButton#unlockServerButton:disabled {\n"
"            background: #0B202E;\n"
"            border: 1px outset;\n"
"            color: grey;\n"
"            border-color: #0B202E;\n"
"            }"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/unlock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unlockServerButton.setIcon(icon5)
        self.unlockServerButton.setObjectName(_fromUtf8("unlockServerButton"))
        self.gridLayout_6.addWidget(self.unlockServerButton, 3, 0, 1, 4)
        self.updatePreviewButton = QtGui.QPushButton(self.panelGroup)
        self.updatePreviewButton.setStyleSheet(_fromUtf8("QPushButton#updatePreviewButton {\n"
"            border-bottom: none;\n"
"            background-color: #0F2D40;\n"
"            border-radius: 1px;\n"
"            }\n"
"\n"
"QPushButton#updatePreviewButton:pressed {\n"
"            background: #0B202E;\n"
"            border: 1px outset;\n"
"            border-color: #0B202E;\n"
"            }\n"
"\n"
"QPushButton#updatePreviewButton:disabled {\n"
"            background: #0B202E;\n"
"            border: 1px outset;\n"
"            color: grey;\n"
"            border-color: #0B202E;\n"
"            }"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updatePreviewButton.setIcon(icon6)
        self.updatePreviewButton.setIconSize(QtCore.QSize(14, 14))
        self.updatePreviewButton.setObjectName(_fromUtf8("updatePreviewButton"))
        self.gridLayout_6.addWidget(self.updatePreviewButton, 1, 0, 1, 4)
        self.quitServerButton = QtGui.QPushButton(self.panelGroup)
        self.quitServerButton.setMinimumSize(QtCore.QSize(0, 22))
        self.quitServerButton.setStyleSheet(_fromUtf8("QPushButton#quitServerButton {\n"
"            border-bottom: none;\n"
"            background-color: #0F2D40;\n"
"            border-radius: 1px;\n"
"            padding-left: 5px;\n"
"            text-align: left;\n"
"            color: #e74c3c;\n"
"            }\n"
"\n"
"QPushButton#quitServerButton:pressed {\n"
"            background: #0B202E;\n"
"            border: 1px outset;\n"
"            border-color: #0B202E;\n"
"            }\n"
"\n"
"QPushButton#quitServerButton:disabled {\n"
"            background: #0B202E;\n"
"            border: 1px outset;\n"
"            color: grey;\n"
"            border-color: #0B202E;\n"
"            }"))
        self.quitServerButton.setIcon(icon1)
        self.quitServerButton.setIconSize(QtCore.QSize(18, 18))
        self.quitServerButton.setObjectName(_fromUtf8("quitServerButton"))
        self.gridLayout_6.addWidget(self.quitServerButton, 5, 2, 1, 2)
        self.previewLabel = QtGui.QLabel(self.panelGroup)
        self.previewLabel.setMinimumSize(QtCore.QSize(300, 200))
        self.previewLabel.setMaximumSize(QtCore.QSize(300, 200))
        self.previewLabel.setStyleSheet(_fromUtf8("background-image: url(:/icons/assets/monitor.png);\n"
"background-repeat: none;\n"
"padding-left: 10px;\n"
"padding-top: 10px;\n"
"border: none;"))
        self.previewLabel.setText(_fromUtf8(""))
        self.previewLabel.setObjectName(_fromUtf8("previewLabel"))
        self.gridLayout_6.addWidget(self.previewLabel, 0, 0, 1, 3)
        self.lockServerButton = QtGui.QPushButton(self.panelGroup)
        self.lockServerButton.setMinimumSize(QtCore.QSize(0, 22))
        self.lockServerButton.setStyleSheet(_fromUtf8("QPushButton#lockServerButton {\n"
"            border-bottom: none;\n"
"            background-color: #0F2D40;\n"
"            border-radius: 1px;\n"
"            padding-left: 5px;\n"
"            text-align: left;\n"
"            color: #e74c3c;\n"
"            }\n"
"\n"
"QPushButton#lockServerButton:pressed {\n"
"            background: #0B202E;\n"
"            border: 1px outset;\n"
"            border-color: #0B202E;\n"
"            }\n"
"\n"
"QPushButton#lockServerButton:disabled {\n"
"            background: #0B202E;\n"
"            border: 1px outset;\n"
"            color: grey;\n"
"            border-color: #0B202E;\n"
"            }"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/lock_2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lockServerButton.setIcon(icon7)
        self.lockServerButton.setIconSize(QtCore.QSize(18, 18))
        self.lockServerButton.setObjectName(_fromUtf8("lockServerButton"))
        self.gridLayout_6.addWidget(self.lockServerButton, 5, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(10, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.panelGroup, 0, 1, 2, 1)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/server.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainTabWidget.addTab(self.serversTab, icon8, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.MainTabWidget, 1, 0, 1, 1)
        self.statusGroup = QtGui.QGroupBox(self.centralwidget)
        self.statusGroup.setMaximumSize(QtCore.QSize(16777215, 32))
        self.statusGroup.setStyleSheet(_fromUtf8("border: 1px ridge;\n"
"border-color: #0F2D40;\n"
"background-color: #0F2D40;\n"
"padding: 0px;"))
        self.statusGroup.setTitle(_fromUtf8(""))
        self.statusGroup.setObjectName(_fromUtf8("statusGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.statusGroup)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 2, 1, 1)
        self.clientStatusLabel = QtGui.QLabel(self.statusGroup)
        self.clientStatusLabel.setStyleSheet(_fromUtf8("border: none; \n"
"color: white;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.clientStatusLabel.setObjectName(_fromUtf8("clientStatusLabel"))
        self.gridLayout_4.addWidget(self.clientStatusLabel, 0, 3, 1, 1)
        self.statusLabel = QtGui.QLabel(self.statusGroup)
        self.statusLabel.setStyleSheet(_fromUtf8("border: none;\n"
"color: #e74c3c;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.gridLayout_4.addWidget(self.statusLabel, 0, 4, 1, 1)
        self.serversOnlineStatus = QtGui.QLabel(self.statusGroup)
        self.serversOnlineStatus.setStyleSheet(_fromUtf8("border: none; \n"
"color: white;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.serversOnlineStatus.setObjectName(_fromUtf8("serversOnlineStatus"))
        self.gridLayout_4.addWidget(self.serversOnlineStatus, 0, 5, 1, 1)
        self.onlineStatus = QtGui.QLabel(self.statusGroup)
        self.onlineStatus.setStyleSheet(_fromUtf8("border: none;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.onlineStatus.setObjectName(_fromUtf8("onlineStatus"))
        self.gridLayout_4.addWidget(self.onlineStatus, 0, 6, 1, 1)
        self.versionLabel = QtGui.QLabel(self.statusGroup)
        self.versionLabel.setStyleSheet(_fromUtf8("border: none; \n"
"color: white;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.gridLayout_4.addWidget(self.versionLabel, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.statusGroup, 2, 0, 1, 1)
        self.creditLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.creditLabel.setFont(font)
        self.creditLabel.setStyleSheet(_fromUtf8("border: none; \n"
"color: white;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.creditLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.creditLabel.setObjectName(_fromUtf8("creditLabel"))
        self.gridLayout_5.addWidget(self.creditLabel, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 24))
        self.menubar.setStyleSheet(_fromUtf8("QMenuBar {\n"
"            background-color: #0C2230;\n"
"            color: rgb(255,255,255);\n"
"            border: 1px solid #000;\n"
"        }\n"
"\n"
"        QMenuBar::item {\n"
"            background-color: #0C2230;\n"
"            color: rgb(255,255,255);\n"
"        }\n"
"\n"
"        QMenuBar::item::selected {\n"
"            background-color: #0F2D40;\n"
"        }\n"
"\n"
"        QMenu {\n"
"            background-color: #0C2230;\n"
"            color: rgb(255,255,255);\n"
"            border: 1px solid #000;           \n"
"        }\n"
"\n"
"        QMenu::item::selected {\n"
"            background-color: #0F2D40;\n"
"        }"))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuClient = QtGui.QMenu(self.menubar)
        self.menuClient.setObjectName(_fromUtf8("menuClient"))
        MainWindow.setMenuBar(self.menubar)
        self.actionStartListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStartListen_for_connections.setObjectName(_fromUtf8("actionStartListen_for_connections"))
        self.actionStopListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStopListen_for_connections.setObjectName(_fromUtf8("actionStopListen_for_connections"))
        self.actionClient_Configuration = QtGui.QAction(MainWindow)
        self.actionClient_Configuration.setObjectName(_fromUtf8("actionClient_Configuration"))
        self.menuClient.addAction(self.actionStartListen_for_connections)
        self.menuClient.addAction(self.actionStopListen_for_connections)
        self.menuClient.addSeparator()
        self.menuClient.addAction(self.actionClient_Configuration)
        self.menubar.addAction(self.menuClient.menuAction())

        self.retranslateUi(MainWindow)
        self.MainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Moderat Client", None))
        self.startListenButton.setText(_translate("MainWindow", "Start", None))
        self.stopListenButton.setText(_translate("MainWindow", "Stop", None))
        self.clientSettingsButton.setText(_translate("MainWindow", "Client Settings", None))
        self.serversTable.setSortingEnabled(False)
        item = self.serversTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ip Address", None))
        item = self.serversTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Socket", None))
        item = self.serversTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Protection", None))
        item = self.serversTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "OS", None))
        item = self.serversTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "User", None))
        item = self.serversTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Version", None))
        item = self.serversTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Active Window Title", None))
        self.remoteShellButton.setText(_translate("MainWindow", "Remote Shell", None))
        self.remoteExplorerButton.setText(_translate("MainWindow", "Remote Explorer", None))
        self.unlockServerButton.setText(_translate("MainWindow", "Unlock Server", None))
        self.updatePreviewButton.setText(_translate("MainWindow", "Update Preview", None))
        self.quitServerButton.setText(_translate("MainWindow", "Quit Server", None))
        self.lockServerButton.setText(_translate("MainWindow", "Lock Server", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.serversTab), _translate("MainWindow", "Servers", None))
        self.clientStatusLabel.setText(_translate("MainWindow", "Client Status: ", None))
        self.statusLabel.setText(_translate("MainWindow", "Not Listening", None))
        self.serversOnlineStatus.setText(_translate("MainWindow", "Servers Online: ", None))
        self.onlineStatus.setText(_translate("MainWindow", "0", None))
        self.versionLabel.setText(_translate("MainWindow", "Client Version 2.0", None))
        self.creditLabel.setText(_translate("MainWindow", "© Uri Patton", None))
        self.menuClient.setTitle(_translate("MainWindow", "Client", None))
        self.actionStartListen_for_connections.setText(_translate("MainWindow", "Start Listening", None))
        self.actionStopListen_for_connections.setText(_translate("MainWindow", "Stop Listening", None))
        self.actionClient_Configuration.setText(_translate("MainWindow", "Client Configuration", None))

import res_rc