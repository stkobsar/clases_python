
class Atom():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_xyz(self):
        return self.x, self.y, self.z

    def translate(self, module, direction):
        self.x = self.x + module*direction[0]
        self.y = self.y + module * direction[1]
        self.z = self.z + module * direction[2]



    #translat(self, vector):
    ####RTrasladar el atomo