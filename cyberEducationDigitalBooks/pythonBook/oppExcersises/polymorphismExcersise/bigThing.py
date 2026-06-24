class BigThing:

    def __init__(self, thing):
        self.thing = thing

    def size(self):

        if isinstance(self.thing, int):
            return self.thing
        elif isinstance(self.thing, list) or isinstance(self.thing, str) or isinstance(self.thing, dict):
            return len(self.thing)
