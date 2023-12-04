from sfbox_api import comb_brush

if __name__ == "__main__":
    brush = comb_brush(Nb=100, n=10, m=4, n_layers=100, sigma=0.01)

    print(brush.profile_labels)
