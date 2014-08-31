"""
  top-level tests for Allan deviation tools
  https://github.com/aewallin/allantools

  this files runs all the tests defined in the /tests/ subdirectories
  
  More datasets along with known deviations (or calculated with 
  known-good programs) are welcome.
  
  results from allantools seem correct, they agree to within 4 to 6 digits 
  of precision with other ADEV tools.
"""

import time
import sys

from nbs14 import nbs14_test
from phasedat import phase_dat_test
from pink_frequency import pink
from Cs5071A import Cs5071A_test_decade
import test_ns

if __name__ == "__main__":
    start = time.clock()

    nbs14_test.run()          # NBS14 test data with published deviations
    phase_dat_test.run()      # phase.dat from Stable32
    pink.run()                # synthetic pink frequency noise
    Cs5071A_test_decade.run() # HP 5071A Cs-clock measured against H-maser
    test_ns.run()             # sanity-checks for tau values

    end = time.clock()
    print "-------------------------"
    print "All tests done in %2.3f s" % (end-start) 
    # 2014-08-31 running time without MTIE on laptop with i7-3537U CPU @ 2.00GHz
    # All tests done in 19.841 s
    print "if we came this far without assertions or errors all is OK!"
