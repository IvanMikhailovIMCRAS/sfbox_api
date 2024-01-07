from sfbox_api import polyacid

if __name__ == "__main__":
    frame = polyacid(N=100, sigma=0.16, pK=2.0, ionic_strength=1e-3, chi=0.5)
    print(frame.profile_labels)
