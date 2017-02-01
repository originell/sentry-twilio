from __future__ import absolute_import

try:
    pkg_resources.get_distribution('sentry-twilio')
except pkg_resources.DistributionNotFound:
    return
else:
    raise RuntimeError("Found %r. This has been superseded by 'sentry-plugins', so please uninstall." % name)
