# jenkins-test-pipeline

## To test
```

python3  parser_watcher.py   'davidboukari@gmail.com' 'srv,Code,Timestamp\nmyserver5,CODEA2,2021-05-11T12:37:42, 90, (90%)\nmyserver4,CODEA2,2021-05-11T12:39:47, 85, (85%)\nmyserver3,CODEA2,2021-05-11T12:33:48, 87, (87%)\nmyserver10,CODEA2,2021-05-11T12:31:46, 93, (93%)\nmysever8,CODEA2,2021-05-11T12:39:43, 130, (130%)\n' 'Alert CPU' 'server_mail.csv' 'OPERATION_SYSTEM-CPU' acknowledge

# Multivalue key => value acknowledge ex: /ftp1/disk1  90
python3  parser_watcher.py   'davidboukari@gmail.com' 'srv,Code,Timestamp\nmyserver5,CODEA2,2021-05-11T12:37:42, /bigdata/disk1, 90, (90%)\nmyserver4,CODEA2,2021-05-11T12:39:47, /bigdata/disk1, 85, (85%)\nmyserver3,CODEA2,2021-05-11T12:33:48, /ftp1, ,87, (87%)\nmyserver10,CODEA2,2021-05-11T12:31:46, /nfs/nfs1, 93, (93%)\nmyserver8,CODEA2,2021-05-11T12:39:43, /rootvg, 130, (130%)\n' 'Alert CPU' 'server_mail.csv' 'OPERATION_SYSTEM-DISK' acknowledge
```

## Coverage
```
pytest -v --tb=short  --cov=app -cov-branch --cov-report xml:coverage.xml --junitxml report.xml 
```