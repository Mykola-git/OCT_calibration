# Py-OCT-Calibration

This project aims to produce an easy to use tool to calibrate any SD or SS-OCT. By calibrate I mean substracting background - k-linearize spectra - evaluate and compensate dispersion. In order to compute the calibration the algorithm need multiple measurements:
* mirror1.txt         (OCT interferogram with mirror in one side of the zero delay as sample)
* dark_sample.txt     (OCT interferogram with ref arm blocked)
* mirror2.txt         (OCT interferogram with mirror in the other side of the zero delay as sample)
* dark_ref.txt        (OCT interferogram with sample arm blocked)
* dark_not.txt        (OCT interferogram with both arm blocked)

Those .txt file should be saved into a file in data/spectra/<dir-name> directory.

## Packages dependencies

In order to use the Py-OCT-Calibration Library, one must have installed the following packages:

```
    - Numpy
    - Scipy
    - json
    - matplotlib
    - sphynx (for developer only)
    - git (for developer only)

```

Using pip3 one can use the following commands:

```console
>>> pip3 install Numpy
>>> pip3 install Scipy
>>> pip3 install matplotlib
>>> pip3 install gitpython
>>> apt-get install python-sphinx (for Unix OS)
>>> sudo port install py27-sphinx (for Mac OS)
```

## Project architecture

The folder architecture is presented as :

```
    PyOCTCalibration/
            - data/                         (contain all data)
                - calibration/
                - img/
            - processing/                
                - calibration.py            (compute the k-linear., dispersion, spectrum shift, noise)
                - Aline.py                  (process one Aline)
                - Bscan.py                  (process one Bscan)
                - Cscan.py                  (process one Cscan)
            - toolbox/                      (contain tools to do all the processing)

            - Doc/                          (not yet added)

```


## Run example

### Calibration

In order to run a calibration example one can tape the following command on command prompt:

```console

>>> python3 processing/calibration.py --dispersion=1 --input-dir=./data/calibration/spectra/example/ --output-file=calib.json

```

Arguments for processing/calibration.py are:

* --dispersion : [1] for normal dispersion, [-1] for anormal
* --input-dir : directory of the input files for calibration
* --output-file : name of the output .json file containing all the calibration parameters which is saved in same directory as input-dir

Here an example of the output of the de-noising process.

<img src=".\doc\images\Figure_1.png"
     alt="spectrum de-noising"
     style="float: left; margin-right: 10px;" />


### Aline

In order to process one example of Aline, one can tape the following command on command prompt:

```console

>>> python3 processing/Aline.py --dispersion=1 --input-dir = ../ --calibration=calib.json

```

Arguments for processing/Aline.py are:

* --dispersion : [1] for normal dispersion, [-1] for anormal
* --input-file : directory of the input Aline file
* --calibration : directory for the output .json file containing all the calibration parameters
* --output-file : directory for the processed Aline file

### Bscan

In order to process one example of Bscan, one can tape the following command on command prompt:

```console

>>> python3 processing/Aline.py --dispersion=1 --input-dir = ../ --calibration=calib.json --output-file=...

```

Arguments for processing/Aline.py are:

* --dispersion : [1] for normal dispersion, [-1] for anormal
* --input-file : directory of the input Aline file
* --calibration : directory for the output .json file containing all the calibration parameters
* --output-file : directory for the processed Bscan file



### Cscan

In order to process one example of Aline, one can tape the following command on command prompt:

```console

>>> python3 processing/Aline.py --dispersion=1 --input-dir = ../ --calibration=calib.json --output-file=...

```

Arguments for processing/Aline.py are:

* --dispersion : [1] for normal dispersion, [-1] for anormal
* --input-file : directory of the input Aline file
* --calibration : directory for the output .json file containing all the calibration parameters
* --output-file : directory for the processed Cscan file


Here is an example of output give by:

```console

>>> python3 process_Bscan.py -f=cible_6 -d=-1

```
## For citing this project in scientific papers

<a href="https://zenodo.org/badge/latestdoi/188613450"><img src="https://zenodo.org/badge/188613450.svg" alt="DOI"></a>

## Pep8 coding convention

In order to keep a clean and consistent code, one can follow the convention as presented in the following link:

https://www.python.org/dev/peps/pep-0008/#documentation-strings