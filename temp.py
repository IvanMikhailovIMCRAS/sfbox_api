from sfbox_api import Frame, Lat, Mol, Mon, Sys


def comb_brush(Nb: int, n: int, m: int, n_layers, sigma: float) -> Frame:
    if n <= 0:
        comp = f"(X)1((A){m}){Nb//m-1}(A){m}"
    else:
        comp = f"(X)1((A){m}[(A){n}]){Nb//m-1}(A){m}"
    theta = (Nb + 1 + (Nb // m - 1) * n) * sigma
    lat = Lat(
        **{
            "n_layers": n_layers,
            "geometry": "flat",
            "lowerbound": "surface",
            "upperbound": "surface",
        }
    )
    mons = [
        Mon(**{"name": "X", "freedom": "pinned", "pinned_range": "1"}),
        Mon(**{"name": "A", "freedom": "free"}),
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


if __name__ == "__main__":
    frame = comb_brush(Nb=100, n=10, m=20, n_layers=100, sigma=0.01)
    print(frame.profile_labels)
