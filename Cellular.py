from cForm import cForm
from random import random
from Constant import Constant
"""
Cellule pouvant être subdivisée
"""


class Cellular:
    def __init__(self, cellularForm, actualOperation, parent=None, childs=None):
        self.cellularForm = cellularForm

        self.parent = parent
        self.childs = childs

        self.actualOperation = actualOperation

    # On avance d'une opération la cellule
    # Appel par cellularModel
    def nextOperation(self, rootActualisation, operations):
        if len(self.actualOperation.result) == 2:
            # Division

            v0 = self.actualOperation.divideVal + (self.actualOperation.divideProba*(random() - 0.5))
            v1 = self.actualOperation.divideVal + (self.actualOperation.divideProba*(random() - 0.5))
            [cellularForm0, cellularForm1] = self.cellularForm.divide(self.actualOperation.divideVert,
                                                                      v0,
                                                                      v1)

            if cellularForm0.getMinSize() > Constant.SIZE_STOP and cellularForm1.getMinSize() > Constant.SIZE_STOP:
                self.childs = []
                cellularForm0.base = (self.actualOperation.setBase1 + self.cellularForm.base)%2
                cellular0 = Cellular(cellularForm0,
                                 operations[self.actualOperation.result[0]],
                                 self)
                self.childs.append(cellular0)
                rootActualisation.append(cellular0)

                cellularForm1.base = (self.actualOperation.setBase2 + self.cellularForm.base)%2
                cellular1 = Cellular(cellularForm1,
                                 operations[self.actualOperation.result[1]],
                                 self)
                self.childs.append(cellular1)
                rootActualisation.append(cellular1)

        elif len(self.actualOperation.result) == 1:
            # Actualisation état
            self.actualOperation = operations[self.actualOperation.result[0]]
            rootActualisation.append(self)

    def draw(self, screen):
        if self.childs != None:
            for i in self.childs:
                i.draw(screen)
        elif self.actualOperation.name == "Ir" or self.actualOperation.name == "Il":
            self.cellularForm.drawFill(screen)
        else:
            self.cellularForm.draw(screen)

        """

        """
