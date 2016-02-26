import setuptools
from packagename.version import Version

with open('requirements.txt') as f:
    requirements_txt = f.read().splitlines()

setuptools.setup(name='clc',
                 version=Version('1.0.0').number,
                 description='Python SDK for CenturyLinkCloud',
                 long_description=open('README.md').read().strip(),
                 author='ecosystem@ctl.io',
                 author_email='ecosystem@ctl.io',
                 url='http://github.com/CenturyLinkCloud/py-clc-sdk',
                 py_modules=['clc'],
                 install_requires=requirements_txt,
                 license='MIT License',
                 zip_safe=False,
                 keywords='clc sdk',
                 classifiers=['Packages'])
