from setuptools import setup
from stock_chart_tools import __version__

# requirements
with open("requirements.txt") as requirements:
    req = [i.strip() for i in requirements]

setup(
    name='stock_chart_tools',
    version=__version__,
    description='Tools for creating data series that can be chartes',
    url='https://github.com/philfoster/stock_chart_tools',
    author='Philip Foster',
    author_email='phil@the-fosters.net',
    license='GPL v3',
    packages=['stock_chart_tools'],
    package_dir={"stock_chart_tools": "stock_chart_tools"},
    install_requires=req,
    platforms=["any"],
    keywords=["technical-analysis", "macd", "ema", "sma", "stocks"],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'
    ]
)

