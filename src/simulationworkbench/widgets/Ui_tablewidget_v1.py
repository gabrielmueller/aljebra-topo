# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tom/Work/Eric4/BioPARKIN/src/simulationworkbench/widgets/tablewidget_v1.ui'
#
# Created: Tue Jul 17 14:29:50 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TableWidget(object):
    def setupUi(self, TableWidget):
        TableWidget.setObjectName("TableWidget")
        TableWidget.resize(793, 621)
        self.horizontalLayout = QtGui.QHBoxLayout(TableWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtGui.QSplitter(TableWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtGui.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tabWidgetPage1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dataSourceTableView = QtGui.QTableView(self.tabWidgetPage1)
        self.dataSourceTableView.setObjectName("dataSourceTableView")
        self.verticalLayout_3.addWidget(self.dataSourceTableView)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonSelectAll = QtGui.QPushButton(self.tabWidgetPage1)
        self.buttonSelectAll.setObjectName("buttonSelectAll")
        self.horizontalLayout_2.addWidget(self.buttonSelectAll)
        self.buttonDeselectAll = QtGui.QPushButton(self.tabWidgetPage1)
        self.buttonDeselectAll.setObjectName("buttonDeselectAll")
        self.horizontalLayout_2.addWidget(self.buttonDeselectAll)
        self.buttonInvertSelection = QtGui.QPushButton(self.tabWidgetPage1)
        self.buttonInvertSelection.setObjectName("buttonInvertSelection")
        self.horizontalLayout_2.addWidget(self.buttonInvertSelection)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtGui.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_GeneralSettings = QtGui.QGroupBox(self.tabWidgetPage2)
        self.groupBox_GeneralSettings.setObjectName("groupBox_GeneralSettings")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_GeneralSettings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxShowUnits = QtGui.QCheckBox(self.groupBox_GeneralSettings)
        self.checkBoxShowUnits.setChecked(True)
        self.checkBoxShowUnits.setObjectName("checkBoxShowUnits")
        self.verticalLayout.addWidget(self.checkBoxShowUnits)
        self.checkBoxOrientation = QtGui.QCheckBox(self.groupBox_GeneralSettings)
        self.checkBoxOrientation.setObjectName("checkBoxOrientation")
        self.verticalLayout.addWidget(self.checkBoxOrientation)
        self.verticalLayout_4.addWidget(self.groupBox_GeneralSettings)
        self.groupBox_Coloring = QtGui.QGroupBox(self.tabWidgetPage2)
        self.groupBox_Coloring.setCheckable(True)
        self.groupBox_Coloring.setChecked(False)
        self.groupBox_Coloring.setObjectName("groupBox_Coloring")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_Coloring)
        self.gridLayout.setObjectName("gridLayout")
        self.label_Coloring_Threshold = QtGui.QLabel(self.groupBox_Coloring)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Coloring_Threshold.sizePolicy().hasHeightForWidth())
        self.label_Coloring_Threshold.setSizePolicy(sizePolicy)
        self.label_Coloring_Threshold.setObjectName("label_Coloring_Threshold")
        self.gridLayout.addWidget(self.label_Coloring_Threshold, 0, 0, 1, 1)
        self.doubleSpinBox_Coloring_Threshold = QtGui.QDoubleSpinBox(self.groupBox_Coloring)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_Coloring_Threshold.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Coloring_Threshold.setSizePolicy(sizePolicy)
        self.doubleSpinBox_Coloring_Threshold.setWrapping(False)
        self.doubleSpinBox_Coloring_Threshold.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_Coloring_Threshold.setAccelerated(True)
        self.doubleSpinBox_Coloring_Threshold.setDecimals(5)
        self.doubleSpinBox_Coloring_Threshold.setMinimum(-1.0)
        self.doubleSpinBox_Coloring_Threshold.setMaximum(1.0)
        self.doubleSpinBox_Coloring_Threshold.setSingleStep(0.01)
        self.doubleSpinBox_Coloring_Threshold.setObjectName("doubleSpinBox_Coloring_Threshold")
        self.gridLayout.addWidget(self.doubleSpinBox_Coloring_Threshold, 0, 1, 1, 1)
        self.spinBox_Coloring_Exponent = QtGui.QSpinBox(self.groupBox_Coloring)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_Coloring_Exponent.sizePolicy().hasHeightForWidth())
        self.spinBox_Coloring_Exponent.setSizePolicy(sizePolicy)
        self.spinBox_Coloring_Exponent.setAccelerated(True)
        self.spinBox_Coloring_Exponent.setPrefix("")
        self.spinBox_Coloring_Exponent.setMinimum(-99)
        self.spinBox_Coloring_Exponent.setProperty("value", 0)
        self.spinBox_Coloring_Exponent.setObjectName("spinBox_Coloring_Exponent")
        self.gridLayout.addWidget(self.spinBox_Coloring_Exponent, 0, 3, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_Coloring)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_Coloring)
        self.groupBox_Actions = QtGui.QGroupBox(self.tabWidgetPage2)
        self.groupBox_Actions.setObjectName("groupBox_Actions")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_Actions)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonSaveTable = QtGui.QPushButton(self.groupBox_Actions)
        self.buttonSaveTable.setObjectName("buttonSaveTable")
        self.verticalLayout_2.addWidget(self.buttonSaveTable)
        self.buttonSetExperimentalData = QtGui.QPushButton(self.groupBox_Actions)
        self.buttonSetExperimentalData.setFlat(False)
        self.buttonSetExperimentalData.setObjectName("buttonSetExperimentalData")
        self.verticalLayout_2.addWidget(self.buttonSetExperimentalData)
        self.verticalLayout_4.addWidget(self.groupBox_Actions)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tableWrapper = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWrapper.sizePolicy().hasHeightForWidth())
        self.tableWrapper.setSizePolicy(sizePolicy)
        self.tableWrapper.setObjectName("tableWrapper")
        self.horizontalLayout.addWidget(self.splitter)
        self.actionSave = QtGui.QAction(TableWidget)
        self.actionSave.setObjectName("actionSave")
        self.actionAddToExperimentalData = QtGui.QAction(TableWidget)
        self.actionAddToExperimentalData.setObjectName("actionAddToExperimentalData")
        self.actionSelectAll = QtGui.QAction(TableWidget)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionDeselectAll = QtGui.QAction(TableWidget)
        self.actionDeselectAll.setObjectName("actionDeselectAll")
        self.actionInvertSelection = QtGui.QAction(TableWidget)
        self.actionInvertSelection.setObjectName("actionInvertSelection")

        self.retranslateUi(TableWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonSetExperimentalData, QtCore.SIGNAL("clicked()"), self.actionAddToExperimentalData.trigger)
        QtCore.QObject.connect(self.buttonSelectAll, QtCore.SIGNAL("clicked()"), self.actionSelectAll.trigger)
        QtCore.QObject.connect(self.buttonDeselectAll, QtCore.SIGNAL("clicked()"), self.actionDeselectAll.trigger)
        QtCore.QObject.connect(self.buttonInvertSelection, QtCore.SIGNAL("clicked()"), self.actionInvertSelection.trigger)
        QtCore.QObject.connect(self.buttonSaveTable, QtCore.SIGNAL("clicked()"), self.actionSave.trigger)
        QtCore.QMetaObject.connectSlotsByName(TableWidget)

    def retranslateUi(self, TableWidget):
        TableWidget.setWindowTitle(QtGui.QApplication.translate("TableWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSelectAll.setText(QtGui.QApplication.translate("TableWidget", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDeselectAll.setText(QtGui.QApplication.translate("TableWidget", "Deselect All", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonInvertSelection.setText(QtGui.QApplication.translate("TableWidget", "Invert Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QtGui.QApplication.translate("TableWidget", "Data Sources", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_GeneralSettings.setTitle(QtGui.QApplication.translate("TableWidget", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxShowUnits.setText(QtGui.QApplication.translate("TableWidget", "Show Units in Table Headers", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxOrientation.setText(QtGui.QApplication.translate("TableWidget", "Switch rows vs. columns", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_Coloring.setTitle(QtGui.QApplication.translate("TableWidget", "Coloring", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Coloring_Threshold.setText(QtGui.QApplication.translate("TableWidget", " Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TableWidget", "   E", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_Actions.setTitle(QtGui.QApplication.translate("TableWidget", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSaveTable.setText(QtGui.QApplication.translate("TableWidget", "Save Data...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSetExperimentalData.setText(QtGui.QApplication.translate("TableWidget", "Add Data to Data Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QtGui.QApplication.translate("TableWidget", "Settings && Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("TableWidget", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("TableWidget", "Save the current plot.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddToExperimentalData.setText(QtGui.QApplication.translate("TableWidget", "Add Data to Experimental Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddToExperimentalData.setToolTip(QtGui.QApplication.translate("TableWidget", "Adds the currently displayed data and adds it to the experimental data. This is usually only useful if you want to want to use simulation results (which can then be perturbed) as input for other tools like parameter value estimation.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectAll.setText(QtGui.QApplication.translate("TableWidget", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectAll.setToolTip(QtGui.QApplication.translate("TableWidget", "Select All Data Sources", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeselectAll.setText(QtGui.QApplication.translate("TableWidget", "Deselect All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeselectAll.setToolTip(QtGui.QApplication.translate("TableWidget", "Deselect All Data Sources", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvertSelection.setText(QtGui.QApplication.translate("TableWidget", "Invert Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvertSelection.setToolTip(QtGui.QApplication.translate("TableWidget", "Invert the Current Selection of Data Sources", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TableWidget = QtGui.QWidget()
    ui = Ui_TableWidget()
    ui.setupUi(TableWidget)
    TableWidget.show()
    sys.exit(app.exec_())

