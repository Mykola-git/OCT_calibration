# -

'''_____Standard imports_____'''
import numpy as np
import os
import tables
import sys


'''_____Add package_____'''
p = os.path.abspath('.')
if p not in sys.path:
    sys.path.append(p)

'''_____Arguments parsing/loading_____'''
from src.toolbox.parsing import Cscan_parse_arguments
arguments = Cscan_parse_arguments()
from src.toolbox._arguments import Arguments



'''_____Project imports_____'''

if Arguments.compiled:
    from src.toolbox.cython.loadings import load_calibration
    if Arguments.gpu:
        from src.toolbox.cython.main_processing_gpu import process_Bscan
    else:
        from src.toolbox.cython.main_processing_cpu import process_Bscan
else:
    from src.toolbox.loadings import load_calibration
    if Arguments.gpu:
        from src.toolbox.main_processing_gpu import process_Bscan
    else:
        from src.toolbox.main_processing_cpu import process_Bscan


calibration = load_calibration(dir = Arguments.calibration_file)

Bscan_list = os.listdir(Arguments.input_directory)

Bscan_list = [os.path.join(Arguments.input_directory, s) for s in Bscan_list]

f = tables.open_file(Arguments.output_file, mode='w')

atom = tables.Float64Atom()

array_c = f.create_earray(f.root, 'data', atom, (0, Arguments.dimension[1], Arguments.dimension[2]/2))

length = len(Bscan_list)

for n_i, Bscan_spectra in enumerate(Bscan_list):
    print(Bscan_spectra)

    sys.stdout.write('Bscan processing ... [{0}/{1}] \n'.format(n_i, length ) )

    temp = np.load(Bscan_spectra)

    array_c.append([process_Bscan(temp, calibration)])

sys.stdout.write(' saving into {0} file \n'.format(Arguments.output_file ) )

if not Arguments.silent:
    from src.toolbox.plottings import Bscan_plots
    from src.toolbox.filters import denoise_Bscan
    Bscan_plots( denoise_Bscan( f.root.data[-1,:,:] ) )


f.close()



#-
