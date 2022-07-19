import setuptools

setuptools.setup(
    name="SunwaySMS",
    version="0.1.0",
    author=" Sunway ICT Center",
    author_email="shadafrough@gmail.com",
    description="Sunway sms webservice for python.",
    long_description_content_type="text/markdown",
    url="https://github.com/sunwaysms/SunWay-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["zeep"],
)