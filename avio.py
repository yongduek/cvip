import cv2 as cv
import numpy as np
import av
import av.datasets

vframes = [] # video frames in numpy
aframes = [] # audio frames (2x1024) in numpy
aframesorg = [] # as is returned

container = av.open('./black-gms-20.mp4')
#container.streams.video[0].thread_type = 'AUTO'

count = 0
for frame in container.decode(video=0, audio=0):
    if type(frame) == av.video.frame.VideoFrame:
        arr = np.asarray(frame.to_image())
#        cv.imshow ('win', arr)
#        cv.waitKey(5)
        vframes.append(arr)
#         print (frame.to_image().size)
#         print ('-=-----------------')
    elif type(frame) == av.audio.frame.AudioFrame:
        count += 1
        aframes.append(frame.to_ndarray())
        aframesorg.append(frame)
#         print (frame.rate, frame.sample_rate, frame.time, frame.to_nd_array().shape)
    else:
        print ('No AV? ', frame)
#     print (count)
#
cv.destroyAllWindows()

print ('pixel data type: ', vframes[0].dtype)

fps = container.streams.video[0].rate


ofilename = 'output-aorg.mp4'
ocont = av.open(ofilename, mode='w')
astream = ocont.add_stream('mp3', rate=container.streams.audio[0].rate)
vstr = ocont.add_stream('h264', rate=fps)

print ('video outstream')
for v in vframes:
    vf = v.copy() # v is read only
    
    vf[100:vf.shape[0]-100, 20:vf.shape[1]-20, 0] = 128

    ovf = av.VideoFrame.from_ndarray (vf)
    for packet in vstr.encode(ovf):
        ocont.mux(packet)
# flush
for packet in vstr.encode():
    ocont.mux(packet)
#

print ('audio outstream')
for of in aframesorg:
    arr = of.to_ndarray()
    
    filtered = arr.copy()

    of2 = av.audio.frame.AudioFrame.from_ndarray(filtered, format='fltp')
    of2.rate = of.rate
    of2.time_base = of.time_base

    for packet in astream.encode(of2):
        ocont.mux(packet)
#flush
for packet in astream.encode():
    ocont.mux(packet)
#

ocont.close()

print ('done: ', ofilename)