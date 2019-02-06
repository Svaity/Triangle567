# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
	# define multiple sets of tests as functions with names that begin

	def testRightTriangleA(self):
		self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

	def testRightTriangleB(self):
		self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

	def testEquilateralTriangles(self):
		self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
		self.assertEqual(classifyTriangle(3,3,3),'Equilateral','1,1,1 should be equilateral')
		self.assertEqual(classifyTriangle(7,7,7),'Equilateral','1,1,1 should be equilateral')


	def testset1(self):
		"""where everyhing is right (Even Isoceles)"""
		self.assertEqual(classifyTriangle(3, 3, 3), "Equilateral")
		self.assertEqual(classifyTriangle(3, 4, 5), "Right")
		self.assertEqual(classifyTriangle(3, 4, 3), "Isoceles")

	def testset6(self):
		"""wierd values"""
		self.assertEqual(classifyTriangle(1.34, 4, 3), "InvalidInput")
		self.assertEqual(classifyTriangle(4443, 4443, 33), "InvalidInput")

	def testset2(self):
		"""where everything can go wrong """
		with self.assertRaises(NameError):
			classifyTriangle(g, 4, 5)
		with self.assertRaises(TypeError):
			classifyTriangle("a", 5, 6)

	def testset4(self):
		"""not valid"""
		self.assertEqual(classifyTriangle(-2,4,3),"InvalidInput")
		self.assertEqual(classifyTriangle(0, 3, 4), "InvalidInput")

	def testset(self):
		"""Check fro Scalene"""
		self.assertEqual(classifyTriangle(2, 3, 4), "Scalene")

	def testset3(self):
		"""where thing are not correct"""
		self.assertNotEqual(classifyTriangle(3, 4, 3), "Equilateral")
		self.assertNotEqual(classifyTriangle(3, 3, 6), "Right")


if __name__ == '__main__':
	print('Running unit tests')
	unittest.main()

