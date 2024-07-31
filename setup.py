from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name="pachira-python",
    version="0.0.1",
    description="Python API for Pachira project",
    long_description=long_description,
    long_description_content_type="text/markdown",    
    url="https://github.com/SYS-Labs",
    author="icmoore",
    author_email="defipy.devs@gmail.com",
    license="MIT",
    package_dir = {"pachira": "python/prod"},
    packages=[
        "pachira",
        "pachira.explorer"
    ],
    install_requires=["requests"],
    include_package_data=True,
    zip_safe=False,
)
