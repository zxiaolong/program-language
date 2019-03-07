import sys
if sys.version_info < (3, 4):
    raise RuntimeError('At least Python 3.4 is required')
else:
	print(sys.version_info)