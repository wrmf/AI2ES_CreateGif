import imageio.v2 as imageio
import os
import glob

images = []

path = ''
for filename in sorted(glob.glob(os.path.join(path, '*.png'))):
    images.append(imageio.imread(filename))

imageio.mimsave('alphaBeta.gif', images, duration=1)