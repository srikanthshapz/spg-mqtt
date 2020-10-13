import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HBT_IP_Platform", 
    version="1.0.1",
    author="srikanth_shapur",
    author_email="srikanth.shapursridharmurthy@honeywell.com",
    description="A HBT-IP Messaging Protocol",
    packages=setuptools.find_packages(),
    dependency_links=['https://github.com/srikanthshapz/spg-mqtt/tree/master/#egg=HBT_IP_Core-1.0.5'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
