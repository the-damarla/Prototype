from examples.calculator.calc_conf import *
from examples.calculator.calc_node_base import *


@register_node(OP_NODE_SQR)
class CalcNode_Add(CalcNode):
    def __init__(self, scene):
        super().__init__(scene, OP_NODE_SQR, "Square", "")


@register_node(OP_NODE_REC)
class CalcNode_Add(CalcNode):
    def __init__(self, scene):
        super().__init__(scene, OP_NODE_REC, "Rectangle", "")


@register_node(OP_NODE_RMB)
class CalcNode_Add(CalcNode):
    def __init__(self, scene):
        super().__init__(scene, OP_NODE_RMB, "Rhombus", "")
