##How to use
Install the lib via pip
```
pip install git+https://github.com/avillanova/recording-browser-behave.git
```


Create a object passing the webdriver and start it, example:
```
Video(context.driver).start()
```

##Options
```
video-name = 'bla.mp4' #Default is 'evidence.mp4'
four_cc = 'mp4v' #CODEC to be called by cv2.VideoWriter_fourcc(*four_cc)
fps = 30 #Default is 9
```


##Example
```
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=path)
driver.set_window_size(1366, 768)
Video(driver).start()
```
