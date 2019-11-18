import json, requests, csv, sys

logFile ='./updateWorkfront.log'

with open('./report_full.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data = json.dumps(row)
        # print(data)
        URL = "" # Workfront endpoint url
        try:
            r = requests.post(url=URL, data=data, headers={'content-type':'application/json'})
            if(r.status_code != 200):
                raise row
            else:
                print("[SUCCESS:] "+row["ticketId"])
		l = open(logFile, "a")
                l.write("[SUCCESS:] "+row["ticketId"]+"\n")
		l.close()
        except:
            print("[ERROR:] "+row["ticketId"]+" Failed")
	    l = open(logFile, "a")
            l.write("[ERROR:] "+row["ticketId"]+" Failed\n")
            l.close()
            pass
