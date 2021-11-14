#!/usr/bin/groovy

@Grab('com.xlson.groovycsv:groovycsv:1.3')
import static com.xlson.groovycsv.CsvParser.parseCsv

fh = new File('server_mail.csv')
def csv_content = fh.getText('utf-8')
def data_iterator = parseCsv(csv_content, separator: ';', readFirstLine: false)
map_all_server = [:]

/* Build the array "mail" => { */
i = 0
for (line in data_iterator) {
  map_all_server[line[0]] = line.values
}

for (l in map_all_server) {
  println l.key + '=>' + l.value
}

String param_server_list="srv,Code,Timestamp\nmyserver5,CODEA2,2021-05-11T12:37:42,(60%)\nmysever4,CODEA2,2021-05-11T12:39:47,(60%)\nmyserver3,CODEA2,2021-05-11T12:33:48,(60%)\nmyserver10,CODEA2,2021-05-11T12:31:46,(60%)\nmysever8,CODEA2,2021-05-11T12:39:43,(60%)\n"
mail_to = "unknown@localhost.localdomain"
mail_subject = "Metric CPU errors"

String[] list_server_on_error = param_server_list.tokenize('\n')
line = 0
for( String my_server_info:  list_server_on_error)
{ 
  if( line > 0 )
  {
    println my_server_info;
    my_server = my_server_info.tokenize(',')[0]
    println "--->" + my_server 

    try
    {
      // Find mail
      csv_info = map_all_server.get(my_server).value
      email_addr = csv_info[4]
      email_subject = mail_subject + ' - (' +  csv_info[3]  + ')'
      println "------------>" + email_addr
      // Send an email
    }
    catch( Exception e) 
    {
      println "Server not found in the CSV file"
      email_addr = mail_to
      email_subject = mail_subject
    }
    email_message = my_server_info

    println "emailext body: " + email_message + ", subject: " + email_subject + ", to: " + email_addr

  
    // emailext body: "${mail_message}", subject: "${mail_subject}", to: "${mail_to}"
  }
  line++
} 


