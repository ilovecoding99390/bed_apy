from setuptools import setup, find_packages

setup(
    name="bed_apy",
    version="1.0.0",
    author="Ezekiel Nogle",
    description="A Bedrock WebSocket system for Minecraft Python modding",
    packages=find_packages(),
    install_requires=[
        "websockets",
        "asyncio",
        "json",
        "uuid",
        "urllib",
        "base64"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPL-3.0)",
        "Operating System :: OS Independent",
    ]
)