#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import locale
import platform

matplotlib.use("pgf")

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_NUMERIC, 'Polish')
else:
    locale.setlocale(locale.LC_NUMERIC, ('pl_PL', 'UTF-8'))
