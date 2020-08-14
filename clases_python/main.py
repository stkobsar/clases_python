import clases_python.atom as at
import clases_python.protein as pt


def read_file_pdb(file):
    protein = pt.Protein([]) #crear objeto protein vacio

    with open(file, "r") as f:
        contents = f.readlines()
    for content in contents:
        if content.startswith("ATOM"):
            x = float(content[31:38])
            y = float(content[40:46])
            z = float(content[47:54])
            atom = at.Atom(x, y, z)
            protein.add_atom(atom) #añadir atom a clas protein mediante el método creado en la clase
    #print(protein.atoms[0].x) get coordenate x of first atom
    return protein


if __name__ == "__main__":
    protein = read_file_pdb("data/4m5k.pdb")
    protein.plot()
    #protein.translate([1,1,1])
    #protein.plot