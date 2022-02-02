from pyexpat.errors import messages
from read_data import read_data
import json
def find_all_users_id(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    msg=[]
    masg=data['messages']
    user_id=[]
    idx=0
    d={}
    indx=-1
    while idx<len(msg):
        d=msg[idx]
        for k,v in d.items():
            if k=="actor_id":
                user_id.append(v)
        idx+=1
        d={}
        user_id2=[]
        for item in user_id:
            if item not in user_id2:
                user_id2.append(item)
                    
    return user_id2
data=read_data('data/result.json')
print(find_all_users_id(data))