#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2017 aibot.me, Inc. All Rights Reserved
#
########################################################################
import urllib3
import json
import base64
import time
import os
import sys
import wave
import numpy as np
from datetime import datetime
from pyaudio import PyAudio, paInt16
import keyboard
import warnings
warnings.simplefilter("ignore", DeprecationWarning)

class GenAudio(object):
    def __init__(self):
        self.num_samples = 2000
        self.sampling_rate = 8000
        self.level = 1500
        self.count_num = 20
        self.save_length = 8

        self.voice_string = []

        self.time_count = 99999999999999999999
    #
    def save_wav(self, filename):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(self.sampling_rate)
        wf.writeframes(np.array(self.voice_string).tobytes())
        wf.close()

    def read_audio(self):

        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1, rate=self.sampling_rate, input=True,
                         frames_per_buffer=self.num_samples)

        save_count = 0
        save_buffer = []
        time_count = self.time_count

        # 퀴즈 문제 설정
        print("문제: 친구를 만났을 때 하는 말은?")



        print("녹음 시작 ...",end="\n\n")
        while True:
            time_count -= 1
            string_audio_data = stream.read(self.num_samples)
            audio_data = np.fromstring(string_audio_data, dtype=np.short)
            large_sample_count = np.sum(audio_data > self.level)

            if large_sample_count > self.count_num:
                save_count = self.save_length
            else:
                save_count -= 1
            if save_count < 0:
                save_count = 0

            if save_count > 0:
                save_buffer.append(string_audio_data)
            else:
                if len(save_buffer) > 0:
                    self.voice_string = save_buffer
                    save_buffer = []
                    return True
        return True


if __name__ == "__main__":
    r = GenAudio()
    r.read_audio()
    r.save_wav("./test.wav") #저장될 이름
    print("===== 종료되었습니다. =====",end="\n\n\n")

    openApiURL1 = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
    accessKey = "API key값 [발급받아야함]"
    audioFilePath = "[파일위치]"
    languageCode = "korean" #언어 선택 가능
    file = open(audioFilePath, "rb")
    audioContents = base64.b64encode(file.read()).decode("utf8")
    file.close()

    requestJson = {
        "access_key": accessKey,
        "argument": {
            "language_code": languageCode,
            "audio": audioContents
        }
    }
    http = urllib3.PoolManager()
    response1 = http.request(
        "POST",
        openApiURL1,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )
    print("===== 나의 텍스트 =====",end="\n")
    print(str(response1.data[43:len(response1.data)-3],"utf-8"))



    openApiURL = "http://aiopen.etri.re.kr:8000/ParaphraseQA"
    sentence1 = "오늘 날씨가 좋네요" # 퀴즈 정답 [비교할 문장]
    sentence2 = str(response1.data[43:len(response1.data) - 3], "utf-8")# 사용자 음성 -> 텍스트
    requestJson = {
        "access_key": accessKey,
        "argument": {
            "sentence1": sentence1,
            "sentence2": sentence2
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )
    print("===== 정답 텍스트 =====")
    print(sentence1)
    print("===== 유사도 비교 =====")
    print("정답 문장: "+sentence1)
    print("나의 문장: "+(str(response1.data[43:len(response1.data)-3],"utf-8")))
    print("===== 유사도 결과 =====")
    if 'paraphrase' == str(response.data[39:len(response.data) - 3], "utf-8"):
        print("매우 유사합니다 :)")
    elif 'not paraphrase' == str(response.data[39:len(response.data) - 3], "utf-8"):
        print("유사도가 낮습니다 :(")



