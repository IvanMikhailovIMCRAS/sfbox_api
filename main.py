from sfbox_api import barbwire, polyacid

if __name__ == "__main__":
    frame = polyacid(N=100, sigma=0.16, pK=1.0, ionic_strength=1e-3, chi=0.5)
    print(frame.profile_labels)

    bw = barbwire(p=3, n=100, m=100, q=2, root=2, theta=5, chi=0, n_layers=200)
    print(bw.profile_labels)
