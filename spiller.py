class Spiller:
    def __init__(self, navn, farge):
        self._navn = navn
        self._farge = farge
        self._snakeBody = []
        self._snakeBody.append((50,50))
        self._retningX = 1
        self._retningY = 0
        pass

    def endreRettning(self, retning):
        if retning == "up":
            self._retningX = 0
            self._retningY = -1
        elif retning == "down":
            self._retningX = 0
            self._retningY = 1
        elif retning == "left":
            self._retningX = -1
            self._retningY = 0
        elif retning == "right":
            self._retningX = 1
            self._retningY = 0
        pass

    def hentFarge(self):
        return self._farge

    def hentSlange(self):
        return self._snakeBody
