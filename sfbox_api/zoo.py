from .frame import Frame
from .lattice import Lat
from .molecule import Mol
from .monomer import Mon
from .system import Sys


def comb_brush(Nb: int, n: int, m: int, n_layers, sigma: float) -> Frame:
    if n <= 0:
        if m > 1:
            comp = f"(X)1((A){m}){Nb//m-1}(A){m-1}(G)1"
        else:
            comp = f"(X)1((A){m}){Nb//m-1}(G)1"
    else:
        if m > 1:
            comp = f"(X)1((A){m}[(A){n}]){Nb//m-1}(A){m-1}(G)1"
        else:
            comp = f"(X)1((A){m}[(A){n}]){Nb//m-1}(G)1"
    theta = (Nb + 1 + (Nb // m - 1) * n) * sigma
    lat = Lat(**{"n_layers": n_layers, "geometry": "cylindrical"})
    mons = [
        Mon(**{"name": "X", "freedom": "pinned", "pinned_range": "1"}),
        Mon(**{"name": "A", "freedom": "free"}),
        Mon(**{"name": "G", "freedom": "free"}),
        Mon(**{"name": "W", "freedom": "free"}),
    ]
    mols = [
        Mol(**{"name": "Water", "composition": "(W)1", "freedom": "solvent"}),
        Mol(
            **{
                "name": "pol",
                "composition": comp,
                "freedom": "restricted",
                "theta": theta,
            }
        ),
    ]
    sys = Sys()
    chi = 0.0
    chi_list = {"X W": chi, "A W": chi}

    frame = Frame(lat, sys, mols, mons, chi_list=chi_list)
    frame.run()

    return frame


def barbwire(p, n, m, q, n_layers, sigma):
    comp = f"(X)1(A){m-1}([(A){n}]){q}((A){m}([(A){n}]){q}){p-1}(A){m-1}(G)1"
    N = (m + q * n) * p + m
    theta = N * sigma
    lat = Lat(**{"n_layers": n_layers, "geometry": "cylindrical"})
    mons = [
        Mon(**{"name": "X", "freedom": "pinned", "pinned_range": "1"}),
        Mon(**{"name": "A", "freedom": "free"}),
        Mon(**{"name": "G", "freedom": "free"}),
        Mon(**{"name": "W", "freedom": "free"}),
    ]
    mols = [
        Mol(**{"name": "Water", "composition": "(W)1", "freedom": "solvent"}),
        Mol(
            **{
                "name": "pol",
                "composition": comp,
                "freedom": "restricted",
                "theta": theta,
            }
        ),
    ]
    sys = Sys()
    chi = 0.0
    chi_list = {"X W": chi, "A W": chi}

    frame = Frame(lat, sys, mols, mons, chi_list=chi_list)
    frame.run()

    return frame
