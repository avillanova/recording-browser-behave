from setuptools import find_packages, setup
setup(
    name='recording-browser-behave',
    version='0.1.8',
    description='To recording the browser in Thread',
    author='Alex Villanova',
    author_email='alexsrvillanova@gmail.com',
    url='https://github.com/avillanova/recording-browser-behave',
    license='MIT',
    install_requires=[
        'Pillow~=8.2.0',
        'numpy~=1.20.2',
        'opencv-python~=4.5.1.48',
    ],
    package_data={'': ['Roboto-Black.ttf']},
    include_package_data=True,
    packages=find_packages(include=['video_recorder'])
)