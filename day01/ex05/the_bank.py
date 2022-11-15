class Account(object): 

    ID_COUNT = 1

    def __init__(self, name, **kwargs) : 
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT 
        Account.ID_COUNT += 1 
        self.name = name
        if not hasattr(self, 'value') :
            self.value = 0

        if self.value < 0 :
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str) :
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount) : 
        self.value += amount

class Bank(object): 
    """The bank"""

    def __init__(self): 
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account:  Account() new account to append
            @return   True if success, False if an error occured
        """

        if not isinstance(new_account, Account) :
            return False

        for accounts in self.accounts :
            if accounts.name == new_account.name :
                return False

        self.accounts.append(new_account)
        return True

    def isCorrupted(self, new_account, fixMode = False) :

        matched = {'name', 'id', 'value', 'addr', 'zip'}
        for attribute in dir(new_account) :
            if attribute.startswith('b') is True :
                if fixMode is True : del new_account.__dict__[attribute]
                else: return True
            if attribute.startswith('zip') is True :
                matched.remove('zip')
            if attribute.startswith('addr') is True :
                matched.remove('addr')
            if attribute == 'name' and type(new_account.name) == str :
                matched.remove('name')
            if attribute == 'value' and (type(new_account.value) == int or type(new_account.value) == float) :
                matched.remove('value')
            if attribute == 'id' and type(new_account.id) == int :
                matched.remove('id')
        
        if len(matched) != 0 :  
            if fixMode is True :
                for missing in matched :
                    if missing == 'zip' :   new_account.__dict__['zip'] = 'zip default'
                    if missing == 'addr' :  new_account.__dict__['addr'] = 'addr default'
                    if missing == 'value' : new_account.__dict__['value'] = 0
                    if missing == 'id' : new_account.__dict__['id'] = 0
                    if missing == 'name' : new_account.__dict__['name'] = 'name default'
            else :
                return True
        if len(dir(new_account)) % 2 == 0 :
            if fixMode is True:
                new_account.__dict__['_'] = '_'
            return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        originAcount = [account for account in self.accounts if account.name == origin]
        destAcount = [account for account in self.accounts if account.name == dest]
        if amount < 0 or len(originAcount) != 1 or len(destAcount) != 1:
            return False
        originAcount = originAcount[0]
        destAcount = destAcount[0]

        if self.isCorrupted(originAcount) is True or self.isCorrupted(destAcount) is True :
            return False

        if origin != dest :
            if amount > originAcount.value :
                return False
            originAcount.transfer(-amount)
            destAcount.transfer(amount)
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
                @name:   str(name) of the account
                @return  True if success, False if an error occured
            """
        if type(name) != str :
            return False
        acount = [ac for ac in self.accounts if ac.name == name]
        if len(acount) != 1 :
            return False
        self.isCorrupted(acount[0], True)
        return True