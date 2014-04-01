# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/segmentationwidget.ui'
#
# Created: Tue Apr  1 16:26:52 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SegmentationWidget(object):
    def setupUi(self, SegmentationWidget):
        SegmentationWidget.setObjectName("SegmentationWidget")
        SegmentationWidget.resize(1033, 731)
        self.gridLayout_2 = QtGui.QGridLayout(SegmentationWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtGui.QSplitter(SegmentationWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox = GroupBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self._toolBox = QtGui.QToolBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._toolBox.sizePolicy().hasHeightForWidth())
        self._toolBox.setSizePolicy(sizePolicy)
        self._toolBox.setObjectName("_toolBox")
        self.file = QtGui.QWidget()
        self.file.setGeometry(QtCore.QRect(0, 0, 184, 234))
        self.file.setObjectName("file")
        self.gridLayout = QtGui.QGridLayout(self.file)
        self.gridLayout.setObjectName("gridLayout")
        self._pushButtonLoad = QtGui.QPushButton(self.file)
        self._pushButtonLoad.setObjectName("_pushButtonLoad")
        self.gridLayout.addWidget(self._pushButtonLoad, 1, 0, 1, 1)
        self._pushButtonSave = QtGui.QPushButton(self.file)
        self._pushButtonSave.setObjectName("_pushButtonSave")
        self.gridLayout.addWidget(self._pushButtonSave, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self._toolBox.addItem(self.file, "")
        self.view = QtGui.QWidget()
        self.view.setGeometry(QtCore.QRect(0, 0, 227, 455))
        self.view.setObjectName("view")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.view)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtGui.QGroupBox(self.view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self._radioButtonParallel = QtGui.QRadioButton(self.groupBox_3)
        self._radioButtonParallel.setObjectName("_radioButtonParallel")
        self.verticalLayout_9.addWidget(self._radioButtonParallel)
        self._radioButtonPerspective = QtGui.QRadioButton(self.groupBox_3)
        self._radioButtonPerspective.setChecked(True)
        self._radioButtonPerspective.setObjectName("_radioButtonPerspective")
        self.verticalLayout_9.addWidget(self._radioButtonPerspective)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_6 = QtGui.QGroupBox(self.view)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtGui.QLabel(self.groupBox_6)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self._doubleSpinBoxNormalArrow = QtGui.QDoubleSpinBox(self.groupBox_6)
        self._doubleSpinBoxNormalArrow.setMinimum(0.01)
        self._doubleSpinBoxNormalArrow.setMaximum(9999999.99)
        self._doubleSpinBoxNormalArrow.setObjectName("_doubleSpinBoxNormalArrow")
        self.verticalLayout_6.addWidget(self._doubleSpinBoxNormalArrow)
        self.label_8 = QtGui.QLabel(self.groupBox_6)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self._doubleSpinBoxRotationCentre = QtGui.QDoubleSpinBox(self.groupBox_6)
        self._doubleSpinBoxRotationCentre.setMinimum(0.01)
        self._doubleSpinBoxRotationCentre.setMaximum(999999.99)
        self._doubleSpinBoxRotationCentre.setObjectName("_doubleSpinBoxRotationCentre")
        self.verticalLayout_6.addWidget(self._doubleSpinBoxRotationCentre)
        self.label_9 = QtGui.QLabel(self.groupBox_6)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self._doubleSpinBoxSegmentationPoint = QtGui.QDoubleSpinBox(self.groupBox_6)
        self._doubleSpinBoxSegmentationPoint.setMinimum(0.01)
        self._doubleSpinBoxSegmentationPoint.setMaximum(999999.99)
        self._doubleSpinBoxSegmentationPoint.setObjectName("_doubleSpinBoxSegmentationPoint")
        self.verticalLayout_6.addWidget(self._doubleSpinBoxSegmentationPoint)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_7 = QtGui.QGroupBox(self.view)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self._checkBoxImagePlane = QtGui.QCheckBox(self.groupBox_7)
        self._checkBoxImagePlane.setChecked(True)
        self._checkBoxImagePlane.setObjectName("_checkBoxImagePlane")
        self.verticalLayout_10.addWidget(self._checkBoxImagePlane)
        self._checkBoxImageOutline = QtGui.QCheckBox(self.groupBox_7)
        self._checkBoxImageOutline.setChecked(True)
        self._checkBoxImageOutline.setObjectName("_checkBoxImageOutline")
        self.verticalLayout_10.addWidget(self._checkBoxImageOutline)
        self._checkBoxCoordinateLabels = QtGui.QCheckBox(self.groupBox_7)
        self._checkBoxCoordinateLabels.setChecked(True)
        self._checkBoxCoordinateLabels.setObjectName("_checkBoxCoordinateLabels")
        self.verticalLayout_10.addWidget(self._checkBoxCoordinateLabels)
        self.verticalLayout_3.addWidget(self.groupBox_7)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self._pushButtonViewAll = QtGui.QPushButton(self.view)
        self._pushButtonViewAll.setObjectName("_pushButtonViewAll")
        self.horizontalLayout_4.addWidget(self._pushButtonViewAll)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self._pushButtonReset = QtGui.QPushButton(self.view)
        self._pushButtonReset.setObjectName("_pushButtonReset")
        self.horizontalLayout_3.addWidget(self._pushButtonReset)
        spacerItem4 = QtGui.QSpacerItem(37, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self._toolBox.addItem(self.view, "")
        self.mode = QtGui.QWidget()
        self.mode.setGeometry(QtCore.QRect(0, 0, 184, 234))
        self.mode.setObjectName("mode")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.mode)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtGui.QGroupBox(self.mode)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self._radioButtonSegment = QtGui.QRadioButton(self.groupBox_2)
        self._radioButtonSegment.setChecked(True)
        self._radioButtonSegment.setObjectName("_radioButtonSegment")
        self.verticalLayout_2.addWidget(self._radioButtonSegment)
        self._radioButtonMove = QtGui.QRadioButton(self.groupBox_2)
        self._radioButtonMove.setToolTip("")
        self._radioButtonMove.setObjectName("_radioButtonMove")
        self.verticalLayout_2.addWidget(self._radioButtonMove)
        self._radioButtonRotate = QtGui.QRadioButton(self.groupBox_2)
        self._radioButtonRotate.setToolTip("")
        self._radioButtonRotate.setObjectName("_radioButtonRotate")
        self.verticalLayout_2.addWidget(self._radioButtonRotate)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_8 = QtGui.QGroupBox(self.mode)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self._checkBoxStreamingCreate = QtGui.QCheckBox(self.groupBox_8)
        self._checkBoxStreamingCreate.setObjectName("_checkBoxStreamingCreate")
        self.verticalLayout_11.addWidget(self._checkBoxStreamingCreate)
        self.verticalLayout_4.addWidget(self.groupBox_8)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self._toolBox.addItem(self.mode, "")
        self.image = QtGui.QWidget()
        self.image.setGeometry(QtCore.QRect(0, 0, 170, 244))
        self.image.setObjectName("image")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.image)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_4 = QtGui.QGroupBox(self.image)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self._labelmageWidth = QtGui.QLabel(self.groupBox_4)
        self._labelmageWidth.setText("")
        self._labelmageWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self._labelmageWidth.setObjectName("_labelmageWidth")
        self.horizontalLayout_2.addWidget(self._labelmageWidth)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self._labelmageHeight = QtGui.QLabel(self.groupBox_4)
        self._labelmageHeight.setText("")
        self._labelmageHeight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self._labelmageHeight.setObjectName("_labelmageHeight")
        self.horizontalLayout_5.addWidget(self._labelmageHeight)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self._labelmageDepth = QtGui.QLabel(self.groupBox_4)
        self._labelmageDepth.setText("")
        self._labelmageDepth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self._labelmageDepth.setObjectName("_labelmageDepth")
        self.horizontalLayout_6.addWidget(self._labelmageDepth)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_8.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.image)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtGui.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self._lineEditWidthScale = QtGui.QLineEdit(self.groupBox_5)
        self._lineEditWidthScale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self._lineEditWidthScale.setObjectName("_lineEditWidthScale")
        self.horizontalLayout_7.addWidget(self._lineEditWidthScale)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self._lineEditHeightScale = QtGui.QLineEdit(self.groupBox_5)
        self._lineEditHeightScale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self._lineEditHeightScale.setObjectName("_lineEditHeightScale")
        self.horizontalLayout_8.addWidget(self._lineEditHeightScale)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self._lineEditDepthScale = QtGui.QLineEdit(self.groupBox_5)
        self._lineEditDepthScale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self._lineEditDepthScale.setObjectName("_lineEditDepthScale")
        self.horizontalLayout_9.addWidget(self._lineEditDepthScale)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout_8.addWidget(self.groupBox_5)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self._toolBox.addItem(self.image, "")
        self.verticalLayout.addWidget(self._toolBox)
        self._tabWidget1 = SegmentationTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self._tabWidget1.sizePolicy().hasHeightForWidth())
        self._tabWidget1.setSizePolicy(sizePolicy)
        self._tabWidget1.setObjectName("_tabWidget1")
        self.tab3d = QtGui.QWidget()
        self.tab3d.setObjectName("tab3d")
        self.verticalLayoutTab3d = QtGui.QVBoxLayout(self.tab3d)
        self.verticalLayoutTab3d.setObjectName("verticalLayoutTab3d")
        self._sceneviewer3d = SceneviewerWidget3D(self.tab3d)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self._sceneviewer3d.sizePolicy().hasHeightForWidth())
        self._sceneviewer3d.setSizePolicy(sizePolicy)
        self._sceneviewer3d.setMinimumSize(QtCore.QSize(30, 30))
        self._sceneviewer3d.setObjectName("_sceneviewer3d")
        self.verticalLayoutTab3d.addWidget(self._sceneviewer3d)
        self._tabWidget1.addTab(self.tab3d, "")
        self.tab2d = QtGui.QWidget()
        self.tab2d.setObjectName("tab2d")
        self.verticalLayoutTab2d = QtGui.QVBoxLayout(self.tab2d)
        self.verticalLayoutTab2d.setObjectName("verticalLayoutTab2d")
        self._sceneviewer2d = SceneviewerWidget2D(self.tab2d)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._sceneviewer2d.sizePolicy().hasHeightForWidth())
        self._sceneviewer2d.setSizePolicy(sizePolicy)
        self._sceneviewer2d.setObjectName("_sceneviewer2d")
        self.verticalLayoutTab2d.addWidget(self._sceneviewer2d)
        self._tabWidget1.addTab(self.tab2d, "")
        self._tabWidget2 = SegmentationTabWidget(self.splitter)
        self._tabWidget2.setObjectName("_tabWidget2")
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.doneButton = QtGui.QPushButton(SegmentationWidget)
        self.doneButton.setObjectName("doneButton")
        self.horizontalLayout.addWidget(self.doneButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(SegmentationWidget)
        self._toolBox.setCurrentIndex(2)
        self._tabWidget1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SegmentationWidget)

    def retranslateUi(self, SegmentationWidget):
        SegmentationWidget.setWindowTitle(QtGui.QApplication.translate("SegmentationWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SegmentationWidget", "Digitiser", None, QtGui.QApplication.UnicodeUTF8))
        self._pushButtonLoad.setText(QtGui.QApplication.translate("SegmentationWidget", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self._pushButtonSave.setText(QtGui.QApplication.translate("SegmentationWidget", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self._toolBox.setItemText(self._toolBox.indexOf(self.file), QtGui.QApplication.translate("SegmentationWidget", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("SegmentationWidget", "Projection Mode", None, QtGui.QApplication.UnicodeUTF8))
        self._radioButtonParallel.setText(QtGui.QApplication.translate("SegmentationWidget", "Parallel", None, QtGui.QApplication.UnicodeUTF8))
        self._radioButtonPerspective.setText(QtGui.QApplication.translate("SegmentationWidget", "Perspective                       ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("SegmentationWidget", "Icon Sizes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("SegmentationWidget", "Image Plane Normal Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("SegmentationWidget", "Image Plane Rotation Centre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("SegmentationWidget", "Segmentation point", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("SegmentationWidget", "Graphic Visibility", None, QtGui.QApplication.UnicodeUTF8))
        self._checkBoxImagePlane.setText(QtGui.QApplication.translate("SegmentationWidget", "Image plane", None, QtGui.QApplication.UnicodeUTF8))
        self._checkBoxImageOutline.setText(QtGui.QApplication.translate("SegmentationWidget", "Image outline", None, QtGui.QApplication.UnicodeUTF8))
        self._checkBoxCoordinateLabels.setText(QtGui.QApplication.translate("SegmentationWidget", "Coordinate labels", None, QtGui.QApplication.UnicodeUTF8))
        self._pushButtonViewAll.setText(QtGui.QApplication.translate("SegmentationWidget", "View All", None, QtGui.QApplication.UnicodeUTF8))
        self._pushButtonReset.setText(QtGui.QApplication.translate("SegmentationWidget", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self._toolBox.setItemText(self._toolBox.indexOf(self.view), QtGui.QApplication.translate("SegmentationWidget", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("SegmentationWidget", "View Mode", None, QtGui.QApplication.UnicodeUTF8))
        self._radioButtonSegment.setText(QtGui.QApplication.translate("SegmentationWidget", "Segment", None, QtGui.QApplication.UnicodeUTF8))
        self._radioButtonMove.setText(QtGui.QApplication.translate("SegmentationWidget", "Move Image Plane", None, QtGui.QApplication.UnicodeUTF8))
        self._radioButtonRotate.setText(QtGui.QApplication.translate("SegmentationWidget", "Rotate Image Plane", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("SegmentationWidget", "Create Mode", None, QtGui.QApplication.UnicodeUTF8))
        self._checkBoxStreamingCreate.setText(QtGui.QApplication.translate("SegmentationWidget", "Streaming", None, QtGui.QApplication.UnicodeUTF8))
        self._toolBox.setItemText(self._toolBox.indexOf(self.mode), QtGui.QApplication.translate("SegmentationWidget", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("SegmentationWidget", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SegmentationWidget", "Width : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SegmentationWidget", "Height : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SegmentationWidget", "Depth : ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("SegmentationWidget", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SegmentationWidget", "Width : ", None, QtGui.QApplication.UnicodeUTF8))
        self._lineEditWidthScale.setText(QtGui.QApplication.translate("SegmentationWidget", "1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SegmentationWidget", "Height : ", None, QtGui.QApplication.UnicodeUTF8))
        self._lineEditHeightScale.setText(QtGui.QApplication.translate("SegmentationWidget", "1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("SegmentationWidget", "Depth : ", None, QtGui.QApplication.UnicodeUTF8))
        self._lineEditDepthScale.setText(QtGui.QApplication.translate("SegmentationWidget", "1.0", None, QtGui.QApplication.UnicodeUTF8))
        self._toolBox.setItemText(self._toolBox.indexOf(self.image), QtGui.QApplication.translate("SegmentationWidget", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self._tabWidget1.setTabText(self._tabWidget1.indexOf(self.tab3d), QtGui.QApplication.translate("SegmentationWidget", "3D View", None, QtGui.QApplication.UnicodeUTF8))
        self._tabWidget1.setTabText(self._tabWidget1.indexOf(self.tab2d), QtGui.QApplication.translate("SegmentationWidget", "2D View", None, QtGui.QApplication.UnicodeUTF8))
        self.doneButton.setText(QtGui.QApplication.translate("SegmentationWidget", "&Done", None, QtGui.QApplication.UnicodeUTF8))

from segmentationstep.widgets.sceneviewerwidget3d import SceneviewerWidget3D
from segmentationstep.widgets.groupbox import GroupBox
from segmentationstep.widgets.segmentationtabwidget import SegmentationTabWidget
from segmentationstep.widgets.sceneviewerwidget2d import SceneviewerWidget2D
from . import resources_rc
