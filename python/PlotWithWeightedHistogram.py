#!/usr/bin/env python
from icecube.examples.histos import WeightedHistogram
import random

wh = WeightedHistogram.WeightedHistogram(0, 18, 5)

for x in range(19):
    wh.fill(x, (x+1)*random.random())
    wh.fill(x, (x+1)*random.random())
    wh.fill(x, (x+1)*random.random())
    wh.fill(x, (x+1)*random.random())
    wh.fill(x, (x+1)*random.random())

wh.plot(linewidth=15, color='green')
