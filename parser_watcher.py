import os
import sys
import csv
import glob
from prettyprinter import pprint

# To test
# python3  parser_watcher.py   'davidboukari@gmail.com' 'srv,Code,Timestamp\nmyserver5,CODEA2,2021-05-11T12:37:42, 90, (90%)\nmyserver4,CODEA2,2021-05-11T12:39:47, 85, (85%)\nmyserver3,CODEA2,2021-05-11T12:33:48, 87, (87%)\nmyserver10,CODEA2,2021-05-11T12:31:46, 93, (93%)\nmysever8,CODEA2,2021-05-11T12:39:43, 130, (130%)\n' 'Alert CPU' 'server_mail.csv' 'OPERATION_SYSTEM-CPU' acknowledge

def get_dico_from_csv_file(csv_file):
  print(f'-----> get_dico_from_csv_file({csv_file})')
  dico = {}
  current_line = 0
  with open(csv_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
      try:
        if row[0][0] != '#':
          dico[ row[0] ] = row
      except:
        print(f'Error: line {current_line+1}' + ', '.join(row) )
      current_line += 1
  return dico

def is_acknowledged(alert, acknowledges, mail_alert_type):
  host = alert[0].strip()
  percent = float( alert[3].strip() )
  for ack_file in acknowledges:
    for ack in acknowledges[ack_file]:
      ack_host = acknowledges[ack_file][ack][0].strip()
      ack_alert = acknowledges[ack_file][ack][1].strip()
      ack_value = acknowledges[ack_file][ack][2].strip()
      if ack_host == '*' or host == ack_host:
        if ack_alert == '*' or ack_alert == mail_alert_type:
          if ack_value == '*':
            print(f'host={host}, percent={percent}  is acknowledged by rule_file={ack_file}, ack_host={ack_host}, ack_alert={ack_alert}, ack_value={ack_value}')
            return True
          else:
            ack_value_float = float(ack_value)
            if ack_value_float <= percent:
              print(f'host={host}, percent={percent}  is acknowledged by rule_file={ack_file}, ack_host={ack_host}, ack_alert={ack_alert}, ack_value={ack_value}')
              return True  
  print(f'host={host}, percent={percent} is_acknowledged() return false')
  return False;    


def get_mail_from_hostname(hostname, server_team_info, default_email):
  try:
    email = server_team_info[hostname][4]
  except:
    email = default_email
  return email

if __name__ == "__main__":
  os.environ['PYTHON_MAIL_LIST_RETURN'] = ""
  DEFAULT_MAIL_TO = sys.argv[1] 
  MAIL_MESSAGE = sys.argv[2]
  MAIL_SUBJECT = sys.argv[3]
  INFRA_MAIL_FILE = sys.argv[4]
  MAIL_METRIC = sys.argv[5]
  RULES_DIRECTORY = sys.argv[6]
  
  print(f'DEFAULT_MAIL_TO={DEFAULT_MAIL_TO}')
  print(f'MAIL_MESSAGE={MAIL_MESSAGE}')
  print(f'MAIL_SUBJECT={MAIL_SUBJECT}')
  print(f'INFRA_MAIL_FILE={INFRA_MAIL_FILE}')
  print(f'MAIL_METRIC={MAIL_METRIC}')
  print(f'RULES_DIRECTORY={RULES_DIRECTORY}')

  # Get the server team mail list
  server_team_info = get_dico_from_csv_file( INFRA_MAIL_FILE )

  # Get acknowledge file
  list_rules_files = glob.glob( RULES_DIRECTORY + '/*.rules' ) 
  acknowledge_rules_list = {}
  if list_rules_files is not None:
    for i in range(0, len(list_rules_files)):
      acknowledge_rules_list[list_rules_files[i]] = get_dico_from_csv_file( list_rules_files[i] )
  
  # Parse Message
  alert_lines = MAIL_MESSAGE.split("\\n")
  alert_current_number = 0
  if alert_lines is not None:
      for current_alert in alert_lines:
        is_ack = False
        if alert_current_number > 0:
          info_alert = current_alert.split(',')
          if info_alert is not None:
            try:
              server_infos = server_team_info[ info_alert[0] ]
              my_current_server = server_infos[0]
              is_ack = is_acknowledged( info_alert, acknowledge_rules_list, MAIL_METRIC) 
              print(f'is_ack={is_ack}')                
            except Exception as e:
              print('Error: --------')
              print(e)
            if is_ack:
              print("True => Nothing to do")
            else:
              server_mail_address = get_mail_from_hostname( info_alert[0], server_team_info, DEFAULT_MAIL_TO  ) 
              if os.environ['PYTHON_MAIL_LIST_RETURN'] == '':
                os.environ['PYTHON_MAIL_LIST_RETURN'] = current_alert + ',' + server_mail_address  + "\n" 
              else: 
                os.environ['PYTHON_MAIL_LIST_RETURN'] += current_alert + ',' + server_mail_address  +  "\n" 
              print("False ---") 
        alert_current_number += 1
  print(f"os.environ['PYTHON_MAIL_LIST_RETURN']={os.environ['PYTHON_MAIL_LIST_RETURN']}")

 
