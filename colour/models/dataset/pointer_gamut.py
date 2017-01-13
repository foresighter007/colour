#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pointer's Gamut
===============

Defines *Pointer's Gamut* data.

See Also
--------
`RGB Colourspaces Jupyter Notebook
<http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/\
blob/master/notebooks/models/rgb.ipynb>`_

References
----------
.. [1]  Pointer, M. R. (1980). Pointer’s Gamut Data. Retrieved from
        http://www.cis.rit.edu/research/mcsl2/online/PointerData.xls
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.colorimetry import LIGHT_SOURCES

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2016 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['POINTER_GAMUT_ILLUMINANT',
           'POINTER_GAMUT_DATA',
           'POINTER_GAMUT_BOUNDARIES']

POINTER_GAMUT_ILLUMINANT = (
    LIGHT_SOURCES['CIE 1931 2 Degree Standard Observer']['SC'])
"""
*Pointer's Gamut* illuminant *SC*.

POINTER_GAMUT_ILLUMINANT : ndarray
"""

POINTER_GAMUT_DATA = np.array([
    [15, 10, 0],
    [15, 15, 10],
    [15, 14, 20],
    [15, 35, 30],
    [15, 27, 40],
    [15, 10, 50],
    [15, 4, 60],
    [15, 5, 70],
    [15, 6, 80],
    [15, 4, 90],
    [15, 9, 100],
    [15, 9, 110],
    [15, 4, 120],
    [15, 5, 130],
    [15, 7, 140],
    [15, 7, 150],
    [15, 8, 160],
    [15, 13, 170],
    [15, 10, 180],
    [15, 7, 190],
    [15, 5, 200],
    [15, 0, 210],
    [15, 2, 220],
    [15, 10, 230],
    [15, 8, 240],
    [15, 9, 250],
    [15, 12, 260],
    [15, 14, 270],
    [15, 10, 280],
    [15, 20, 290],
    [15, 30, 300],
    [15, 62, 310],
    [15, 60, 320],
    [15, 20, 330],
    [15, 26, 340],
    [15, 15, 350],
    [20, 30, 0],
    [20, 30, 10],
    [20, 34, 20],
    [20, 48, 30],
    [20, 40, 40],
    [20, 21, 50],
    [20, 15, 60],
    [20, 15, 70],
    [20, 15, 80],
    [20, 12, 90],
    [20, 16, 100],
    [20, 18, 110],
    [20, 14, 120],
    [20, 18, 130],
    [20, 20, 140],
    [20, 21, 150],
    [20, 24, 160],
    [20, 25, 170],
    [20, 25, 180],
    [20, 19, 190],
    [20, 19, 200],
    [20, 12, 210],
    [20, 12, 220],
    [20, 20, 230],
    [20, 16, 240],
    [20, 21, 250],
    [20, 24, 260],
    [20, 31, 270],
    [20, 29, 280],
    [20, 40, 290],
    [20, 55, 300],
    [20, 76, 310],
    [20, 71, 320],
    [20, 50, 330],
    [20, 49, 340],
    [20, 37, 350],
    [25, 43, 0],
    [25, 45, 10],
    [25, 49, 20],
    [25, 59, 30],
    [25, 53, 40],
    [25, 34, 50],
    [25, 26, 60],
    [25, 25, 70],
    [25, 24, 80],
    [25, 20, 90],
    [25, 23, 100],
    [25, 27, 110],
    [25, 23, 120],
    [25, 30, 130],
    [25, 32, 140],
    [25, 34, 150],
    [25, 36, 160],
    [25, 36, 170],
    [25, 38, 180],
    [25, 30, 190],
    [25, 29, 200],
    [25, 17, 210],
    [25, 20, 220],
    [25, 29, 230],
    [25, 26, 240],
    [25, 32, 250],
    [25, 34, 260],
    [25, 42, 270],
    [25, 45, 280],
    [25, 60, 290],
    [25, 72, 300],
    [25, 85, 310],
    [25, 79, 320],
    [25, 72, 330],
    [25, 63, 340],
    [25, 52, 350],
    [30, 56, 0],
    [30, 56, 10],
    [30, 61, 20],
    [30, 68, 30],
    [30, 66, 40],
    [30, 45, 50],
    [30, 37, 60],
    [30, 36, 70],
    [30, 32, 80],
    [30, 28, 90],
    [30, 30, 100],
    [30, 35, 110],
    [30, 32, 120],
    [30, 40, 130],
    [30, 42, 140],
    [30, 45, 150],
    [30, 48, 160],
    [30, 47, 170],
    [30, 48, 180],
    [30, 40, 190],
    [30, 37, 200],
    [30, 26, 210],
    [30, 28, 220],
    [30, 36, 230],
    [30, 34, 240],
    [30, 40, 250],
    [30, 41, 260],
    [30, 50, 270],
    [30, 55, 280],
    [30, 69, 290],
    [30, 81, 300],
    [30, 88, 310],
    [30, 84, 320],
    [30, 86, 330],
    [30, 73, 340],
    [30, 65, 350],
    [35, 68, 0],
    [35, 64, 10],
    [35, 69, 20],
    [35, 75, 30],
    [35, 79, 40],
    [35, 60, 50],
    [35, 48, 60],
    [35, 46, 70],
    [35, 40, 80],
    [35, 36, 90],
    [35, 37, 100],
    [35, 44, 110],
    [35, 41, 120],
    [35, 48, 130],
    [35, 52, 140],
    [35, 57, 150],
    [35, 58, 160],
    [35, 57, 170],
    [35, 57, 180],
    [35, 48, 190],
    [35, 42, 200],
    [35, 34, 210],
    [35, 35, 220],
    [35, 42, 230],
    [35, 41, 240],
    [35, 49, 250],
    [35, 46, 260],
    [35, 55, 270],
    [35, 60, 280],
    [35, 71, 290],
    [35, 79, 300],
    [35, 85, 310],
    [35, 85, 320],
    [35, 89, 330],
    [35, 82, 340],
    [35, 73, 350],
    [40, 77, 0],
    [40, 70, 10],
    [40, 74, 20],
    [40, 82, 30],
    [40, 90, 40],
    [40, 75, 50],
    [40, 59, 60],
    [40, 56, 70],
    [40, 48, 80],
    [40, 44, 90],
    [40, 45, 100],
    [40, 52, 110],
    [40, 49, 120],
    [40, 56, 130],
    [40, 60, 140],
    [40, 68, 150],
    [40, 68, 160],
    [40, 65, 170],
    [40, 64, 180],
    [40, 55, 190],
    [40, 45, 200],
    [40, 43, 210],
    [40, 40, 220],
    [40, 46, 230],
    [40, 47, 240],
    [40, 54, 250],
    [40, 51, 260],
    [40, 60, 270],
    [40, 61, 280],
    [40, 69, 290],
    [40, 72, 300],
    [40, 80, 310],
    [40, 86, 320],
    [40, 89, 330],
    [40, 87, 340],
    [40, 79, 350],
    [45, 79, 0],
    [45, 73, 10],
    [45, 76, 20],
    [45, 84, 30],
    [45, 94, 40],
    [45, 90, 50],
    [45, 70, 60],
    [45, 67, 70],
    [45, 55, 80],
    [45, 53, 90],
    [45, 51, 100],
    [45, 59, 110],
    [45, 57, 120],
    [45, 64, 130],
    [45, 69, 140],
    [45, 75, 150],
    [45, 76, 160],
    [45, 70, 170],
    [45, 69, 180],
    [45, 59, 190],
    [45, 46, 200],
    [45, 49, 210],
    [45, 45, 220],
    [45, 49, 230],
    [45, 49, 240],
    [45, 55, 250],
    [45, 55, 260],
    [45, 60, 270],
    [45, 60, 280],
    [45, 65, 290],
    [45, 64, 300],
    [45, 71, 310],
    [45, 82, 320],
    [45, 86, 330],
    [45, 87, 340],
    [45, 82, 350],
    [50, 77, 0],
    [50, 73, 10],
    [50, 76, 20],
    [50, 83, 30],
    [50, 93, 40],
    [50, 100, 50],
    [50, 82, 60],
    [50, 76, 70],
    [50, 64, 80],
    [50, 60, 90],
    [50, 58, 100],
    [50, 66, 110],
    [50, 64, 120],
    [50, 70, 130],
    [50, 76, 140],
    [50, 81, 150],
    [50, 82, 160],
    [50, 75, 170],
    [50, 71, 180],
    [50, 62, 190],
    [50, 46, 200],
    [50, 51, 210],
    [50, 48, 220],
    [50, 51, 230],
    [50, 50, 240],
    [50, 55, 250],
    [50, 56, 260],
    [50, 57, 270],
    [50, 57, 280],
    [50, 58, 290],
    [50, 57, 300],
    [50, 62, 310],
    [50, 74, 320],
    [50, 80, 330],
    [50, 83, 340],
    [50, 84, 350],
    [55, 72, 0],
    [55, 71, 10],
    [55, 74, 20],
    [55, 80, 30],
    [55, 88, 40],
    [55, 102, 50],
    [55, 93, 60],
    [55, 85, 70],
    [55, 72, 80],
    [55, 68, 90],
    [55, 65, 100],
    [55, 74, 110],
    [55, 71, 120],
    [55, 77, 130],
    [55, 82, 140],
    [55, 84, 150],
    [55, 85, 160],
    [55, 76, 170],
    [55, 72, 180],
    [55, 62, 190],
    [55, 45, 200],
    [55, 54, 210],
    [55, 51, 220],
    [55, 52, 230],
    [55, 50, 240],
    [55, 52, 250],
    [55, 51, 260],
    [55, 50, 270],
    [55, 53, 280],
    [55, 50, 290],
    [55, 50, 300],
    [55, 55, 310],
    [55, 66, 320],
    [55, 72, 330],
    [55, 78, 340],
    [55, 79, 350],
    [60, 65, 0],
    [60, 65, 10],
    [60, 68, 20],
    [60, 75, 30],
    [60, 82, 40],
    [60, 99, 50],
    [60, 103, 60],
    [60, 94, 70],
    [60, 82, 80],
    [60, 75, 90],
    [60, 72, 100],
    [60, 82, 110],
    [60, 78, 120],
    [60, 82, 130],
    [60, 87, 140],
    [60, 84, 150],
    [60, 83, 160],
    [60, 75, 170],
    [60, 69, 180],
    [60, 60, 190],
    [60, 43, 200],
    [60, 50, 210],
    [60, 49, 220],
    [60, 50, 230],
    [60, 47, 240],
    [60, 48, 250],
    [60, 46, 260],
    [60, 45, 270],
    [60, 46, 280],
    [60, 43, 290],
    [60, 42, 300],
    [60, 47, 310],
    [60, 57, 320],
    [60, 63, 330],
    [60, 71, 340],
    [60, 73, 350],
    [65, 57, 0],
    [65, 57, 10],
    [65, 61, 20],
    [65, 67, 30],
    [65, 72, 40],
    [65, 88, 50],
    [65, 106, 60],
    [65, 102, 70],
    [65, 94, 80],
    [65, 83, 90],
    [65, 80, 100],
    [65, 87, 110],
    [65, 84, 120],
    [65, 85, 130],
    [65, 89, 140],
    [65, 83, 150],
    [65, 78, 160],
    [65, 71, 170],
    [65, 64, 180],
    [65, 55, 190],
    [65, 39, 200],
    [65, 46, 210],
    [65, 45, 220],
    [65, 45, 230],
    [65, 42, 240],
    [65, 43, 250],
    [65, 40, 260],
    [65, 39, 270],
    [65, 40, 280],
    [65, 36, 290],
    [65, 35, 300],
    [65, 41, 310],
    [65, 48, 320],
    [65, 54, 330],
    [65, 62, 340],
    [65, 63, 350],
    [70, 50, 0],
    [70, 48, 10],
    [70, 51, 20],
    [70, 56, 30],
    [70, 60, 40],
    [70, 75, 50],
    [70, 98, 60],
    [70, 108, 70],
    [70, 105, 80],
    [70, 90, 90],
    [70, 86, 100],
    [70, 92, 110],
    [70, 90, 120],
    [70, 88, 130],
    [70, 90, 140],
    [70, 80, 150],
    [70, 69, 160],
    [70, 65, 170],
    [70, 60, 180],
    [70, 49, 190],
    [70, 35, 200],
    [70, 40, 210],
    [70, 38, 220],
    [70, 39, 230],
    [70, 36, 240],
    [70, 36, 250],
    [70, 33, 260],
    [70, 33, 270],
    [70, 34, 280],
    [70, 29, 290],
    [70, 30, 300],
    [70, 34, 310],
    [70, 40, 320],
    [70, 45, 330],
    [70, 51, 340],
    [70, 53, 350],
    [75, 40, 0],
    [75, 39, 10],
    [75, 40, 20],
    [75, 45, 30],
    [75, 47, 40],
    [75, 59, 50],
    [75, 85, 60],
    [75, 103, 70],
    [75, 115, 80],
    [75, 98, 90],
    [75, 94, 100],
    [75, 95, 110],
    [75, 94, 120],
    [75, 89, 130],
    [75, 83, 140],
    [75, 72, 150],
    [75, 59, 160],
    [75, 57, 170],
    [75, 51, 180],
    [75, 41, 190],
    [75, 30, 200],
    [75, 32, 210],
    [75, 32, 220],
    [75, 32, 230],
    [75, 29, 240],
    [75, 29, 250],
    [75, 27, 260],
    [75, 26, 270],
    [75, 25, 280],
    [75, 24, 290],
    [75, 24, 300],
    [75, 27, 310],
    [75, 31, 320],
    [75, 36, 330],
    [75, 40, 340],
    [75, 40, 350],
    [80, 30, 0],
    [80, 30, 10],
    [80, 30, 20],
    [80, 33, 30],
    [80, 35, 40],
    [80, 45, 50],
    [80, 66, 60],
    [80, 82, 70],
    [80, 115, 80],
    [80, 106, 90],
    [80, 100, 100],
    [80, 100, 110],
    [80, 95, 120],
    [80, 84, 130],
    [80, 71, 140],
    [80, 58, 150],
    [80, 49, 160],
    [80, 45, 170],
    [80, 41, 180],
    [80, 32, 190],
    [80, 22, 200],
    [80, 24, 210],
    [80, 23, 220],
    [80, 24, 230],
    [80, 21, 240],
    [80, 21, 250],
    [80, 20, 260],
    [80, 20, 270],
    [80, 18, 280],
    [80, 18, 290],
    [80, 17, 300],
    [80, 20, 310],
    [80, 24, 320],
    [80, 27, 330],
    [80, 28, 340],
    [80, 30, 350],
    [85, 19, 0],
    [85, 18, 10],
    [85, 19, 20],
    [85, 21, 30],
    [85, 22, 40],
    [85, 30, 50],
    [85, 45, 60],
    [85, 58, 70],
    [85, 83, 80],
    [85, 111, 90],
    [85, 106, 100],
    [85, 96, 110],
    [85, 83, 120],
    [85, 64, 130],
    [85, 54, 140],
    [85, 44, 150],
    [85, 34, 160],
    [85, 30, 170],
    [85, 29, 180],
    [85, 23, 190],
    [85, 14, 200],
    [85, 14, 210],
    [85, 15, 220],
    [85, 15, 230],
    [85, 12, 240],
    [85, 13, 250],
    [85, 13, 260],
    [85, 13, 270],
    [85, 11, 280],
    [85, 12, 290],
    [85, 12, 300],
    [85, 14, 310],
    [85, 16, 320],
    [85, 18, 330],
    [85, 18, 340],
    [85, 17, 350],
    [90, 8, 0],
    [90, 7, 10],
    [90, 9, 20],
    [90, 10, 30],
    [90, 10, 40],
    [90, 15, 50],
    [90, 23, 60],
    [90, 34, 70],
    [90, 48, 80],
    [90, 90, 90],
    [90, 108, 100],
    [90, 84, 110],
    [90, 50, 120],
    [90, 35, 130],
    [90, 30, 140],
    [90, 20, 150],
    [90, 15, 160],
    [90, 15, 170],
    [90, 16, 180],
    [90, 13, 190],
    [90, 7, 200],
    [90, 4, 210],
    [90, 6, 220],
    [90, 7, 230],
    [90, 4, 240],
    [90, 4, 250],
    [90, 6, 260],
    [90, 6, 270],
    [90, 4, 280],
    [90, 5, 290],
    [90, 5, 300],
    [90, 6, 310],
    [90, 8, 320],
    [90, 9, 330],
    [90, 4, 340],
    [90, 6, 350]])
