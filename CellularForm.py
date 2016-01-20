from Vector3D import Vector3D
import math
"""
Quadrilatère quelconque utilisée pour la création des cellules
"""
class CellularForm:
    def __init__(self, points):
        self.points = points #L'ordre a de l'importance
        self.base = 0

    #Divise la forme en 2
    #@param:    seg0 -- entier -- position dans l'index de la liste de segments
    #           val0 -- float  -- position découpe premier segment
    #           val1 -- float  -- position découpe second segment
    def divide(self, seg0, val0, val1):
        assert(seg0 <= 4 and seg0 >= 0)
        assert(val0 >= 0.0 and val0 <= 1.0)
        assert(val1 >= 0.0 and val1 <= 1.0)
        print(self.base)
        seg0 = (seg0 + self.base)%4
        seg1 = (seg0 + 2)%4

        #Calcul des vecteurs des 2 segments
        vec0 = Vector3D(self.points[seg0], self.points[(seg0 + 1)%4])
        vec1 = Vector3D(self.points[(seg1 + 1)%4], self.points[seg1])

        #Calcul de la position des points
        pos0 = vec0*val0 + self.points[seg0]
        pos1 = vec1*val1 + self.points[(seg1 + 1)%4]

        #Création des nouvelles formes
        points0 = []
        points1 = []

        points0.append(self.points[(seg1 + 1)%4])
        points0.append(self.points[seg0])
        points0.append(pos0)
        points0.append(pos1)

        points1.append(self.points[seg1])
        points1.append(self.points[(seg0 + 1)%4])
        points1.append(pos0)
        points1.append(pos1)

        return [CellularForm(points0), CellularForm(points1)]

    #Divise la forme en 2 avec une gestion de la pente
    #@param:    seg0 -- entier -- position dans l'index de la liste de segments
    #           val0 -- float  -- position découpe premier segment
    #           val1 -- float  -- position découpe second segment
    def normalizeDivide(self, seg0, val0, val1):
        assert(seg0 <= 4 and seg0 >= 0)
        assert(val0 >= 0.0 and val0 <= 1.0)
        assert(val1 >= 0.0 and val1 <= 1.0)
        seg1 = (seg0 + 2)%4

        #Calcul des vecteurs des 2 segments
        vec0 = Vector3D(self.points[seg0], self.points[(seg0 + 1)%4])
        vec1 = Vector3D(self.points[seg1], self.points[(seg1 + 1)%4])

        #Normalization
        vec0N = vec0.copy()
        magn = vec0N.normalize()
        scalar = vec0N*vec1
        #On recherche le plus petit coté par projection
        assert(scalar >= 0.0)
        if scalar <= 1.0:
            max = scalar
            val1 = magn*val1/max
        else:
            vec1N = vec1.copy()
            magn2 = vec1N.normalize()
            vec1N.normalize()
            max = scalar*magn/magn2
            val0 = magn2*val0/max

        #Calcul de la position des points
        pos0 = vec0*val0 + self.points[seg0]
        pos1 = vec1*val1 + self.points[seg1]

        #Création des nouvelles formes
        points0 = []
        points1 = []

        points0.append(self.points[(seg1 + 1)%4], self.points[seg0], pos0, pos1)
        points1.append(self.points[(seg0 + 1)%4], self.points[seg1], pos1, pos0)

        return [CellularForm(points0), CellularForm(points1)]

    def draw(self, screen):
        for i in range(len(self.points)):
            a = 1.5
            vec = Vector3D(100, 300, 0, 0)
            p0 = self.points[i].getRotatedZ(a) + vec
            p1 = self.points[(i + 1)%4].getRotatedZ(a) + vec
            screen.create_line(p0.getX(),
                               p0.getY(),
                               p1.getX(),
                               p1.getY())
            """
            screen.create_line(self.points[i].getX(),
                               self.points[i].getY(),
                               self.points[(i + 1)%4].getX(),
                               self.points[(i + 1)%4].getY())
            """