import setuptools

setuptools.setup(
    name="Wine vendor api service",
    version="0.1.0",

    author="Louis Taylor",
    author_email="louis@kragniz.eu",

    py_modules=['supplier'],
    entry_points={'console_scripts':
        ['supplier-api = supplier:main',]
    ,},

    install_requires=[
        'PyYAML >= 3.11',
        'flask'
    ],

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
