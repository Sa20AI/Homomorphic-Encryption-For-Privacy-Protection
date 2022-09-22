import imp
from logmodel import LogModel
import phe as paillier
import json


def getData():
    with open('patient.json', 'r') as file:
        ans = json.load(file)
    answer = json.loads(ans)
    return answer


print(getData())
