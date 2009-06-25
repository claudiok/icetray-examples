#!/usr/bin/env python

def main():
    """
    Make a dom occupancy plot from some 2007 experimental data
    """

    import sys
    try:
        import numpy, pylab
    except ImportError:
        sys.exit(0)
    
    from icecube import icetray, dataclasses, dataio, util


    hitseries_key = 'InIceRawData'

    data = numpy.zeros((81,61), float)
    nevent = 0
    for frame in util.all_physics([util.icdata_2007], verbose=True, update_frequency=5):
        nevent += 1
        hits = frame.Get(hitseries_key)
        for entry in hits:
            data[entry.key().GetString(), entry.key().GetOM()] += 1
            
    pylab.pcolor(numpy.transpose(data))
    pylab.axis('tight')
    ax = pylab.gca()
    ax.set_ylim(1,60)
    ax.set_xlim(1,80)
    ax.invert_yaxis()
    pylab.xlabel('string')
    pylab.ylabel('OM')
    pylab.title("DOM Occupancy,  %d events" % nevent)
    pylab.colorbar()
    pylab.savefig('dom_occupancy.png')
    print 'saved plot to "dom_occupancy.png"'

if __name__ == '__main__':
    main()

