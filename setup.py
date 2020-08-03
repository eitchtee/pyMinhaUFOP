import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyminhaufop",
    packages=['pyminhaufop'],
    version="0.0.1",
    license='MIT',
    author="Herculino Trotta Neto",
    author_email="herculinotrotta@gmail.com",
    description="Wrapper não-oficial para a API mobile da MinhaUFOP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['UFOP', 'api'],
    url="https://github.com/eitchtee/pyMinhaUFOP",
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    install_requires=[
          'requests',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)