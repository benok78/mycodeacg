#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd

def pygraph(booktoread):
    mdf = pd.read_excel(booktoread, sheet_name='Sheet1')
    menMeans = mdf['mins']
    menMeans = tuple(menMeans.values) ## this produces a tuple from the mins column

    quarters = mdf['quarter']
    quarters = tuple(quarters.values)

    N = 4
    #menMeans = (20, 35, 30, 35)
    #womenMeans = (25, 32, 34, 20)
    #menStd = (2, 3, 4, 1)
    #womenStd = (3, 5, 2, 3)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.30       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans, width)  ## blue bottom values
    #p2 = plt.bar(ind, womenMeans, width,
    #             bottom=menMeans, yerr=womenStd) ## orange top vslues

    plt.ylabel('Outage Minutes')
    plt.title('Outage Minutes per Quarter')
    plt.xticks(ind, quarters) ##x axis data
    plt.yticks(np.arange(0, 201, 15))
    plt.legend((p1[0],), ('Minutes',))

    #plt.show()
    now = datetime.datetime.now()
    filesaved = now.strftime("%Y-%m-%d-outage.png")
    plt.savefig(filesaved)
    return filesaved
