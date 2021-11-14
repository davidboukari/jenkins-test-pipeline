from setuptools import setup, find_packages

setup(name="jenkins-test-pipeline",
      version="0.0.1",
      description="A pipeline test with alert managing https://github.com/davidboukari/jenkins-test-pipeline.git",
      author="David Boukari",
      author_email="davidboukari@gmail.com",
      packages=find_packages(),
      install_requires=[
            'appdirs==1.4.4',
            'astroid==2.5.6',
            'attrs==21.2.0',
            'colorful==0.5.4',
            'coverage==5.5',
            'csv-reader==1.2.0',
            'distlib==0.3.2',
            'filelock==3.0.12',
            'flake8==3.9.2',
            'glob2==0.7',
            'iniconfig==1.1.1',
            'isort==5.9.1',
            'lazy-object-proxy==1.6.0',
            'mccabe==0.6.1',
            'packaging==20.9',
            'pluggy==0.13.1',
            'pprintpp==0.4.0',
            'prettyprinter==0.18.0',
            'py==1.10.0',
            'pycodestyle==2.7.0',
            'pyflakes==2.3.1',
            'Pygments==2.9.0',
            'pylint==2.8.3',
            'pyparsing==2.4.7',
            'pytest==6.2.4',
            'pytest-cov==2.12.1',
            'six==1.16.0',
            'toml==0.10.2',
            'tox==3.23.1',
            'virtualenv==20.4.7',
            'wrapt==1.12.1'
      ],
      license="Apache 2.0"
      )

# import setuptools
#
# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
#
# setuptools.setup(
#     name="jenkins-test-pipeline",
#     version="0.0.1",
#     author="David Boukari",
#     author_email="davidboukari@gmail.com",
#     description="A small example package",
#     long_description="long_description ...",
#     long_description_content_type="text/markdown",
#     url="https://github.com/davidboukari/jenkins-test-pipeline.git",
#     package_dir={"app"},
#     packages=setuptools.find_packages(where="app"),
#     python_requires=">=3.6",
# )
