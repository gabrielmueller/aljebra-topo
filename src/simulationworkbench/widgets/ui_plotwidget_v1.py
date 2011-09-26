# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\bioparkin\src\simulationworkbench\widgets\plotwidget_v1.ui'
#
# Created: Mon Sep 26 08:08:46 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PlotWidget(object):
    def setupUi(self, PlotWidget):
        PlotWidget.setObjectName("PlotWidget")
        PlotWidget.resize(793, 621)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(PlotWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtGui.QSplitter(PlotWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtGui.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dataSourceTableView = QtGui.QTableView(self.tabWidgetPage1)
        self.dataSourceTableView.setObjectName("dataSourceTableView")
        self.verticalLayout_3.addWidget(self.dataSourceTableView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonSelectAll = QtGui.QPushButton(self.tabWidgetPage1)
        self.buttonSelectAll.setObjectName("buttonSelectAll")
        self.horizontalLayout.addWidget(self.buttonSelectAll)
        self.buttonDeselectAll = QtGui.QPushButton(self.tabWidgetPage1)
        self.buttonDeselectAll.setObjectName("buttonDeselectAll")
        self.horizontalLayout.addWidget(self.buttonDeselectAll)
        self.buttonInvertSelection = QtGui.QPushButton(self.tabWidgetPage1)
        self.buttonInvertSelection.setObjectName("buttonInvertSelection")
        self.horizontalLayout.addWidget(self.buttonInvertSelection)
        spacerItem = QtGui.QSpacerItem(278, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtGui.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxShowLegend = QtGui.QCheckBox(self.tabWidgetPage2)
        self.checkBoxShowLegend.setChecked(False)
        self.checkBoxShowLegend.setObjectName("checkBoxShowLegend")
        self.verticalLayout.addWidget(self.checkBoxShowLegend)
        self.checkBoxLogYAxis = QtGui.QCheckBox(self.tabWidgetPage2)
        self.checkBoxLogYAxis.setObjectName("checkBoxLogYAxis")
        self.verticalLayout.addWidget(self.checkBoxLogYAxis)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonSavePlot = QtGui.QPushButton(self.tabWidgetPage2)
        self.buttonSavePlot.setObjectName("buttonSavePlot")
        self.verticalLayout_2.addWidget(self.buttonSavePlot)
        spacerItem1 = QtGui.QSpacerItem(20, 429, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.plotWrapper = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWrapper.sizePolicy().hasHeightForWidth())
        self.plotWrapper.setSizePolicy(sizePolicy)
        self.plotWrapper.setObjectName("plotWrapper")
        self.horizontalLayout_2.addWidget(self.splitter)
        self.actionSave = QtGui.QAction(PlotWidget)
        self.actionSave.setObjectName("actionSave")
        self.actionSelectAll = QtGui.QAction(PlotWidget)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionDeselectAll = QtGui.QAction(PlotWidget)
        self.actionDeselectAll.setObjectName("actionDeselectAll")
        self.actionInvertSelection = QtGui.QAction(PlotWidget)
        self.actionInvertSelection.setObjectName("actionInvertSelection")

        self.retranslateUi(PlotWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PlotWidget)

    def retranslateUi(self, PlotWidget):
        PlotWidget.setWindowTitle(QtGui.QApplication.translate("PlotWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSelectAll.setText(QtGui.QApplication.translate("PlotWidget", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDeselectAll.setText(QtGui.QApplication.translate("PlotWidget", "Deselect All", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonInvertSelection.setText(QtGui.QApplication.translate("PlotWidget", "Invert Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QtGui.QApplication.translate("PlotWidget", "Data Sources", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxShowLegend.setText(QtGui.QApplication.translate("PlotWidget", "Show &Legend", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxLogYAxis.setText(QtGui.QApplication.translate("PlotWidget", "&Logarithmic Y Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSavePlot.setText(QtGui.QApplication.translate("PlotWidget", "Save Plot...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QtGui.QApplication.translate("PlotWidget", "Settings && Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("PlotWidget", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("PlotWidget", "Save the current plot.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectAll.setText(QtGui.QApplication.translate("PlotWidget", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeselectAll.setText(QtGui.QApplication.translate("PlotWidget", "Deselect All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvertSelection.setText(QtGui.QApplication.translate("PlotWidget", "Invert Selection", None, QtGui.QApplication.UnicodeUTF8))

