import gc
import time

from lib.Kernel import Kernel


def timed_function(f, *args, **kwargs):
    import time
    myname = str(f).split(' ')[1]

    def new_func(*args, **kwargs):
        t = time.ticks_us()
        result = f(*args, **kwargs)
        delta = time.ticks_diff(t, time.ticks_us())
        log.debug('GC: {} Function {} Time = {:6.3f}ms'.format(str(gc.mem_free()), myname, delta / 1000))
        return result

    return new_func

def load_properties(filepath, sep='=', comment_char='#', section_char='['):
    """
    Read the file passed as parameter as a properties file.
    """
    props = {}
    # if check_file_exists(filepath):
    with open(filepath, "rt") as f:
        for line in f:
            l = line.strip()
            if l and not (l.startswith(comment_char) or l.startswith(section_char)):
                key_value = l.split(sep)
                key = key_value[0].strip()
                value = sep.join(key_value[1:]).strip().strip('"')
                props[key] = value

    return props


# Initialize
kernel = Kernel(load_properties("conf/os.properties"))
log = kernel.logger
