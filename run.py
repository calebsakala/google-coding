#! /usr/bin/env python3

import os 
import requests

directory = "/data/feedback"
feedback_list = []

for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as f:
                title = f.readline().strip()
                name = f.readline().strip()
                date = f.readline().strip()
                feedback = f.readlines()[0].strip()
                person_dict = {"title":title, "name": name, "date": date, "feedback": feedback}
                feedback_list.append(person_dict)

for person in feedback_list:
        response = requests.post('http://104.154.71.132/feedback/', data=person)
        if response.ok:
                print("Congratulations! Entry loaded.")
        else:
                print(f"Error: {response.status_code})")
