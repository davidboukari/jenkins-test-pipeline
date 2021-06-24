import pytest
from app.bin.parser_watcher import main

'''Test parser_watcher'''


class TestParserWatcher:
    @staticmethod
    @pytest.mark.parametrize('argv', [['parser_watcher.py', 'davidboukari@gmail.com',
                                       'srv,Code,Timestamp\n'
                                       'myserver5,CODEA2,2021-05-11T12:37:42, 90, (90%)\n'
                                       'myserver4,CODEA2,2021-05-11T12:39:47, 85, (85%)\n'
                                       'myserver3,CODEA2,2021-05-11T12:33:48, 87, (87%)\n'
                                       'myserver10,CODEA2,2021-05-11T12:31:46, 93, (93%)\n'
                                       'mysever8,CODEA2,2021-05-11T12:39:43, 130, (130%)\n',
                                       'Alert CPU',
                                       'datas/server_mail.csv',
                                       'OPERATION_SYSTEM-CPU',
                                       'datas/acknowledge'],
                                      ['parser_watcher.py', 'davidboukari@gmail.com', 'srv,Code,Timestamp\n'
                                       'myserver5,CODEA2,2021-05-11T12:37:42, /bigdata/disk1, 90, (90%)\n'
                                       'myserver4,CODEA2,2021-05-11T12:39:47, /bigdata/disk1, 85, (85%)\n'
                                       'myserver3,CODEA2,2021-05-11T12:33:48, /ftp1, ,87, (87%)\n'
                                       'myserver10,CODEA2,2021-05-11T12:31:46, /nfs/nfs1, 93, (93%)\n'
                                       'myserver8,CODEA2,2021-05-11T12:39:43, /rootvg, 130, (130%)\n',
                                       'Alert CPU',
                                       'datas/server_mail.csv',
                                       'OPERATION_SYSTEM-DISK',
                                       'datas/acknowledge']
                                      ])
    def test_main(argv):
        exec_code = main(argv)
        assert exec_code == 0

