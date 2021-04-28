# coding=utf-8

import cv2
import threading
import textwrap
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pkg_resources

path = 'Roboto-Black.ttf'  # always use slash
filepath = pkg_resources.resource_filename(__name__, path)

class Video(threading.Thread):
    def __init__(self, driver, video_name='evidence.mp4', four_cc='mp4v', fps=3, context=None,
                 color_hex='#000000', font=filepath,
                 alpha=50, show_url=False, show_step=False):
        print(font)
        print(data)
        self.driver = driver
        self.video_name = video_name
        self.four_cc = four_cc
        self.context = context
        self.height = self.width = 0
        self.font = ImageFont.truetype(font, 32)
        self.color_hex = color_hex
        self.show_url = show_url
        self.show_step = show_step
        self.alpha = alpha
        self.fps = fps

        super(Video, self).__init__()

    def run(self):
        self.height, self.width, layers = self._get_matrix().shape
        video = cv2.VideoWriter(self.video_name, cv2.VideoWriter_fourcc(*self.four_cc), self.fps, (self.width, self.height))
        while True:
            try:
                video.write(self._get_matrix())
            except Exception:
                return False
        cv2.destroyAllWindows()
        video.release()

    def _get_matrix(self):
        byte_stream = self.driver.get_screenshot_as_png()
        data_array = np.frombuffer(byte_stream, dtype=np.uint8)
        matrix = cv2.imdecode(data_array, 1)
        if self.show_url:
            matrix = self._mark_url(matrix)
        if self.show_step and hasattr(self.context, 'step'):
            matrix = self._mark_step(matrix)
        return matrix

    def _mark_step(self, matrix):
        text = f'{self.context.step.keyword} {self.context.step.name}'
        img_pil = Image.fromarray(matrix)
        draw = ImageDraw.Draw(img_pil)

        margin, offset = 40, 20
        for line in textwrap.wrap(text):
            c_text, text_h = self._draw(draw, line)
            img_pil.paste(c_text, (margin, offset), c_text)
            offset = offset + text_h + 4
        return np.array(img_pil)

    def _mark_url(self, matrix):
        text = self.driver.current_url
        text = textwrap.wrap(text)
        img_pil = Image.fromarray(matrix)
        draw = ImageDraw.Draw(img_pil)
        c_text, text_h = self._draw(draw, text[0])
        margin = 40
        img_pil.paste(c_text, (margin, self.height - text_h - 10), c_text)
        return np.array(img_pil)

    def _draw(self, draw, text):
        text_w, text_h = draw.textsize(text, self.font)
        c_text = Image.new('RGB', (text_w + 3, text_h + 3), color=self.color_hex)
        drawing = ImageDraw.Draw(c_text)
        drawing.text((1, 0), text, font=self.font, fill=(255, 255, 255, 255))
        c_text.putalpha(self.alpha)
        return c_text, text_h
