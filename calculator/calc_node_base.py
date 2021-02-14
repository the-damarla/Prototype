from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from nodeeditor.node_node import Node
from nodeeditor.node_content_widget import QDMNodeContentWidget
from nodeeditor.node_graphics_node import QDMGraphicsNode
from examples.calculator.calc_drag_listbox import *


class CalcGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        """Set up internal attributes like `width`, `height`, etc."""
        super().initSizes()
        self.width = 160
        self.height = 240
        self.edge_roundness = 10.0
        self.edge_padding = 10.0
        self.title_horizontal_padding = 4.0
        self.title_vertical_padding = 4.0


class CalcContent(QDMNodeContentWidget):
    def initUI(self):
        lb1 = QTextEdit(self.node.content_text, self)
        lb1.setObjectName(self.node.content_text_objname)


class CalcNode(Node):
    def __init__(self, scene, op_code, op_title, content_text="", content_text_objname="calc_node_bg", inputs=[2, 2], outputs=[1]):
        self.op_code = op_code
        self.op_title = op_title
        self.content_text = content_text
        self.content_text_objname = content_text_objname

        super().__init__(scene, self.op_title, inputs, outputs)

        path = QPainterPath()
        paint = QPainter()
        paint.setPen(QPen(Qt.white, 10, Qt.SolidLine))
        paint.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        if self.op_code == 1 | self.op_code == 2 | self.op_code == 3:
            path.moveTo(200, 50)
            path.arcTo(150, 0, 50, 50, 0, 90)
            path.arcTo(50, 0, 50, 50, 90, 90)
            path.arcTo(50, 50, 50, 50, 180, 90)
            path.arcTo(150, 50, 50, 50, 270, 90)
            path.lineTo(200, 25)
            self.myPolygon = path.toFillPolygon()
            print(" check 1")
        elif self.op_code == 1:
            myPolygon = QPolygonF([
                QPointF(-100, 0), QPointF(0, 100),
                QPointF(100, 0), QPointF(0, -100),
                QPointF(-100, 0)])
            paint.drawPolygon(myPolygon)
            print("check 2")
        elif self.op_code == 2:
            myPolygon = QPolygonF([
                QPointF(-100, -100), QPointF(100, -100),
                QPointF(100, 100), QPointF(-100, 100),
                QPointF(-100, -100)])
            paint.drawPolygon(myPolygon)
            print("check 3")
        else:
            myPolygon = QPolygonF([
                QPointF(-120, -80), QPointF(-70, 80),
                QPointF(120, 80), QPointF(70, -80),
                QPointF(-120, -80)])
            print("check 4")
            paint.drawPolygon(myPolygon)

    def initInnerClasses(self):
        self.content = CalcContent(self)
        self.grNode = CalcGraphicsNode(self)


