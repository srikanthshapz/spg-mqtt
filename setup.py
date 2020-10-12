import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HBT_IP_Core", 
    version="1.0.5",
    author="srikanth_shapur",
    author_email="srikanth.shapursridharmurthy@honeywell.com",
    description="A HBT-IP Messaging Protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(exclude=["*platforms*","*controller*","*tests*"]),
    install_requires=[
          'protobuf',
	  'paho-mqtt',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
