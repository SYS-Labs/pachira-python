from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name="pachira-python",
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
        "pachira.event",
        "pachira.abi"
    ],
    install_requires=['web3', 
                      'eth_abi', 
                      'eth_typing', 
                      'eth_utils', 
                      'hexbytes', 
                      'blockscout-python == 0.1.2'],
    include_package_data=True,
    zip_safe=False,
)
