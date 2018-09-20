from setuptools import setup

setup(
    name='WEATHER',
    version='0.1',
    py_modules=['weather'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        weather=weather:main
        ''',
)
