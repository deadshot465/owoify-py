import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='owoify-py',
    version='1.1.2',
    author='Chehui Chou',
    author_email='tetsuki.syu1315@gmail.com',
    description='Turning your worst nightmare into a Python package.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/deadshot465/owoify-py',
    packages=setuptools.find_packages(),
    classfiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
)
