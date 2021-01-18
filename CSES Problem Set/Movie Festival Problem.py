#!/usr/bin/env python
# coding: utf-8

# ## Movie Festival Problem (from CSES)

# In[14]:


# from https://cses.fi/problemset/task/1629/
# input n is number of movies
# maximize n given start and end times for each movie

import numpy as np

def main():
    movies = [int(x) for x in input().split()] 
    times = np.reshape(movies[1:], (-1, 2))
    scheduler(times)

def scheduler(times):
    can_watch = 0
    while times.size > 0:
        if times.shape[0] == 1: # number of movies in list
            can_watch += 1
            break
        else:
            x = np.amin(times[:,1]) # find movie that ends earliest
            can_watch += 1
            times = times[~np.any(times < x, axis=1), :] # remove it and its intersections from list
    return can_watch

if __name__ == '__main__':
    main()
    print(can_watch)

