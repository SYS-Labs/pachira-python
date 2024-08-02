from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name="pachira",
    version="0.0.1",
    description="Python library for Pachira on DeFi, data research and integration",
    long_description=long_description,
    long_description_content_type="text/markdown",    
    url="https://github.com/SYS-Labs",
    author="icmoore",
    author_email="icmoore@syscoin.org",
    license="MIT",
    package_dir = {"pachira": "python/prod"},
    packages=[
        "pachira",
        "pachira.explorer"
    ],
    install_requires=["requests, blockscout-python"],
    include_package_data=True,
    zip_safe=False,
)
