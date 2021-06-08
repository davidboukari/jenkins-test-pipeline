pipeline
{
  agent any
  stages
  {
/*
    stage('Sonarqube')
    {
      environment
      {
        scannerHome = tool 'SonarQubeScanner'
      }
      steps
      {
        withSonarQubeEnv('sonarqube-jenkins-test-pipeline')
        {
          sh "${scannerHome}/bin/sonar-scanner"
        }
        timeout(time: 10, unit: 'MINUTES')
        {
          waitForQualityGate abortPipeline: true
        }
      }
    }
*/
    stage('Notification Email')
    {
      steps
      {
        script
        {
          float my_float = "123 ".trim() as float
          println "my_float=" + my_float
            
          def scmVars = checkout scm
          // Call the function
          def map_all_acknowledge_rules = load_acknowledges(ACKNOWLEDGE_FILE)

          //println scmVars.toString() 
          SERVER_FILE_MAIL = 'server_mail.csv'
          if( MAIL_MESSAGE != "No subject" )
          {
            map_all_server = [:]
            if (fileExists(SERVER_FILE_MAIL))
            {
              echo SERVER_FILE_MAIL + ' found OK'
              error_lines = ''
              readFile(SERVER_FILE_MAIL).split('\n').eachWithIndex
              {
                line, count -> def fields = line.split(';')
                try
                {
                  map_all_server[fields[0]] = fields
                }
                catch( Exception e )
                {
                  println e
                  error_lines += "line:" + count + " - content:" + line + "\n"
                } 
              }
              if( error_lines != '' )
              {
                println "Send mail for:\n" + error_lines
                try
                {
                  body_message = "File: ${scmVars.GIT_URL}/blob/${scmVars.GIT_BRANCH}/${SERVER_FILE_MAIL}\nJob: ${BUILD_URL}\n\n${error_lines}"
                  emailext  to: MAIL_TO, subject: "Error in file ${SERVER_FILE_MAIL}", body: body_message
                }
                catch(Exception e)
                {
                  println e
                }
              }
              map_all_server.each
              {
                key, value -> println key.toString() + '-' + value.toString()
              }
            }
            else
            {
              error('Aborting: Machines.csv Not found. Failing.')
            }
            String param_server_list="srv,Code,Timestamp\nmyserver5,CODEA2,2021-05-11T12:37:42, 90, (90%)\nmysever4,CODEA2,2021-05-11T12:39:47, 85, (85%)\nmyserver3,CODEA2,2021-05-11T12:33:48, 87, (87%)\nmyserver10,CODEA2,2021-05-11T12:31:46, 93, (93%)\nmysever8,CODEA2,2021-05-11T12:39:43, 130, (130%)\n"
            mail_to = "unknown@localhost.localdomain"
            mail_subject = "Metric CPU errors"
            mail_alert_type = 'OPERATION_SYSTEM-CPU'

            String[] list_server_on_error = param_server_list.tokenize('\n')
            line = 0
            for( String my_server_info:  list_server_on_error)
            {
              if( line > 0 )
              {
                println my_server_info;
                my_current_server = my_server_info.tokenize(',')
                my_server = my_current_server[0]
                println "--->" + my_server
                is_ack = false
                try
                {
                  // Find mail
                  csv_info = map_all_server[my_server]
                  email_addr = csv_info[4]
                  // Add the Team to the subject 
                  email_subject = mail_subject + ' - (' +  csv_info[3]  + ')'
                  println "------------>" + email_addr
                  
                  is_ack = is_acknowledged( my_current_server, map_all_acknowledge_rules, mail_alert_type) 
                }
                catch( Exception e)
                {
                  println "Server not found in the CSV file"
                  email_addr = mail_to
                  email_subject = mail_subject
                }
                email_message = my_server_info
                if(  !is_ack )
                {
                  println "emailext body: " + email_message + ", subject: " + email_subject + ", to: " + email_addr
                  try
                  {
                    emailext to: "${email_addr}", subject: "${email_subject}", body: "${email_message}"
                  }
                  catch(Exception ex1)
                  {
                    println ex1
                  }
                }
              }
              line++
             }
           }
           else
           {
             println "There is no message to send"
           }
        }
      }
    }
/*
    stage('Notification Mattermost')
    {
       steps
       {
         // Send to Mattermost webhook
          mattermostSend (
            color: "#2A42EA",
            channel: 'devops',
            endpoint: 'http://192.168.0.133:8065/hooks/uwfu8ohdojyi9gbf1gtykkyzeo',
            message: "Hello from jenkins pipeline --"
          )
       }
    }
*/
/*
    stage('GIT')
    {
       steps
       {
         echo 'Get the git source ...'
         sleep(2)
       }
    }

    stage('Unit Tests')
    {
      steps
      {
        echo 'Unit Tests...'
        //sh 'pip install --upgrade --user tox'
        sh 'tox -r'
      }
    }

    stage('Security Tests')
    {
      steps
      {
        echo 'Security Tests...'
        sleep(2)
        //sh 'tox -r -e envsecurity'
      }
    }

    stage('Sonarqube')
    {
      environment
      {
        scannerHome = tool 'SonarQubeScanner'
      }
      steps
      {
        withSonarQubeEnv('sonarqube')
        {
          sh "${scannerHome}/bin/sonar-scanner"
        }
        timeout(time: 10, unit: 'MINUTES')
        {
          waitForQualityGate abortPipeline: true
        }
      }
    }

    stage('Deployment')
    {
      steps
      {
        echo 'Deployment...'
        sleep(2)
        // DEV

        // UAT

        // PRD
      }
    }
*/

  }

  post {
    always 
    {
      script
      {
        try
        {
          emailext body: "Success From jenkins msg...", subject: "From jenkins Success job ...", to: 'root@localhost'
        }
        catch(Exception ex)
        {
          println ex    
        }
    
      }
    }
  }

}

