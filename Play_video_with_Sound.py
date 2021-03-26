# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 12:25:06 2020

@author: us51114
"""
import time
import cv2
import numpy as np
import sounddevice as sd
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer
video_path="D:\\kalathi\\My_collection\\Python\\video_editor\\SampleVideo_1280x720_2mb.mp4"
def PlayVideo(video_path):
    cap=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    fs=player.frame_rate
    print("Audio fs:",fs)
    fps = cap.get(cv2.CAP_PROP_FPS)
    exc_tps=1/fps;i=1
    if cap.isOpened():
        # sd.play(sample_re, fs)
        start_t=time.perf_counter()
        while(1):
            ret, frame = cap.read()
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            act_elps_t=exc_tps*i
            if ret:
                cv2.imshow('frame',frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            # end_t=time.perf_counter()
            # print("start time:",start_t,"end time:",end_t)
            # sleep_t=1/fps-(end_t-start_t)
            i=i+1
            sleep_t=act_elps_t-(time.perf_counter()-start_t)
            # print(sleep_t)
            if sleep_t>0:
                # new_wait=exc_tps+start_t
                # end_t=time.perf_counter()
                # print("start time:",start_t,"end time:",end_t,"New wait time:",new_wait,"diff:",new_wait-end_t)
                # time.sleep(new_wait-end_t)
                time.sleep(act_elps_t-(time.perf_counter()-start_t))
            # start_t=end_t
            # print(end_t-start_t)
        cap.release()
        cv2.destroyAllWindows()
        sd.stop()
    
    # print(type(player))
    # while True:
    #     audio_frame, val = player.get_frame()
    #     print(audio_frame,val)
    #     if cv2.waitKey(28) & 0xFF == ord("q"):
    #         break
    #     if val == 'eof' or audio_frame is None:
    #         break
    # # print(player)
    # # sd.play(player, 44100.0)
    # while True:
    #     grabbed, frame=video.read()
    #     audio_frame, val = player.get_frame()
    #     if not grabbed:
    #         print("End of video")
    #         break
    #     if cv2.waitKey(28) & 0xFF == ord("q"):
    #         break
    #     cv2.imshow("image", frame)
    #     if val != 'eof' and audio_frame is not None:
    #         #audio
    #         img, t = audio_frame
    # video.release()
    # cv2.destroyAllWindows()
PlayVideo(video_path)
# player = MediaPlayer(video_path)
# for x in range(6):
#     time.sleep(2)