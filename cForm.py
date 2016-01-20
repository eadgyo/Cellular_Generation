from Vector3D import Vector3D

"""
Quadrilatère quelconque utilisée pour la création des cellules
"""


class cForm:
    def __init__(self, points):
        self.points = points  # L'ordre a de l'importance
        self.base = 0

    # Divise la forme en 2
    # @param:    seg0 -- entier -- position dans l'index de la liste de segments
    #           val0 -- float  -- position découpe premier segment
    #           val1 -- float  -- position découpe second segment
    def divide(self, seg0, val0, val1):
        assert (seg0 <= 4 and seg0 >= 0)
        assert (val0 >= 0.0 and val0 <= 1.0), val0
        assert (val1 >= 0.0 and val1 <= 1.0), val1
        seg0 = (self.base + seg0)%2
        seg1 = (seg0 + 2) % 4

        # Calcul des vecteurs des 2 segments
        vec0 = Vector3D(self.points[seg0], self.points[(seg0 + 1) % 4])
        vec1 = Vector3D(self.points[(seg1 + 1) % 4], self.points[seg1])

        # Calcul de la position des points
        pos0 = vec0 * val0 + self.points[seg0]
        pos1 = vec1 * val1 + self.points[(seg1 + 1) % 4]

        # Création des nouvelles formes
        points0 = []
        points1 = []
        if seg0 == 1:
            # Horizontal
            points0.append(self.points[0])
            points0.append(self.points[1])
            points0.append(pos0)
            points0.append(pos1)

            points1.append(pos1)
            points1.append(pos0)
            points1.append(self.points[2])
            points1.append(self.points[3])


        else:
            # Vertical
            points0.append(self.points[0])
            points0.append(pos0)
            points0.append(pos1)
            points0.append(self.points[3])

            points1.append(pos0)
            points1.append(self.points[1])
            points1.append(self.points[2])
            points1.append(pos1)

        return [cForm(points0), cForm(points1)]

    # Divise la forme en 2 avec une gestion de la pente
    # @param:    seg0 -- entier -- position dans l'index de la liste de segments
    #           val0 -- float  -- position découpe premier segment
    #           val1 -- float  -- position découpe second segment
    def normalizeDivide(self, seg0, val0, val1):
        assert (4 >= seg0 >= 0)
        assert (0.0 <= val0 <= 1.0)
        assert (0.0 <= val1 <= 1.0)
        seg1 = (seg0 + 2) % 4

        # Calcul des vecteurs des 2 segments
        vec0 = Vector3D(self.points[seg0], self.points[(seg0 + 1) % 4])
        vec1 = Vector3D(self.points[seg1], self.points[(seg1 + 1) % 4])

        # Normalization
        vec0N = vec0.copy()
        magn = vec0N.normalize()
        scalar = vec0N * vec1
        # On recherche le plus petit coté par projection
        assert (scalar >= 0.0)
        if scalar <= 1.0:
            max = scalar
            val1 = magn * val1 / max
        else:
            vec1N = vec1.copy()
            magn2 = vec1N.normalize()
            vec1N.normalize()
            max = scalar * magn / magn2
            val0 = magn2 * val0 / max

        # Calcul de la position des points
        pos0 = vec0 * val0 + self.points[seg0]
        pos1 = vec1 * val1 + self.points[seg1]

        # Création des nouvelles formes
        points0 = []
        points1 = []

        points0.append(self.points[(seg1 + 1) % 4], self.points[seg0], pos0, pos1)
        points1.append(self.points[(seg0 + 1) % 4], self.points[seg1], pos1, pos0)

        return [cForm(points0), cForm(points1)]

    def getMinSize(self):
        min = -1
        for i in range(len(self.points)):
            vec = self.points[(i+1)%4] - self.points[i]
            sqMagn = vec.getMagnitude()
            if sqMagn > min:
                min = sqMagn
        return min

    def draw(self, screen):
        vec = Vector3D(100, 300, 0, 0)
        a = 0  # 1.5
        ps = []
        for i in range(len(self.points)):
            ps.append(self.points[i].getRotatedZ(a) + vec)

        for i in range(len(self.points)):
            screen.create_line(ps[i].getX(), ps[i].getY(), ps[(i + 1)%4].getX(), ps[(i + 1)%4].getY())

    def drawFill(self, screen):
        vec = Vector3D(100, 300, 0, 0)
        a = 0  # 1.5
        ps = []
        for i in range(len(self.points)):
            ps.append(self.points[i].getRotatedZ(a) + vec)

        screen.create_polygon(  ps[0].getX(), ps[0].getY(),
                                ps[1].getX(), ps[1].getY(),
                                ps[2].getX(), ps[2].getY(),
                                ps[3].getX(), ps[3].getY(),
                                fill='red')
