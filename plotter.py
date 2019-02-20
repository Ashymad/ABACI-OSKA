#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.io.wavfile as wv
import locale
import platform

matplotlib.use("pgf")

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_NUMERIC, 'Polish')
else:
    locale.setlocale(locale.LC_NUMERIC, ('pl_PL', 'UTF-8'))

fs, mp3_320 = wv.read("data/audio-320.wav")
fs, mp3_256 = wv.read("data/audio-256.wav")
fs, mp3_196 = wv.read("data/audio-196.wav")
fs, mp3_128 = wv.read("data/audio-128.wav")

plt.figure()
plt.specgram(mp3_320.transpose()[1], Fs=fs, NFFT=128, noverlap=64)
plt.savefig("plots/320.pgf")
plt.figure()
plt.specgram(mp3_256.transpose()[1], Fs=fs, NFFT=128, noverlap=64)
plt.savefig("plots/256.pgf")
plt.figure()
plt.specgram(mp3_196.transpose()[1], Fs=fs, NFFT=128, noverlap=64)
plt.savefig("plots/196.pgf")
plt.figure()
plt.specgram(mp3_128.transpose()[1], Fs=fs, NFFT=128, noverlap=64)
plt.savefig("plots/128.pgf")
