import imageio.v2 as imageio
import os
import glob

images = []

path = 'output'
for filename in sorted(glob.glob(os.path.join(path, '*.png'))):
    images.append(imageio.imread(filename))
    print(f"Added {filename}")

imageio.mimsave(f'{path}/gif.gif', images, duration=1)