# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memskel.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.control_F = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control_F.sizePolicy().hasHeightForWidth())
        self.control_F.setSizePolicy(sizePolicy)
        self.control_F.setMinimumSize(QtCore.QSize(200, 0))
        self.control_F.setMaximumSize(QtCore.QSize(200, 16777215))
        self.control_F.setFrameShape(QtGui.QFrame.StyledPanel)
        self.control_F.setFrameShadow(QtGui.QFrame.Raised)
        self.control_F.setObjectName(_fromUtf8("control_F"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.control_F)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame_6 = QtGui.QFrame(self.control_F)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.open_BTN = QtGui.QPushButton(self.frame_6)
        self.open_BTN.setObjectName(_fromUtf8("open_BTN"))
        self.horizontalLayout_8.addWidget(self.open_BTN)
        self.save_BTN = QtGui.QPushButton(self.frame_6)
        self.save_BTN.setObjectName(_fromUtf8("save_BTN"))
        self.horizontalLayout_8.addWidget(self.save_BTN)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.line_6 = QtGui.QFrame(self.control_F)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_2.addWidget(self.line_6)
        self.thresholding_GB = QtGui.QGroupBox(self.control_F)
        self.thresholding_GB.setMinimumSize(QtCore.QSize(0, 60))
        self.thresholding_GB.setMaximumSize(QtCore.QSize(16777215, 120))
        self.thresholding_GB.setObjectName(_fromUtf8("thresholding_GB"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.thresholding_GB)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.threshold_LBL = QtGui.QLabel(self.thresholding_GB)
        self.threshold_LBL.setMaximumSize(QtCore.QSize(20000, 20))
        self.threshold_LBL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.threshold_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.threshold_LBL.setObjectName(_fromUtf8("threshold_LBL"))
        self.verticalLayout_3.addWidget(self.threshold_LBL)
        self.threshold_SL = QtGui.QSlider(self.thresholding_GB)
        self.threshold_SL.setMaximum(255)
        self.threshold_SL.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_SL.setObjectName(_fromUtf8("threshold_SL"))
        self.verticalLayout_3.addWidget(self.threshold_SL)
        self.frame_3 = QtGui.QFrame(self.thresholding_GB)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.rectangle_ROI_BTN = QtGui.QPushButton(self.frame_3)
        self.rectangle_ROI_BTN.setObjectName(_fromUtf8("rectangle_ROI_BTN"))
        self.horizontalLayout_5.addWidget(self.rectangle_ROI_BTN)
        self.circle_ROI_BTN = QtGui.QPushButton(self.frame_3)
        self.circle_ROI_BTN.setObjectName(_fromUtf8("circle_ROI_BTN"))
        self.horizontalLayout_5.addWidget(self.circle_ROI_BTN)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.thresholding_GB)
        self.line_2 = QtGui.QFrame(self.control_F)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.segmentation_GB = QtGui.QGroupBox(self.control_F)
        self.segmentation_GB.setMinimumSize(QtCore.QSize(0, 100))
        self.segmentation_GB.setMaximumSize(QtCore.QSize(16777215, 100))
        self.segmentation_GB.setObjectName(_fromUtf8("segmentation_GB"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.segmentation_GB)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame_4 = QtGui.QFrame(self.segmentation_GB)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.segment_img_BTN = QtGui.QPushButton(self.frame_4)
        self.segment_img_BTN.setObjectName(_fromUtf8("segment_img_BTN"))
        self.horizontalLayout_6.addWidget(self.segment_img_BTN)
        self.segment_stack_BTN = QtGui.QPushButton(self.frame_4)
        self.segment_stack_BTN.setObjectName(_fromUtf8("segment_stack_BTN"))
        self.horizontalLayout_6.addWidget(self.segment_stack_BTN)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.label_3 = QtGui.QLabel(self.segmentation_GB)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.frame_5 = QtGui.QFrame(self.segmentation_GB)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.segment_obj_BTN = QtGui.QPushButton(self.frame_5)
        self.segment_obj_BTN.setCheckable(True)
        self.segment_obj_BTN.setObjectName(_fromUtf8("segment_obj_BTN"))
        self.horizontalLayout_7.addWidget(self.segment_obj_BTN)
        self.segment_bgd_BTN = QtGui.QPushButton(self.frame_5)
        self.segment_bgd_BTN.setCheckable(True)
        self.segment_bgd_BTN.setObjectName(_fromUtf8("segment_bgd_BTN"))
        self.horizontalLayout_7.addWidget(self.segment_bgd_BTN)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.segmentation_GB)
        self.line_3 = QtGui.QFrame(self.control_F)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        self.skeleton_GB = QtGui.QGroupBox(self.control_F)
        self.skeleton_GB.setMinimumSize(QtCore.QSize(0, 60))
        self.skeleton_GB.setMaximumSize(QtCore.QSize(16777215, 60))
        self.skeleton_GB.setObjectName(_fromUtf8("skeleton_GB"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.skeleton_GB)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.skeleton_BTN = QtGui.QPushButton(self.skeleton_GB)
        self.skeleton_BTN.setObjectName(_fromUtf8("skeleton_BTN"))
        self.verticalLayout_5.addWidget(self.skeleton_BTN)
        self.verticalLayout_2.addWidget(self.skeleton_GB)
        self.line_4 = QtGui.QFrame(self.control_F)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.approximation_GB = QtGui.QGroupBox(self.control_F)
        self.approximation_GB.setMinimumSize(QtCore.QSize(0, 100))
        self.approximation_GB.setMaximumSize(QtCore.QSize(16777215, 100))
        self.approximation_GB.setObjectName(_fromUtf8("approximation_GB"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.approximation_GB)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.approximation_BTN = QtGui.QPushButton(self.approximation_GB)
        self.approximation_BTN.setObjectName(_fromUtf8("approximation_BTN"))
        self.verticalLayout_6.addWidget(self.approximation_BTN)
        self.frame = QtGui.QFrame(self.approximation_GB)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.smoothing_fac_SB = QtGui.QSpinBox(self.frame)
        self.smoothing_fac_SB.setMaximumSize(QtCore.QSize(50, 16777215))
        self.smoothing_fac_SB.setMaximum(10)
        self.smoothing_fac_SB.setProperty("value", 1)
        self.smoothing_fac_SB.setObjectName(_fromUtf8("smoothing_fac_SB"))
        self.horizontalLayout_3.addWidget(self.smoothing_fac_SB)
        self.verticalLayout_6.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.approximation_GB)
        self.line_5 = QtGui.QFrame(self.control_F)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_2.addWidget(self.line_5)
        self.eraser_GB = QtGui.QGroupBox(self.control_F)
        self.eraser_GB.setMinimumSize(QtCore.QSize(0, 100))
        self.eraser_GB.setMaximumSize(QtCore.QSize(16777215, 100))
        self.eraser_GB.setObjectName(_fromUtf8("eraser_GB"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.eraser_GB)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.eraser_BTN = QtGui.QPushButton(self.eraser_GB)
        self.eraser_BTN.setObjectName(_fromUtf8("eraser_BTN"))
        self.verticalLayout_7.addWidget(self.eraser_BTN)
        self.frame_2 = QtGui.QFrame(self.eraser_GB)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.smoothing_fac_SB_2 = QtGui.QSpinBox(self.frame_2)
        self.smoothing_fac_SB_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.smoothing_fac_SB_2.setMinimum(1)
        self.smoothing_fac_SB_2.setMaximum(50)
        self.smoothing_fac_SB_2.setProperty("value", 1)
        self.smoothing_fac_SB_2.setObjectName(_fromUtf8("smoothing_fac_SB_2"))
        self.horizontalLayout_4.addWidget(self.smoothing_fac_SB_2)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.eraser_GB)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.control_F)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.display_F = QtGui.QFrame(self.centralwidget)
        self.display_F.setFrameShape(QtGui.QFrame.StyledPanel)
        self.display_F.setFrameShadow(QtGui.QFrame.Raised)
        self.display_F.setObjectName(_fromUtf8("display_F"))
        self.verticalLayout = QtGui.QVBoxLayout(self.display_F)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.views_F = QtGui.QFrame(self.display_F)
        self.views_F.setMaximumSize(QtCore.QSize(16777215, 40))
        self.views_F.setFrameShape(QtGui.QFrame.StyledPanel)
        self.views_F.setFrameShadow(QtGui.QFrame.Raised)
        self.views_F.setObjectName(_fromUtf8("views_F"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.views_F)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.disp_roi_BTN = QtGui.QPushButton(self.views_F)
        self.disp_roi_BTN.setCheckable(True)
        self.disp_roi_BTN.setObjectName(_fromUtf8("disp_roi_BTN"))
        self.horizontalLayout_2.addWidget(self.disp_roi_BTN)
        self.disp_membrane_BTN = QtGui.QPushButton(self.views_F)
        self.disp_membrane_BTN.setCheckable(True)
        self.disp_membrane_BTN.setObjectName(_fromUtf8("disp_membrane_BTN"))
        self.horizontalLayout_2.addWidget(self.disp_membrane_BTN)
        self.disp_skelet_BTN = QtGui.QPushButton(self.views_F)
        self.disp_skelet_BTN.setCheckable(True)
        self.disp_skelet_BTN.setObjectName(_fromUtf8("disp_skelet_BTN"))
        self.horizontalLayout_2.addWidget(self.disp_skelet_BTN)
        self.disp_approximation_BTN = QtGui.QPushButton(self.views_F)
        self.disp_approximation_BTN.setCheckable(True)
        self.disp_approximation_BTN.setObjectName(_fromUtf8("disp_approximation_BTN"))
        self.horizontalLayout_2.addWidget(self.disp_approximation_BTN)
        self.verticalLayout.addWidget(self.views_F)
        self.frame_7 = QtGui.QFrame(self.display_F)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.canvas_L = QtGui.QLabel(self.frame_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_L.sizePolicy().hasHeightForWidth())
        self.canvas_L.setSizePolicy(sizePolicy)
        self.canvas_L.setText(_fromUtf8(""))
        self.canvas_L.setObjectName(_fromUtf8("canvas_L"))
        self.verticalLayout_9.addWidget(self.canvas_L)
        self.slice_slider_F = QtGui.QFrame(self.frame_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slice_slider_F.sizePolicy().hasHeightForWidth())
        self.slice_slider_F.setSizePolicy(sizePolicy)
        self.slice_slider_F.setFrameShape(QtGui.QFrame.StyledPanel)
        self.slice_slider_F.setFrameShadow(QtGui.QFrame.Raised)
        self.slice_slider_F.setObjectName(_fromUtf8("slice_slider_F"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.slice_slider_F)
        self.horizontalLayout_9.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.actual_slice_LBL = QtGui.QLabel(self.slice_slider_F)
        self.actual_slice_LBL.setMinimumSize(QtCore.QSize(20, 0))
        self.actual_slice_LBL.setMaximumSize(QtCore.QSize(20, 16777215))
        self.actual_slice_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.actual_slice_LBL.setObjectName(_fromUtf8("actual_slice_LBL"))
        self.horizontalLayout_9.addWidget(self.actual_slice_LBL)
        self.label_4 = QtGui.QLabel(self.slice_slider_F)
        self.label_4.setMaximumSize(QtCore.QSize(5, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_9.addWidget(self.label_4)
        self.max_slice_LBL = QtGui.QLabel(self.slice_slider_F)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_slice_LBL.sizePolicy().hasHeightForWidth())
        self.max_slice_LBL.setSizePolicy(sizePolicy)
        self.max_slice_LBL.setMinimumSize(QtCore.QSize(20, 0))
        self.max_slice_LBL.setMaximumSize(QtCore.QSize(20, 16777215))
        self.max_slice_LBL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.max_slice_LBL.setObjectName(_fromUtf8("max_slice_LBL"))
        self.horizontalLayout_9.addWidget(self.max_slice_LBL)
        self.slice_SB = QtGui.QScrollBar(self.slice_slider_F)
        self.slice_SB.setOrientation(QtCore.Qt.Horizontal)
        self.slice_SB.setObjectName(_fromUtf8("slice_SB"))
        self.horizontalLayout_9.addWidget(self.slice_SB)
        self.verticalLayout_9.addWidget(self.slice_slider_F)
        self.verticalLayout.addWidget(self.frame_7)
        self.horizontalLayout.addWidget(self.display_F)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.threshold_SL, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.threshold_LBL.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MemSkel", None))
        self.open_BTN.setText(_translate("MainWindow", "Open", None))
        self.save_BTN.setText(_translate("MainWindow", "Save", None))
        self.thresholding_GB.setTitle(_translate("MainWindow", "ROI definition", None))
        self.threshold_LBL.setText(_translate("MainWindow", "0", None))
        self.rectangle_ROI_BTN.setText(_translate("MainWindow", "Rectangle", None))
        self.circle_ROI_BTN.setText(_translate("MainWindow", "Circle", None))
        self.segmentation_GB.setTitle(_translate("MainWindow", "Segmentation", None))
        self.segment_img_BTN.setText(_translate("MainWindow", "img", None))
        self.segment_stack_BTN.setText(_translate("MainWindow", "stack", None))
        self.label_3.setText(_translate("MainWindow", "Marking:", None))
        self.segment_obj_BTN.setText(_translate("MainWindow", "object", None))
        self.segment_bgd_BTN.setText(_translate("MainWindow", "background", None))
        self.skeleton_GB.setTitle(_translate("MainWindow", "Skeleton", None))
        self.skeleton_BTN.setText(_translate("MainWindow", "skeletonize", None))
        self.approximation_GB.setTitle(_translate("MainWindow", "Approximation", None))
        self.approximation_BTN.setText(_translate("MainWindow", "Approximation", None))
        self.label.setText(_translate("MainWindow", "Smoothing factor:", None))
        self.eraser_GB.setTitle(_translate("MainWindow", "Eraser", None))
        self.eraser_BTN.setText(_translate("MainWindow", "Eraser", None))
        self.label_2.setText(_translate("MainWindow", "Radius:", None))
        self.disp_roi_BTN.setText(_translate("MainWindow", "ROI", None))
        self.disp_membrane_BTN.setText(_translate("MainWindow", "membrane", None))
        self.disp_skelet_BTN.setText(_translate("MainWindow", "skelet", None))
        self.disp_approximation_BTN.setText(_translate("MainWindow", "approximation", None))
        self.actual_slice_LBL.setText(_translate("MainWindow", "0", None))
        self.label_4.setText(_translate("MainWindow", "/", None))
        self.max_slice_LBL.setText(_translate("MainWindow", "0", None))

