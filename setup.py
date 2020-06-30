import setuptools

setuptools.setup(
    name='mac-app-env',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
