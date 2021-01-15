#!/usr/bin/env python
# coding: utf-8

# ## Movie Festival Problem (from CSES)
# from https://cses.fi/problemset/task/1629/

def scheduler(times):
    can_watch = 0
    while times.size > 0:
        if times.shape[0] == 1:
            can_watch += 1
            break
        else:
            x = np.amin(times[:,1]) # threshold has earliest end time
            can_watch += 1
            times = times[~np.any(times < x, axis=1), :]
    return can_watch


if __name__ == "__main__":
    import numpy as np
    movies = [int(x) for x in input().split()]
    times = np.reshape(movies[1:], (-1, 2))
    scheduler(times)
