allantools
==========

A small GPL v3+ Python library for calculating Allan deviation and related statistics.

Developed here https://github.com/aewallin/allantools, but also available on PyPi at https://pypi.python.org/pypi/AllanTools

Input data should be evenly spaced observations of either fractional frequency,
or phase in seconds. Deviations are calculated for given tau values in seconds.

Installation

> sudo python setup.py install

Usage:
```python
import allantools # https://github.com/aewallin/allantools/
rate = 1/float(data_interval) # data rate in Hz
taus = [1,2,4,8,16] # tau-values in seconds
# fractional frequency data
(taus_used, adev, adeverror, adev_n) = allantools.adev(fract_freqdata, rate, taus)
# phase data
(taus_used, adev, adeverror, adev_n) = allantools.adev_phase(phasedata, rate, taus)

# notes:
#  - taus_used may differ from taus, if taus has a non-integer multiples of data_interval
#  - adeverror assumes 1/sqrt(adev_n) errors
```

These statistics are currently included:
* ADEV    Allan deviation
* OADEV   overlapping Allan deviation,
* MDEV    modified Allan deviation,
* TDEV    Time deviation
* HDEV    Hadamard deviation
* OHDEV   overlapping Hadamard deviation
* TOTDEV  Total deviation
* MTIE    Maximum time interval error
* TIERMS  Time interval error RMS

To do:
* Modified Total variance
* Time Total (modified total variance scaled by (t^2/3) )
* Hadamard Total

see /tests for tests that compare allantools output to other (e.g. Stable32) programs.

No profiling or optimization attempt was made. Patches that give speedups are welcome.
Make sure your patch does not break any of the tests, and does not significantly reduce the readability of the code.
