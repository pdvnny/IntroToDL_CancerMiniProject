"""********************************************************

	Parker Dunn (pgdunn@bu.edu -- parker_dunn@outlook.com)

	Script to convert images to a rows in a CSV file

********************************************************"""

import glob
import numpy as np
from skimage import io
import multiprocessing as mlt

def load_image(file, img_lst):
	img = io.imread(file)
	img_lst.append(img)


if __name__ == "__main__":
	print("Starting...")
	locs = glob.glob("test/*.tif")

	# Setup
	n = 10000  # number of images to load
	images = np.zeros((n, 96, 96, 3))

	manager = mlt.Manager()

	i = 0
	while i < len(locs[0:n]):
		return_lst = manager.list()
		jobs = []

		for ll in range(4):
			if i < len(locs):
				p = mlt.Process(target=load_image, args=(locs[i], return_lst))
				i += 1
				jobs.append(p)
				p.start()

		for pp in jobs:
			pp.join()

		for ii in range(i-4,i):
			images[ii,:,:,:] = return_lst[(ii-i)]

	print(images[0,0,0,:])
	print(images[-1,0,0,:])
