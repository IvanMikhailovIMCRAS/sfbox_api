import matplotlib.pyplot as plt

from sfbox_api import barbwire, comb_brush

if __name__ == "__main__":
    brush = barbwire(p=4, n=200, m=50, q=5, n_layers=100, sigma=0.05)

    print(brush.profile_labels)

    plt.plot(brush.profile["layer"], brush.profile["G"])
    plt.show()
