from cForm import cForm
"""
Cellule pouvant être subdivisée
"""
class Cellular:
    def __init__(self, cellularForm, actualOperation, parent = None, childs = None):
        self.cellularForm = cellularForm

        self.parent = parent
        self.childs = childs

        self.actualOperation = actualOperation

    #On avance d'une opération la cellule
    #Appel par cellularModel
    def nextOperation(self, rootActualisation, operations):
        if len(self.actualOperation.result) == 2:
        #Division
            self.childs = []
            [cellularForm0, cellularForm1] = self.cellularForm.divide(self.actualOperation.divideVert,
                                                                      self.actualOperation.divideVal,
                                                                        self.actualOperation.divideVal)

            #print(self.actualOperation.setBase)
            #cellularForm0.base = self.actualOperation.setBase
            #cellularForm1.base = self.actualOperation.setBase
            cellular0 = Cellular(cellularForm0,
                                 operations[self.actualOperation.result[0]],
                                 self)
            cellular1 = Cellular(cellularForm1,
                                 operations[self.actualOperation.result[1]],
                                 self)

            self.childs.append(cellular0)
            self.childs.append(cellular1)
            rootActualisation.append(cellular0)
            rootActualisation.append(cellular1)

        elif len(self.actualOperation.result) == 1:
        #Actualisation état
            self.actualOperation = operations[self.actualOperation.result[0]]
            rootActualisation.append(self)


    def draw(self, screen):
        if self.childs != None:
            for i in self.childs:
                i.draw(screen)
        if len(self.actualOperation.result) != 0:
            self.cellularForm.draw(screen)