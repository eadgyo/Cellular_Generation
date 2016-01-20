from Cellular import Cellular
from cForm import cForm
from Vector3D import Vector3D
class Model:
    def __init__(self, posX, posY, lengthX, lengthY, operations):
        points = []
        points.append(Vector3D(posX, posY))
        points.append(Vector3D(posX + lengthX, posY))
        points.append(Vector3D(posX + lengthX, posY + lengthY))
        points.append(Vector3D(posX, posY + lengthY))

        cellularForm = cForm(points)
        self.root = Cellular(cellularForm, operations[0])

        self.operations = operations
        self.rootActualisation = [self.root]

    def update(self):
        newRootActual = []
        for i in self.rootActualisation:
            i.nextOperation(newRootActual, self.operations)
        self.rootActualisation = newRootActual

    def draw(self, screen):
        self.root.draw(screen)

