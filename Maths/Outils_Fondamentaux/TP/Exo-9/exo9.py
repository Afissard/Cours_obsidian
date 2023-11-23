import numpy as np

def diagonale (matriceA):
    if matriceA == len(matriceA[1]):
        matriceB = 0
    else :
        matriceB = matriceA
    return matriceB

def main():
    matriceA = np.array([[2,3], [4,5]])
    print("diagonale de :\n", matriceA, "\n=>\n", diagonale(matriceA))

if __name__ == "__main__":
    main()