import cv2
import threading
import numpy as np


class Video(threading.Thread):
    def __init__(self, driver, video_name='evidence.mp4', four_cc='mp4v'):
        self.driver = driver
        self.video_name = video_name
        self.four_cc = four_cc
        super(Video, self).__init__()

    def run(self):
        height, width, layers = self.get_matrix().shape
        video = cv2.VideoWriter(self.video_name, cv2.VideoWriter_fourcc(*self.four_cc), 9, (width, height))
        while True:
            try:
                video.write(self.get_matrix())
            except Exception:
                return False
        cv2.destroyAllWindows()
        video.release()

    def get_matrix(self):
        byte_stream = self.driver.get_screenshot_as_png()
        data_array = np.frombuffer(byte_stream, dtype=np.uint8)
        matrix = cv2.imdecode(data_array, 1)
        return matrix
