import setuptools

from pyOutlook import __version__

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setuptools.setup(
    name='pyOutlook',
    version=__version__,
    packages=['pyOutlook', 'pyOutlook.internal', 'pyOutlook.core'],
    url='https://pypi.python.org/pypi/pyOutlook',
    license='MIT',
    author='Jens Astrup',
    author_email='jensaiden@gmail.com',
    description='A Python module for connecting to the Outlook REST API, without the hassle of dealing with the '
                'JSON formatting for requests/responses and the REST endpoints and their varying requirements',
    long_description=long_description,
    install_requires=['requests'],
    tests_require=['coverage', 'nose'],
    keywords='outlook office365 microsoft email',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Communications :: Email :: Email Clients (MUA)',
        'Topic :: Office/Business',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Natural Language :: English'
    ]
)
