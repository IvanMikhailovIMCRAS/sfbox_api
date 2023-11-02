import os

TARGET_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/data"


def create_template_pro() -> None:
    with open(f"{TARGET_DIR}/profile.tmp", "w") as f:
        f.writelines("mol : pol : phi : profile")


def run() -> None:
    content = f"""
    lat : flat : n_layers : 150
    lat : flat : geometry : flat
    lat : flat : lambda : 0.16666666666666666667
    lat : flat : lowerbound : surface
    lat : flat : upperbound : mirror1
    lat : flat : bondlength : 3e-10
    
    sys : ivan : temperature : 300

    mon : solid : freedom : frozen
    mon : solid : frozen_range : lowerbound
    
    mon : W : freedom : free
    
    mon : X: freedom : pinned
    mon : X : pinned_range : 1
    mon : X : valence : 0.6
    
    mon : A : freedom : free
    mon : A : valence : 0.6
    
    mon : M : freedom : free
    mon : M : valence : -1
    
    mon : P : freedom : free
    mon : P : valence : 1
    
    mol : ionm : composition : (M)1
    mol : ionm : freedom : neutralizer
    
    mol : ionp : composition : (P)1
    mol : ionp : freedom : free
    mol : ionp : phibulk : 1e-05
    
    mol : solvent : composition : (W)1
    mol : solvent : freedom : solvent

    mol : pol : composition : (X)1(A)30([(A)30])3(A)30
    mol : pol : freedom : restricted
    mol : pol : theta : 5.0

    output : filename.pro : type : profiles
    output : filename.pro : template : {f"{TARGET_DIR}/profile.tmp"}
    
    newton : mynew : tolerance : 1e-7

    start    
    """

    create_template_pro()
    with open(f"{TARGET_DIR}/input.in", "w") as f:
        f.writelines(content)
    os.chdir(TARGET_DIR)
    os.system(f"{TARGET_DIR}/sfbox {TARGET_DIR}/input.in >> info.txt")
