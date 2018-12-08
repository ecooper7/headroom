## ecooper 12/7/2018

import scipy.io.wavfile

fname = 'f1a_0001.wav'  ## put your wave filename here
(sr, data) = scipy.io.wavfile.read(fname)

## speedup: remove every nth sample.
def speedup(d, n):
    newarr = []
    count = 0
    for item in d:
        if count % n != 0:
            #print count
            newarr.append(item)
        count += 1
    return np.array(newarr)

## slowdown: duplicate every nth sample.
def slowdown(d, n):
    newarr = []
    count = 0
    for item in d:
        newarr.append(item)
        if count % n == 0:
            newarr.append(item)
        count += 1
    return np.array(newarr)

## stutter effect
## inputs are data, start time in samples, duration in samples,
## and number of repetitions.
def stutter(d, stime, dur, reps):
    newarr = []
    repeat = []
    count = 0
    for item in d:
        count += 1
        if count >= stime and count <= stime + dur:
            repeat.append(item)
        elif count == stime + dur + 1:
            for i in range(0, reps):
                newarr += repeat
            newarr.append(item)
        else:
            newarr.append(item)
    return np.array(newarr)

# examples
#outdata = speedup(data, 3)
#outdata = slowdown(data, 2)
outdata = stutter(data, 50000, 5000, 5) 
scipy.io.wavfile.write('out.wav', sr, outdata)

## TODO
## - start times and durations for every effect
## - filter-based effects
## - input and output filenames from command line + randomized effects so you don't have to do it by hand
