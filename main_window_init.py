# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 2, -1, 2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.inspire_courage_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.inspire_courage_check_box.setChecked(False)
        self.inspire_courage_check_box.setObjectName("inspire_courage_check_box")
        self.verticalLayout_4.addWidget(self.inspire_courage_check_box)
        self.haste_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.haste_check_box.setObjectName("haste_check_box")
        self.verticalLayout_4.addWidget(self.haste_check_box)
        self.raging_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.raging_check_box.setObjectName("raging_check_box")
        self.verticalLayout_4.addWidget(self.raging_check_box)
        self.charging_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.charging_check_box.setObjectName("charging_check_box")
        self.verticalLayout_4.addWidget(self.charging_check_box)
        self.water_subtype_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.water_subtype_check_box.setObjectName("water_subtype_check_box")
        self.verticalLayout_4.addWidget(self.water_subtype_check_box)
        self.flanking_bonus_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.flanking_bonus_check_box.setObjectName("flanking_bonus_check_box")
        self.verticalLayout_4.addWidget(self.flanking_bonus_check_box)
        self.sneak_attack_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.sneak_attack_check_box.setObjectName("sneak_attack_check_box")
        self.verticalLayout_4.addWidget(self.sneak_attack_check_box)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.attack_bonus_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.attack_bonus_label.setFont(font)
        self.attack_bonus_label.setFrameShape(QtWidgets.QFrame.Box)
        self.attack_bonus_label.setObjectName("attack_bonus_label")
        self.horizontalLayout.addWidget(self.attack_bonus_label)
        self.num_hits_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        self.num_hits_spin_box.setMaximumSize(QtCore.QSize(35, 16777215))
        self.num_hits_spin_box.setSuffix("")
        self.num_hits_spin_box.setMinimum(1)
        self.num_hits_spin_box.setObjectName("num_hits_spin_box")
        self.horizontalLayout.addWidget(self.num_hits_spin_box)
        self.damage_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.damage_label.setFont(font)
        self.damage_label.setFrameShape(QtWidgets.QFrame.Box)
        self.damage_label.setObjectName("damage_label")
        self.horizontalLayout.addWidget(self.damage_label)
        self.crit_damage_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.crit_damage_label.setFont(font)
        self.crit_damage_label.setFrameShape(QtWidgets.QFrame.Box)
        self.crit_damage_label.setObjectName("crit_damage_label")
        self.horizontalLayout.addWidget(self.crit_damage_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ares Snek"))
        self.label.setText(_translate("MainWindow", "Ares Snek"))
        self.label_2.setText(_translate("MainWindow", "Buffs and ability modifiers:"))
        self.inspire_courage_check_box.setText(_translate("MainWindow", "Insipre Courage (Bard playing)"))
        self.haste_check_box.setText(_translate("MainWindow", "Haste"))
        self.raging_check_box.setText(_translate("MainWindow", "Raging"))
        self.charging_check_box.setText(_translate("MainWindow", "Charging"))
        self.water_subtype_check_box.setText(_translate("MainWindow", "Attacking Water Subtype"))
        self.flanking_bonus_check_box.setText(_translate("MainWindow", "Flanking"))
        self.sneak_attack_check_box.setText(_translate("MainWindow", "Sneak Attack"))
        self.attack_bonus_label.setText(_translate("MainWindow", "Attack Bonus:"))
        self.num_hits_spin_box.setToolTip(_translate("MainWindow", "Number of Hits"))
        self.damage_label.setText(_translate("MainWindow", "Damage:"))
        self.crit_damage_label.setText(_translate("MainWindow", "Critical Damage:"))
