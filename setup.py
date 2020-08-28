from setuptools import setup, find_packages


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: Log Analysis',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: System :: Logging',
    'Topic :: Utilities'
]

setup(
    name='pyjsonlines',
    version='1.0.0',
    description='Library to convert Json to Jsonl and Jsonl to Json.',
    long_description=open('README.md').read(),
    url='https://github.com/thisischandanmishra/pyjsonlines',
    author='Chandan Kumar',
    author_email='devchandankumar2@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='jsonl2json jsonlines json2jsonl pyjsonlines',
    packages=find_packages(),
    install_requires=['six']
)
