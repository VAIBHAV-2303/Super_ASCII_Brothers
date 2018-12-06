import setuptools

with open('README.md') as f:
	long_description = f.read()

setuptools.setup(
    name="mario",
    version="1.0",
    author="Vaibhav Garg",
    author_email="vaibhav.garg@students.iiit.ac.in",
    description="Replica of classic mario game",
    url="https://github.com/VAIBHAV-2303/Super_ASCII_Brothers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)