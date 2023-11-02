import os
from typing import Dict, List

from .composition import Composition
from .lattice import Lat
from .molecule import Mol
from .monomer import Mon
from .system import Sys

TARGET_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/data"


class Frame:
    def __init__(
        self,
        lat: Lat,
        sys: Sys,
        mols: List[Mol],
        mons: List[Mon],
        chi_list: Dict = dict(),
    ) -> None:
        self.lat = lat
        self.sys = sys
        self.mols = mols
        self.mons = mons
        self.chi_list = chi_list

        list_mons_names = []
        for m in mons:
            list_mons_names.append(m.name)

        self.compositions = []
        for mol in mols:
            self.compositions.append(Composition(mol.composition))

        list_mons_compare = []
        for comp in self.compositions:
            list_mons_compare += comp.types_list()

        if set(list_mons_names) != set(list_mons_compare):
            raise ValueError(
                f"Set monomers: {list_mons_names}, but {list_mons_compare} used in molecules"
            )

    def __str__(self):
        result = ""
        for p in self.lat:
            if p[1] and p[1] != self.lat.name:
                if p[0] == "lambda1":
                    result += f"lat : {self.lat.name} : lambda : {str(p[1])} \n"
                else:
                    result += f"lat : {self.lat.name} : {p[0]} : {str(p[1])} \n"
        for p in self.sys:
            if p[1] and p[1] != self.sys.name:
                result += f"sys : {self.sys.name} : {p[0]} : {str(p[1])} \n"
        for mon in self.mons:
            for p in mon:
                if p[1] and p[1] != mon.name:
                    result += f"mon : {mon.name} : {p[0]} : {str(p[1])} \n"
        for mol in self.mols:
            for p in mol:
                if p[1] and p[1] != mol.name:
                    result += f"mol : {mol.name} : {p[0]} : {str(p[1])} \n"
        result += "output : filename.pro : type : profiles \n"
        result += f"output : filename.pro : template : {TARGET_DIR}/profile.tmp \n"
        result += "output : filename.kal : type : kal \n"
        result += f"output : filename.kal : template : {TARGET_DIR}/kal.tmp \n"
        result += "start"
        return result

    def run(self):
        f = open(f"{TARGET_DIR}/info.txt", "w")
        f.close()
        f = open(f"{TARGET_DIR}/input.pro", "w")
        f.close()
        with open(f"{TARGET_DIR}/profile.tmp", "w") as f:
            f.writelines("mol : * : phi : profile \n")
            f.writelines("mon : * : phi : profile")
        with open(f"{TARGET_DIR}/kal.tmp", "w") as f:
            f.writelines("sys : * : free energ* : 1 \n")
            f.writelines("mol : * : ln(G* : 1)")
        with open(f"{TARGET_DIR}/input.in", "w") as f:
            f.write(str(self))
        os.chdir(TARGET_DIR)
        os.system(f"{TARGET_DIR}/sfbox {TARGET_DIR}/input.in >> info.txt")