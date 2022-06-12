from time import perf_counter
from array import array
from contextlib import contextmanager

@contextmanager
def timing(label: str):
  t0 = perf_counter()
  yield lambda: (label, t1 - t0)
  t1 = perf_counter()
with timing('Array tests') as total:
  with timing('Array creation innermul') as inner:
    x = array('d', [0] * 1000000)
  with timing('Array creation outermul') as outer:
    x = array('d', [0]) * 1000000

print('Total [%s]: %.6f s' % total())
print(' Timing [%s]: %.6f s' % inner())
print(' Timing [%s]: %.6f s' % outer())



# here we can test function performance time
