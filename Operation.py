class Operation:
    # @param:    name        -- String           -- nom de l'étape
    #           result      -- List[0, 1 ou 2]  -- index operations à réaliser
    #           divideVert  -- Integer          -- 1 -> division verticale ou 0 -> horizontale
    #           divideVal   -- Float            -- position découpe sur le vecteur
    #           divideProba -- Float            -- pourcentage variation val
    def __init__(self, name, result, divideVert, divideVal, divideProba, setBase):
        self.name = name
        self.result = result  # liste 2 max
        self.divideVert = divideVert
        self.divideVal = divideVal
        self.divideProba = divideProba
        self.setBase = setBase
