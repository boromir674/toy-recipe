from setuptools import setup, find_packages

from os import path

this_dir = path.dirname(path.realpath(__file__))


def readme():
    with open(path.join(this_dir, 'README.rst')) as f:
        return f.read()


setup_kwargs = dict(
    name='cpp_python_hybrid',
    version='0.5',
    description='Package that combines C++ and Python code',
    long_description=readme(),
    keywords='reference package',
    zip_safe=False,
    test_suite='tests',
    tests_require=['pytest'],
    # project_urls={
    #     "Source Code": "https://github.com/..,
    # },
    # install_requires=[
    #
    # ],
    # setup_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url='boromir674/first-conda-package-distribution.git',
    # download_url='point to tar.gz',  # help easy_install do its tricks
    author='Konstantinos Lampridis',
    author_email='boromir674@hotmail.com',
    license='GNU GPLv3',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},  # this is required by distutils
    include_package_data=True,
    # Include all data files in packages that distutils are aware of through the MANIFEST.in file
    # package_data={
    #     # If any package contains *.txt or *.rst files, include them:
    #     '': ['*.txt', '*.rst'],
    #     'package_name.file_name': ['data/*.txt', 'data/model.pickle'],
    # },
    entry_points={
        'console_scripts': [
            'add-two = addition_package.addition:main',
        ]
    },
    # extras_require={},
)

setup(**setup_kwargs)
