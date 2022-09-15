import phe as paillier
import json

def storeKeys():
    public_key, private_key = paillier.generate_paillier_keypair()
    keys={}
    keys['public_key'] = {'n': public_key.n}
    keys['private_key'] = {'p': private_key.p, 'q':private_key.q}
    with open('patientkeys.json', 'w') as file:
        json.dump(keys, file)
    

def getKeys():
    with open('patientkeys.json', 'r') as file:
        keys=json.load(file)
        pub_key = paillier.PaillierPublicKey(n=int(keys['public_key']['n']))
        priv_key= paillier.PaillierPrivateKey(pub_key, keys['private_key']['p'],keys['private_key']['q'])
        return pub_key, priv_key


def serializeData(public_key, data):
    encrypted_data_list = [public_key.encrypt(x) for x in data]
    encrypted_data={}
    encrypted_data['public_key'] = {'n' : public_key.n}
    encrypted_data['values'] = [(str(x.ciphertext()), x.exponent) for x in encrypted_data_list]
    serialized = json.dumps(encrypted_data)
    return serialized

def loadAnswer():
    with open('answer.json', 'r') as file:
        ans=json.load(file)
        answer=json.loads(ans)
        return answer

pub_key, priv_key = getKeys()
data = Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age = [4, 150, 85, 30, 12, 20, 0.6,25]
serializeData(pub_key, data)
datafile=serializeData(pub_key, data)
with open('patient.json', 'w') as file:
    json.dump(datafile, file)

print(serializeData())