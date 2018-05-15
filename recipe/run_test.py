import astropy._compiler
import astropy._erfa._core

from astropy.convolution.convolve import _convolveNd_boundary_none_c
from astropy.convolution.convolve import _convolveNd_padded_boundary_c

import astropy.cosmology.scalar_inv_efuncs
import astropy.io.ascii.cparser
import astropy.io.fits.compression
import astropy.io.votable.tablewriter
import astropy.modeling._projections
import astropy.stats.lombscargle.implementations.cython_impl
import astropy.table._column_mixins
import astropy.table._np_utils
import astropy.utils._compiler
import astropy.utils.xml._iterparser
import astropy.wcs._wcs

# We run a subset of the tests which are the most likely to have
# issues because they rely on C extensions and bundled libraries

from astropy import test
test(package='io.ascii')
test(package='time')
test(package='wcs')
test(package='convolution')
