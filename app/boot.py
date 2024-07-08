import time
from lib.toolkit import log

boot_delay = 2
log.info("Boot delay %d sec. Press Ctrl+C to stop" % boot_delay)
time.sleep(boot_delay)
