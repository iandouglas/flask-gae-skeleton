from __future__ import print_function

import sys
import os
import unittest

sdk_base_path = os.environ.get('GOOGLE_APP_ENGINE_SDK')

if not sdk_base_path:
    print("Testing requires the Google App Engine SDK.  Please set GOOGLE_APP_ENGINE_SDK with the path to the SDK.")
    sys.exit(1)

possible_paths = [
    sdk_base_path,
    os.path.join(sdk_base_path, 'platform', 'google_appengine')
]

for sdk_path in possible_paths:
    if os.path.exists(os.path.join(sdk_path, 'dev_appserver.py')):
        # All good, we've found the SDK
        sys.path.insert(0, sdk_path)
        break
else:
    print("Google App Engine SDK not found at {}, please update GOOGLE_APP_ENGINE_SDK".format(sdk_base_path))
    sys.exit(1)

# Run test suite
test_suite = unittest.TestLoader().discover('tests')
unittest.TextTestRunner(verbosity=1).run(test_suite)
