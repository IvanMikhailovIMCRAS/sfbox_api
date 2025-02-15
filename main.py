from sfbox_api import Composition, barbwire, polyacid

if __name__ == "__main__":
    # Demonstrate working across different folders
    frame = polyacid(N=100, sigma=0.16, pK=1.0, ionic_strength=1e-3, chi=0.5)
    print(frame.profile_labels)
    frame.run("123")
    print(frame.profile_labels)
    # Demonstrate the implementation of a special frame
    bw = barbwire(p=3, n=100, m=100, q=2, root=2, theta=5, chi=0, n_layers=200)
    print(bw.profile_labels)
    # Calculation of the polymerization degree
    C = Composition("(x2)1(c5)5(c5)2(e2)1")
    print(C.N)
