from setuptools import setup, find_packages

setup(
    name="async-edge-sensors",
    version="0.1.4",
    packages=find_packages(),
    install_requires=["smbus2", "asyncio"],
    author="EdgeTinkerer",
    description="Asynchronous I2C/SPI wrapper for edge devices.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
