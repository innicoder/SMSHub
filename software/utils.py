def verify(contacts):
    '''verify contacts (with ruleset) 
    
    Verify that each contact exists, non-emtpy row, and with each rule
    following rules are applied
    - min 4
    - max 14
    - starts with either +381 or 381

    Additionally since the API only accepts 381 (without +) 
    we remove symb `+` if it exists
    
    Args:
        contacts: lists of contacts (nubmers)
    
    Returns:
        returns: valid list of contacts (with rules applied)
    '''
    contacts = contacts.split()
    filtered_contacts = []
    for x in contacts:
        if x.startswith('+381') or x.startswith('381') and len(x) >= 4 and len(x) <= 14:
            filtered_contacts.append(x.strip().lstrip('+'))
    return filtered_contacts