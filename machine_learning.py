# Learning project to develop and experiment with machine learning
import numpy as np

def main():
    x = np.asmatrix([(2,1,1),(1,2,1),(1,1,2)])

    i = 0
    j = 0
    for i in x[2]:
        for j in x[2]:
            y = max(i)
            z = max(j)
            x[y,z] = 3
            print(x)

main()
