from sfbox_api import Frame, Lat, Mol, Mon, Sys

if __name__ == "__main__":
    lat = Lat(**{"geometry": "flat", "n_layers": 100})

    mols = []
    mols.append(Mol(**{"name": "water", "composition": "(W)1", "freedom": "solvent"}))
    mols.append(
        Mol(
            **{
                "name": "pol",
                "composition": "(X)1(A)98(G)1",
                "freedom": "restricted",
                "theta": 5.0,
            }
        )
    )

    mons = []
    mons.append(Mon(**{"name": "W", "freedom": "free"}))
    mons.append(Mon(**{"name": "X", "freedom": "pinned", "pinned_range": "1"}))
    mons.append(Mon(**{"name": "A", "freedom": "free"}))
    mons.append(Mon(**{"name": "G", "freedom": "free"}))

    sys = Sys()

    chi_list = {"X W": 0.2, "A W": 0.5}

    frame = Frame(lat, sys, mols, mons, chi_list=chi_list)

    frame.run()

    print(frame.profile_labels)
    # print(frame.profile["water"])

    print(frame.stats_labels)
    print(frame.stats["sys : name : free energy"])
