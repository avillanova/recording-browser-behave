
recording-browser-behave
===================
This library can be used to recorder video from webdriver when you are running an test with behave and without take screenshots.


- How to install
- How to use it
- Options
- Examples
- Important

How to install
--------------
Install the lib via pip:
```shell
pip install git+https://github.com/avillanova/recording-browser-behave.git
```

How to use it:
--------------
Create an instance of the video passing the webdriver that you want to record and call start function to run it in a new Thread.
```python
from video_recorder.record_video import Video
Video(context.driver).start()
```

Options:
--------
You are able to change some configurations:

  |  Parameter    | Default value     |                                  Description                         |
  |---------------|-------------------|----------------------------------------------------------------------|
  |``video-name`` |  evidence.mp4     |    Path and name of your evidence                                    |
  |``four_cc``    |  mp4v             |    Codec to generate the video file                                  |
  |``fps``        |  3                |    Frames per second, you can control the video speed                |
  |``context``    |  None             |    Scenario context to get step infos.                               |
  |``color_hex``  |  #000000          |    Highlighted text color                                            |
  |``font``       |  .Roboto-Black.ttf|    Font to write text                                                |
  |``alpha``      |  50               |    Transparency value, if you need bold you can plus this value      |
  |``show_url``   |  False            |    Put the URL in video or not                                       |
  |``show_step``  |  False            |    Put the Step Name in video or not                                 |
  |``font_size``  |  32               |    Size of the font text                                             |

Examples
--------
```python
def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    context.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=path)
    context.driver.set_window_size(1366, 768)
    Video(context.driver,
        video_name=f'resources/{scenario.name}/evidence.avi',
        four_cc='XVID',
        fps=9,
        context=context,
        color_hex='#f90cf5',
        font='resources/font/chrisMaster.ttf',
        alpha=200,
        show_url=True,
        show_step=True,
        font_size=36
    ).start()

def before_step(context, step):
    context.step = step
```
Important:
----------
- ``show_step=True`` just will work if context is defined in ``Video(driver, context=context)`` and *context* has step attribute, so you need to add it in context using:
```python
def before_step(context, step):
    context.step = step
```
- ``four_cc`` should match with the ``video_name``, so if you are using AVI, for example:
```python
Video(context.driver, video_name=f'resources/{scenario.name}/evidence.avi', four_cc='XVID')
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
