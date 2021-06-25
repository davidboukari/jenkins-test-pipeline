# jenkins-test-pipeline

## install the Package
```
pip install tox
pip install setuptools 
pip install setuptools 
pip install --upgrade pip
pip install corage
pip install coverage
pip install pytest-cov
pip install flake8
pip install prettyprinter 
pip install pylint
pip install setuptools
pip install wheel 
```

## To test
```

python3  parser_watcher.py   'davidboukari@gmail.com' 'srv,Code,Timestamp\nmyserver5,CODEA2,2021-05-11T12:37:42, 90, (90%)\nmyserver4,CODEA2,2021-05-11T12:39:47, 85, (85%)\nmyserver3,CODEA2,2021-05-11T12:33:48, 87, (87%)\nmyserver10,CODEA2,2021-05-11T12:31:46, 93, (93%)\nmysever8,CODEA2,2021-05-11T12:39:43, 130, (130%)\n' 'Alert CPU' 'server_mail.csv' 'OPERATION_SYSTEM-CPU' acknowledge

# Multivalue key => value acknowledge ex: /ftp1/disk1  90
python3  parser_watcher.py   'davidboukari@gmail.com' 'srv,Code,Timestamp\nmyserver5,CODEA2,2021-05-11T12:37:42, /bigdata/disk1, 90, (90%)\nmyserver4,CODEA2,2021-05-11T12:39:47, /bigdata/disk1, 85, (85%)\nmyserver3,CODEA2,2021-05-11T12:33:48, /ftp1, ,87, (87%)\nmyserver10,CODEA2,2021-05-11T12:31:46, /nfs/nfs1, 93, (93%)\nmyserver8,CODEA2,2021-05-11T12:39:43, /rootvg, 130, (130%)\n' 'Alert CPU' 'server_mail.csv' 'OPERATION_SYSTEM-DISK' acknowledge
```

## pytest Coverage
```
pytest -v --tb=short  --cov=app -cov-branch --cov-report xml:coverage.xml --junitxml report.xml 
```

### flake8
```
 flake8 --max-line-length=150 --max-complexity=10
```

## tox

```
cat tox.ini
[tox]
envlist = py38
skipsdist = True

[flake8]
max-line-length=150
max-complexity=13
#filename = app

[testenv]
deps = -r requirements.txt
commands= pytest
          flake8 app tests
          pylint app

[pytest]
addopts  = -v
           --tb=short
           --cov=app
           -cov-branch
           --cov-report xml:coverage.xml
           --junitxml report.xml
```

### Execute tox
```
tox -r
```

### Create the setup.py
```
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
            ...
      ],
      license="Apache 2.0"
      )

```

```
python setup.py sdist
python setup.py bdist_wheel

```
