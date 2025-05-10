import matplotlib.pyplot as plt
import imageio.v2 as imageio

x = []
y = []
with open("2.dat", 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 2):
        x.append([float(x) for x in lines[i].split()])
        y.append([float(y) for y in lines[i+1].split()])

n_frames = len(x)
x_min= min([min(k) for k in x])
x_max = max([max(k) for k in x])
y_min = min([min(k) for k in y])
y_max = max([max(k) for k in y])

images = []
for i in range(n_frames):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.grid(True, linestyle='-')
    ax.plot(x[i], y[i], color='blue')
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_title(f"Кадр {i+1}", fontsize=14)
    output = f"frame_{i+1}.png"
    plt.savefig(output)
    plt.close(fig)
    images.append(output)

