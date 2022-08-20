import imageio.v2 as imageio
import os
import glob

images = []

path = 'images'
for filename in sorted(glob.glob(os.path.join(path, 'Page*.png'))):
    images.append(imageio.imread(filename))

imageio.mimsave('images/alphaBeta.gif', images, duration=1)