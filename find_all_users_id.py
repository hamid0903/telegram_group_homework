from pyexpat.errors import messages
from read_data import read_data
import json
#def find_all_users_id(data: dict)->list:
"""
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    #f=open('data\result.json',encoding='utf8').read()
    #data=json.loads(f)
    #return len(data['id'])

f=open('result.json',encoding='utf8').read()
data=json.loads(f)
print(data["id"])