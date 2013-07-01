#!/usr/bin/env python
from icecube.examples import histos.WeightedHistogram
import random

wh = histos.WeightedHistogram.WeightedHistogram(0, 18, 5)

for x in range(19):
    wh.fill(x, (x+1)*random.random())
    wh.fill(x, (x+1)*random.random())
    wh.fill(x, (x+1)*random.random())
    wh.fill(x, (x+1)*random.random())
    wh.fill(x, (x+1)*random.random())

wh.plot(linewidth=15, color='green')
