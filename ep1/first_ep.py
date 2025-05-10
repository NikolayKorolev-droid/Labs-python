import numpy as np
import matplotlib.pyplot as plt

def ReadPoints(filename):
    with open(filename+'.dat', 'r') as f:
        points = []
        lines = f.readlines()
        n = int(lines[0].strip())
        for i in range(1, n+1):
            x,y = map(float, lines[i].strip().split())
            points.append((x, y))
        return n, points

def MakeGraph(filename):
    n, points = ReadPoints(filename)
    x = [k[0] for k in points]
    y = [k[1] for k in points]
    fig, ax = plt.subplots(figsize=(10, 10))
    x_min, x_max = min(x), max(x)
    y_min, y_max = min(y), max(y)

    ax.scatter(x, y, color='blue')
    ax.grid(True, linestyle='-', alpha=0.5)
    ax.set_title(f"Число точек: {n}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    ax.set_aspect('equal')
    output=f"graphic_{filename}.png"
    plt.savefig(output)
    plt.show()

def main():
    files=['001', '002', '003', '004', '005']
    for file in files:
        MakeGraph(file)

if __name__=="__main__":
    main()