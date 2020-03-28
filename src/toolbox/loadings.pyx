
'''_____Standard imports_____'''
import numpy as np
import pickle


def load_data(dir, type=float):

    data = []

    data = np.load(dir)

    return data


def load_Bscan_spectra(file_dir, dimension=(1,1024,3147)):

    data = np.load(file_dir)
    data = np.reshape(data, dimension)

    return data


def load_calibration(dir=None):

    calibration = pickle.load( open( dir, "rb" ) )

    return calibration