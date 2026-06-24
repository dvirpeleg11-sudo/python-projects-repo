from cyberEducationDigitalBooks.pythonBook.oppExcersises.polymorphismExcersise.bigThing import BigThing


class BigCat(BigThing):

    def __init__(self, thing, weight):
        super().__init__(thing)
        self.weight = weight

    def size(self):
        if self.weight > 20:
            return "very fat"
        elif self.weight > 15:
            return "fat"
        else:
            return "okay"
