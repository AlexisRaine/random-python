# updateWorkfront.py
This python script takes a CSV file and one at a time sends data to a workfront endpoint URL.

I have since found it's better to send workfront a bulk amount of JSON data and allow the Fusion system to parse it on workfront's side instead of making thousands of calls to the API.
