class Operation:
    # @param:    name       -- String           -- nom de l'étape
    #           result      -- List[0, 1 ou 2]  -- index operations à réaliser
    #           divideVert  -- Integer          -- 1 -> division verticale ou 0 -> horizontale
    #           divideVal   -- Float            -- position découpe sur le vecteur
    #           divideProba -- Float            -- valeur variation val
    #           setBase1    -- entier           -- nouvelle base suite à la division pour la premiere forme créee
    #           setBase2    -- entier           -- nouvelle base suite à la division pour la seconde forme créee
    def __init__(self, name, result, divideVert, divideVal, divideProba, setBase1 = 0, setBase2 = 0):
        self.name = name
        self.result = result  # liste 2 max
        self.divideVert = divideVert
        self.divideVal = divideVal
        self.divideProba = divideProba
        self.setBase1 = setBase1
        self.setBase2 = setBase2 #Il 1
