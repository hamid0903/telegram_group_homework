from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    msg=[]
    msg=data['messages']
    user_name=[]
    idx=0
    d={}
    while idx<len(msg):
        d=msg[idx]
        for k,v in d.items():
            if k=="actor":
                user_name.append(v)
        idx+=1
        d={}
        user_name2=[]
        for item in user_name:
            if item not in user_name2:
                user_name2.append(item)
    return user_name2

data=read_data('result.json')
print(find_all_users_name(data))