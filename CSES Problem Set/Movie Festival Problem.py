#!/usr/bin/env python
# coding: utf-8

# from https://cses.fi/problemset/task/1629/
# input is number of movies
# maximize movies one can watch given start and end times for each movie

import numpy as np

def input_handler():
    movies = [int(x) for x in input().split()] 
    times = np.reshape(movies[1:], (-1, 2))
    return times

def scheduler(schedule):
    can_watch = 0
    while schedule.size > 0:
        if schedule.shape[0] == 1: # number of movies in list
            can_watch += 1
            break
        else:
            x = np.amin(schedule[:,1]) # find movie that ends earliest
            can_watch += 1
            schedule = schedule[~np.any(schedule < x, axis=1), :] # remove x and its intersections from list
    return can_watch

if __name__ == '__main__':
    times = input_handler()
    print(scheduler(times))