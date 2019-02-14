#!/usr/bin/python3

"""
Sample program that uses a generated GRIP pipeline to detect red areas in an image and publish them to NetworkTables.
"""

import cv2
import urllib
import networktables
import numpy
from networktables import NetworkTables
from networktables2 import NumberArray
from S_proc import GripPipeline
import datetime
from time import sleep

import logging
logging.basicConfig(level=logging.DEBUG)


def extra_processing(pipeline):
	"""
	Performs extra processing on the pipeline's outputs and publishes data to NetworkTables.
	:param pipeline: the pipeline that just processed an image
	:return: None
	"""
	'''center_x_value = []'''
	# Find the bounding boxes of the contours to get x, y, width, and height
	for contour in pipeline.filter_contours_output:
		
		
		x, y, w, h = cv2.boundingRect(contour)
		print(contour)
		
		'''Orig = 102
		Tru_H = 119
		adj_ang = np.arccos( (w * h) / ( Orig *Tru_H))
		print(adj_ang)'''
		''' dista = (Tru_H'''
	# Publish to the '/vision' network table
	sd = NetworkTable.getTable("/vision")
	sd.putValue("adjust", dist)

def main():
	
	print('Initializing NetworkTables')
	NetworkTable.setClientMode()
	NetworkTable.setIPAddress('localhost')
	NetworkTable.initialize()

	print('Creating video capture')
	cap = cv2.VideoCapture(0)

	print('Creating pipeline')
	pipeline = GripPipeline()

	print('Running pipeline')
	while cap.isOpened():
		have_frame, frame = cap.read()
		if have_frame:
			pipeline.process(frame)
			extra_processing(pipeline)

	print('Capture closed')



if __name__ == '__main__':
	main()