def is_acknowledged(alert, acknowledges, mail_alert_type)
{
  echo "is_acknowledged()"    
  //mail_alert_type
  host = alert[0].trim()
  float percent = alert[3].trim() as float 
  
  /*
  echo "host=" + host
  echo "percent" + 
  
  
  println "-------------------------------------------------"
  println acknowledges
  println "-------------------------------------------------"
  */
  for( ack in acknowledges )
  {
/*
    println "key=" + ack.key  
    println "value=" + ack.value
*/
    ack_host = ack.value[0].trim()
    ack_alert = ack.value[1].trim()
    ack_value = ack.value[2].trim()
   /* if( ack_value_tmp != '*' )
    {
        float ack_value =  ack_value_tmp as float 
    }
    else
    {
       ack_value =  '*'
    }*/
   /*
    echo "--> ack_host=" + ack_host 
    echo "--> ack_alert=" + ack_alert
    echo "----------------> ack_value=" + ack_value
   */
    if( ack_host == '*' || host == ack_host)
    {
      //echo "Host found ${ack_host} == ${host}"
      if( ack_alert == '*' || ack_alert == mail_alert_type )
      {
          if(ack_value == '*' )
          {
              echo "host=${host}, percent=${percent}  is acknowledged by ack_host=${ack_host}, ack_alert=${ack_alert}, ack_value=${ack_value}"
              echo "is_acknowledged() return true"
              return true
          }
          else
          {
              float ack_value_float = ack_value as float
              if(ack_value_float <= percent)
              {
                echo "host=${host}, percent=${percent}  is acknowledged by ack_host=${ack_host}, ack_alert=${ack_alert}, ack_value=${ack_value}"
                echo "is_acknowledged() return true"
                return true  
              }
          }
      }
    }
  }
  echo "is_acknowledged() return false"
  return false;    
}


def load_acknowledges(acknowledge_file)
{
  map_all_acknowledge_rules = [:]
  if (fileExists(acknowledge_file))
  {
    echo acknowledge_file + ' found OK'
    error_lines = ''
    readFile(acknowledge_file).split('\n').eachWithIndex
    {
      line, count -> def fields = line.split(';')
      try
      {
        if( !fields[0].startsWith('#') )
        {
          echo "OK: ${line}"    
          map_all_acknowledge_rules[count] = fields
        }  
        
      }
      catch( Exception e )
      {
        println e
        error_lines += "line:" + count + " - content:" + line + "\n"
      }
    }
    if( error_lines != '' )
    {
      println "Send mail for:\n" + error_lines
/*
      try
      {
        body_message = "File: ${scmVars.GIT_URL}/blob/${scmVars.GIT_BRANCH}/${SERVER_FILE_MAIL}\nJob: ${BUILD_URL}\n\n${error_lines}"
        emailext  to: MAIL_TO, subject: "Error in file ${SERVER_FILE_MAIL}", body: body_message
      }
      catch(Exception e)
      {
        println e
      }
*/ 
    }    
  }
  return map_all_acknowledge_rules 
}


