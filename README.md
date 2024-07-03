- ##### Clone Framework
    <pre>
    git clone https://github.com/Ram051258/Assignment.git</pre>
- ##### Copy the web_ui_testing folder to your project location and open command prompt from there.

- ##### Requirements before running the test
    <pre>
    1) Should use python 3.9 version (recommended) as per library versions mentioned in requriements.txt file
    2) Change ip address in the test file 'test_verify_backend_message.py' as per the project deployed locally. 
        eg: i used http://192.168.59.100:30406/ as per my 'kubectl get service' command. cluster ip and port.
        Note: Added resources screenshots for better understand.
        

    </pre>
    
- ##### Create and activate virtual environment
    <pre>
    python -m venv ENVIRONMENT_NAME
    ENVIRONMENT_NAME\scripts\activate</pre>   
- ##### Install required Python Packages
    <pre>
    pip install -r requirements.txt</pre>
- ##### Run the test
    <pre>
    type the command "pytest" in the same command prompt and the test runs automatically by picking chrome brower.</pre>
