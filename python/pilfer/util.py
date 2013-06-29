import icecube.dataio, sys

def all_physics(files, verbose=False, update_frequency=100):
    """
    Return all physics frames in the list 'files', via generator (doesn't actually
    cache them all in memory).

    Usage::

      for phys_frame in all_physics(glob.glob('/path/to/*.i3.gz')):
          print str(phys_frame)

    """
    nframes = 0 
    for f in files:
        i3f = icecube.dataio.I3File(f)
        if verbose:
            print("%s..." % f)
        #i3f.open_file(f)
        phys = i3f.pop_physics()
        while i3f.more():
            nframes += 1
            if verbose and nframes % update_frequency == 0:
                print('%15d\r' % nframes)
                sys.stdout.flush()
            yield phys
            phys = i3f.pop_physics()