"""
*Pointer's Gamut* data as a tuple of *CIE LCHab* colourspace matrices.

POINTER_GAMUT_DATA : ndarray
"""

POINTER_GAMUT_BOUNDARIES = np.array([
    [0.659, 0.316],
    [0.634, 0.351],
    [0.594, 0.391],
    [0.557, 0.427],
    [0.523, 0.462],
    [0.482, 0.491],
    [0.444, 0.515],
    [0.409, 0.546],
    [0.371, 0.558],
    [0.332, 0.573],
    [0.288, 0.584],
    [0.242, 0.576],
    [0.202, 0.530],
    [0.177, 0.454],
    [0.151, 0.389],
    [0.151, 0.330],
    [0.162, 0.295],
    [0.157, 0.266],
    [0.159, 0.245],
    [0.142, 0.214],
    [0.141, 0.195],
    [0.129, 0.168],
    [0.138, 0.141],
    [0.145, 0.129],
    [0.145, 0.106],
    [0.161, 0.094],
    [0.188, 0.084],
    [0.252, 0.104],
    [0.324, 0.127],
    [0.393, 0.165],
    [0.451, 0.199],
    [0.508, 0.226]])
"""
*Pointer's Gamut* *xy* chromaticity coordinates boundaries.

POINTER_GAMUT_BOUNDARIES : ndarray
"""
