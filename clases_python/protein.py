import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Protein():

    def __init__(self, atoms=[]):
        self.atoms = atoms

    def add_atom(self, atom):
        self.atoms.append(atom)

    def get_cord_xyz(self, atom_idx):
        return self.atoms[atom_idx].get_xyz()

    #translate(self, vector):
        #for atom in atoms:
            #atom.translate(vector)

    def plot(self, same_plot=False, color="blue"):

        x_cor = []
        y_cor = []
        z_cor = []

        for atom in self.atoms:
            x, y, z = atom.get_xyz() #no se pone atributo porque el atributo de la funcion esta definido en la clase atom como self
            x_cor.append(x)
            y_cor.append(y)
            z_cor.append(z)

        # Creating figure
        if not same_plot:
            fig = plt.figure(figsize=(10, 7))
            ax = plt.axes(projection="3d")
            ax.scatter3D(x_cor, y_cor, z_cor, color=color)
            plt.title("simple 3D scatter plot")
            return ax
        else:
            same_plot.scatter3D(x_cor, y_cor, z_cor, color=color)
            plt.title("simple 3D scatter plot")
            return same_plot


        # Creating plot


    def translate(self, module, direction):
        for atom in self.atoms:
            atom.translate(module, direction)

    def rotate(self):
        for atom in self.atoms:
            atom.rotate()



