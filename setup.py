from setuptools import setup

setup(
    name="blabla",
    version="0.1",
    description="Novoic linguistics feature extraction package.",
    url="http://github.com/novoic/BlaBla",
    author="Abhishek Shivkumar",
    author_email="abhishek@novoic.com",
    license="GPL-3.0",
    packages=[
        "blabla",
        "blabla.sentence_processor",
        "blabla.utils",
        "blabla.language_resources",
        "blabla.sentence_aggregators",
    ],
    keywords=[
        "feature-extraction",
        "language",
        "machine-learning",
        "text-processing",
        "python",
        "natural-language-processing",
        "nlp",
        "stanza",
        "dementia",
        "alzheimers-disease",
        "parkinsons-disease",
    ],
    download_url="https://github.com/novoic/blabla/archive/v0.1.tar.gz",
    install_requires=[
        "stanza==1.0.0",
        "flask==1.1.2",
        "jsonpickle==1.4",
        "pyyaml==5.3.1",
        "anytree==2.8.0",
        "nltk==3.5",
        "ipython==7.13.0",
        "jsonschema==3.2.0",
        "pyyaml==5.3.1",
        "pandas==1.0.3"
    ],
    package_data={"": ["*.txt"]},
    include_package_data=True,
    scripts=["bin/blabla"],
    zip_safe=False,
    classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
