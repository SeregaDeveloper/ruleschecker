import os
import json

kbase_path = "/path/to/your/rules"
rulenames = []

def get_all_rulenames():
    '''
    Found all rulenames and write them to base
    '''
    for directory in os.listdir(kbase_path):
        #print(directory)
        file_path = kbase_path + "/" + str(directory)
        for filename in os.listdir(file_path):
            #print (filename)
            if filename == "rule.co":
                rule_path = file_path + "/" + filename
                file = open(rule_path,"r")
                text = file.read()
                rulename = text.split("\nrule ")[1]
                rulename = rulename.split(":")[0]
                #print(rulename)
                if rulename not in rulenames:
                    rulenames.append(rulename)
    return rulenames

def find_rules(word):
    '''
    Print all connected rules from actual base
    '''
    connected = []
    for directory in os.listdir(kbase_path):
        #print(directory)
        file_path = kbase_path + "/" + str(directory)
        for filename in os.listdir(file_path):
            #print (filename)
            if filename == "rule.co":
                rule_path = file_path + "/" + filename
                file = open(rule_path,"r")
                text = file.read()
                rulename = text.split("\nrule ")[1]
                rulename = rulename.split(":")[0]
                if word in text and word != rulename:
                    #print(word + f" Found in {directory}, rulename: {rulename}")
                    connected.append({"connected_rule": rulename, "connected_rule_id": directory})
    #print(connected)
    return connected

def check_answer(answer):
    '''
    Checks answer if search is manual
    '''
    if answer == None:
        return "No linked rules"
    else:
        return answer

def get_all_connected_rules():
    '''
    Search for connected rules
    '''
    all_base = {}
    for rule in rulenames:
        result = find_rules(rule)
        if result != []:
            all_base[rule] = result
    return all_base

def export_info(data):
    '''
    Export info in json
    '''
    output = open("allbase.json","a")
    output.write(json.dumps(data))

def log(msg):
    '''
    Write to log
    '''
    output = open("log.txt","a")
    output.write(msg + "\n")

def visualise(base):
    '''
    Get visual representation of a base -> TO DO
    '''
    return 0

def main():
    try:
        get_all_rulenames()
        export_info(get_all_connected_rules())
    except Exception as err:
        log(err)

    return 0

main()
