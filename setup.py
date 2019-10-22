from setuptools import setup

setup(
    name='mockstore',
    version='0.0.2',
    description='mock complete of google cloud firestore version: 1.0.0',
    author='Spina Nico',
    author_email='spinanico93@gmail.com',
    url='https://github.com/SpinaNico/python-mockstore',
    packages=["mockstore", "mockstore.mock", "mockstore.mock.firestore_impl"],
    install_requires=[]
)