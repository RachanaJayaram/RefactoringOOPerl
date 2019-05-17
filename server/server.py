import os
from flask import Flask,render_template, request,json,Response,jsonify
import socket
import sys
import subprocess


app = Flask(__name__)
@app.route('/') 
def default():
	return '<h1>Refactoring Object Oriented Perl and Translating it to Python</h1>'

@app.route('/translator')
def translator():
        return render_template('OOPerl.html',send_perl="",send_python="",perl_output="",python_output="") #using jinja2 to render voiceWebInterface.html template at this url

@app.route('/translatorPost',methods=['GET', 'POST'])
def translatorPost(): 
    if request.method == 'POST':
        
        file_name =  request.form['file_name'] 
        
        scratch_file=open("scratch_pad.txt","w+")
        scratch_file.write(file_name)
        scratch_file.close()   

        os.system("python stage_1_parser.py")
        os.system("python stage_2_parser.py")
        
        output_file_name=file_name.split('testing/input/')[1]
    
    # condition for when module to be tranlated is in a sub folder input/server/a.pm -> input/server/a.py
        if '/'  in output_file_name:
            output_path='testing/output/' + output_file_name[:output_file_name.rindex('/')]
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            output_file_name=output_path + output_file_name[output_file_name.rindex('/'):output_file_name.index('.')] + '.py'

        else:
            output_file_name='testing/output/' + output_file_name[:output_file_name.index('.')] + '.py'        
        perl_result= subprocess.check_output("perl "+file_name).decode("utf-8")
        python_result= subprocess.check_output("python "+output_file_name).decode("utf-8")
        print(perl_result,python_result)
        
        ip_perl=open(file_name,'r')      
        send_perl=""
        for line in ip_perl.readlines():
            send_perl+=line


        op_python=open(output_file_name,'r')
        send_python=""
        for line in op_python.readlines():
            pre=""
            while(len(line)!=0 and ord(line[0])==9):
                pre+="&emsp;"*4
                line=line[1:]           
            line=pre+line+"<br>"
            print(line)
            send_python+=line
        
        op_python.close()
        ip_perl.close()
        
        # print(send_perl)
        # print(send_python)

        return render_template('OOPerl.html',send_perl=send_perl,send_python=send_python,perl_output=perl_result,python_output=python_result) #using jinja2 to render voiceWebInterface.html template at this url



if __name__=="__main__":
		app.run("127.0.0.1","4200",debug=True)
