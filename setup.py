from setuptools import setup

setup(
    name='enviro_mqtt',
    version='0.1',
    packages=['enviro_mqtt'],
    url='',
    license='MIT',
    author='dh_vie',
    author_email='dhvie85@gmail.com',
    description='',
    install_requires=[
        "ST7735",
        "ltr559",
        "pimoroni-bme280",
        "pms5003",
        "PIL",
        "paho-mqtt",
        "sounddevice"
    ]
)
