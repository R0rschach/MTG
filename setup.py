from setuptools import setup, find_packages

config = {
        'description' : 'MTG Data Analysis',
        'author' : 'Lei Du',
        'author_email' : 'dulei66@gmail.com',
        'version' : '0.1',
        'install_requires' : ['nose'],
        'packages' : find_packages(),
        'scripts': []
}

setup(**config)
