# Python exercises

python -m venv E:\dev\MyPythonExcersises\venv
pip install -t <direct directory> <package>

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./public/scripts/cert.json')
firebase_admin.initialize_app(cred)
client = firestore.client()
client.collection('test').document('foo').set({
    'mytime':firestore.SERVER_TIMESTAMP
})

data = client.collection('test').document('foo').get().to_dict()
print 'Full object:', data
print 'Timestamp:', data['mytime']

https://pypi.org/project/google-cloud-firestore/

[![Build Status](https://travis-ci.com/LairdStreak/MyPythonExcersises.svg?branch=master)](https://travis-ci.com/LairdStreak/MyPythonExcersises)