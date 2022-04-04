# administator ----> UserName : krishna, password: krishna123
import random

#------------------------------ USER Details of Account ------------------------------------------ 

user_details = {
    "BOB" : {
        1000 : {"username" : "krishna", "userpin" : 10, "balance" : 20000, "mobile number" : 9999999999, "Account Number" : 1789654, 'total_withdraw' : 0, 'limit' : 0, 'bankname': 'BOB', 'isNewPin': False},
        2000 : {"username" : "vishal",  "userpin" : 20, "balance" : 50000, "mobile number" : 9999999991, "Account Number" : 1789657 ,'total_withdraw' : 0, 'limit' : 0 , 'bankname': 'BOB', 'isNewPin': False },
    }, 
    "SBI" : {
        3000 : {"username" : "krishna", "userpin" : 30, "balance" : 4000, "mobile number" : 9999999992, "Account Number" : 1789647,  'total_withdraw' : 0, 'limit': 0, 'bankname': 'SBI', 'isNewPin': False},
        4000 : {"username" : "vishal",  "userpin" : 40, "balance" : 30000, "mobile number" : 9999999994, "Account Number" : 1789654 , 'total_withdraw' : 0, 'limit': 0, 'bankname': 'SBI', 'isNewPin': False}
    }
}

#------------------------------ ATM Details -----------------------------------------------------

atm_dict = {
    "BOB" : {
        "bob_atm_modasa" : {"total_atm_amount" :10000,"Location" : "modasa"},
        "bob_atm_ahmedabad" : {"total_atm_amount" : 10000,"Location" : "Ahmedabad"}
    },
    "SBI" : {
        "sbi_atm_modasa" : {"total_atm_amount" : 100000,"Location" : "modasa"},
        "sbi_atm_ahmedabad" : {"total_atm_amount" : 100000,"Location" : "Ahmedabad"}
    }
}
# ----------------------- Administrator Details ---------------------------------------
administrator_details = {
    'krishna': {'password': 'krishna123', 'email_id': 'krishna_singh@gamil.com', 'Phone Number': 9999999999}
}

#----------------- User validation --------------------------------------------
def userValidation(bankname,atmname):
    return getDetails(bankname, atmname)


# --------------- Get details from user side ------------------------------------
def getDetails(bankname, atmname):
    is_invalid = True
    user_detail = user_details[bankname]
    card_number = input("\nEnter Card Number : ")
    # pin_number =  input("\nEnter PIN Number  : ")
    if(card_number.isnumeric()):
        card_number = int(card_number)    
        data = user_detail.get(card_number,"Invalid Card Number")
        if card_number in user_detail:
            if(user_details[bankname][card_number]['isNewPin'] == True):
                pinChange = input("\nyou are new user so Please Change Pin Number For security purpose\nEnter NEW pin Number : ")
                if(pinChange.isnumeric()):
                    pinChange = int(pinChange)
                    user_details[bankname][card_number]['userpin'] = pinChange

                    print('new pin number ', user_details[bankname][card_number]['userpin'])
                    pin_number =  input("\nEnter Confirme PIN Number  : ")
                    if(pin_number.isnumeric()):
                        if(user_details[bankname][card_number]['userpin'] == int(pin_number)):
                            user_details[bankname][card_number]['isNewPin'] = False
                            displayOption(data, bankname, atmname)
                            is_invalid = False    
                        else:
                            print("\n {0:*^50s}  \n ".format(" Pin Number isn't Match "))
                            return is_invalid
                    else:
                         print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))               
                                 
                else:
                    print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))                
            else:
                pin_number =  input("\nEnter PIN Number  : ")
                if(pin_number.isnumeric()):

                    if int(pin_number) in data.values():
                        displayOption(data, bankname, atmname)
                        is_invalid = False
                    else: 
                        print("\n {0:*^50s}  \n ".format(" Invalid Pin Number "))
                        return is_invalid
                else:
                    print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))                                   
        else:
            print("\n {0:*^50s}  \n ".format(" Invalid Card Number "))
            return is_invalid  
    else:
        print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))                
      
#----------------- Display User Details ---------------------------------------------------
def displayDetails(detail):
    print("\n {0:*^60s}\n".format(" YOUR DETAILS "))
    print(f"User Name : {detail['username']}  \t\tAccount Number : {detail['Account Number']}\n")
    print(f"Balance   : {detail['balance']}    \t\tMobile Number : {detail['mobile number']}\n")
    print("\n {0:*^60s}".format(""))

# ------------------- Normal User Service  ------------------------------
def displayOption(data, bankname, atmname):
    print("\n[1] Withdraw \t[2] Deposite \t[3] Display \t[4] <--- BACK\n")
    choice = input("\nChoose option : ")
    if(choice.isnumeric()):
        choice = int(choice)    
        if(choice == 1):
            withdraw(data, bankname, atmname)
            displayOption(data, bankname, atmname)
        elif(choice == 2):
            deposite(data, bankname, atmname)
            displayOption( data, bankname, atmname)
        elif(choice == 3):
            displayDetails(data)
            displayOption(data, bankname, atmname)
        elif(choice == 4):
            print("\n {0:*^50s}  \n ".format(" Thank You  "))
        else:
            print("\nWrong choice \n")
    else:
        print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))

# ------------------- Withdraw  ------------------------------
def withdraw(data, bankname, atmname):
    global  day_limit_transaction, one_time_transaction
    # bank_name = bank_list()
    withdraw_amount = input("\nEnter Withdraw Amount : ")
    if(withdraw_amount.isnumeric()):
        withdraw_amount = int(withdraw_amount)    
        bankNameOfAtm = ''
        for bname in atm_dict:
            for atm_Name in atm_dict[bname]:
                 if(atm_Name == atmname):
                      bankNameOfAtm = bname
        atm = atm_dict[bankNameOfAtm][atmname]
        # print('bank Name Of atm : ', bankNameOfAtm)        
        user_amount = data['balance']
        atm_amount = atm['total_atm_amount']
        if((data['total_withdraw'] + withdraw_amount) <= day_limit_transaction ):
            if(withdraw_amount <= one_time_transaction):
                if(data['limit'] < one_day_limit):
                    if(withdraw_amount%100 == 0 ):
                        if(withdraw_amount <= atm_amount):
                            if(withdraw_amount <= user_amount):
                                if bankname ==  bankNameOfAtm:
                                    total_amount = user_amount - withdraw_amount
                                    atm_amount = atm_amount - withdraw_amount
                                    data['balance'] = total_amount
                                    atm['total_atm_amount'] = atm_amount
                                    data['total_withdraw'] += withdraw_amount
                                    data['limit'] += 1 
                                    print("\n {0:*^50s}  \n ".format(" Successfully Withdraw Amount "))
                                    print("\n {0:*^50s}  \n ".format(' Your Available Amount : ' + str(data['balance'])+' '))

                                else:
                                    print('If you will user other bank AtM card then 5 % cut from Your Amount ') 
                                    updated_withdraw_amount = withdraw_amount*0.05
                                    cut_five_per = updated_withdraw_amount + withdraw_amount
                                    if(cut_five_per <= user_amount):
                                        data['balance'] =   user_amount - cut_five_per
                                        atm['total_atm_amount'] -=  withdraw_amount
                                        data['total_withdraw'] += withdraw_amount
                                        data['limit'] += 1 
                                        print("\n {0:*^50s}  \n ".format(" Successfully Withdraw Amount "))
                                    else:
                                        print("\n {0:*^100s}  \n ".format(" You can't withdraw Amount because " + str(cut_five_per) + ' After cut 5 % Amount '))  
                                    print("\n {0:*^50s}  \n ".format(' Your Available Amount : ' + str(data['balance'])+' '))
                            else:
                                print("\n {0:*^100s}  \n ".format(" You can't withdraw Amount because " + 'Your Available Amount : ' +  str(user_amount)+' '))  

                        else:
                            print("\n {0:*^100s}  \n ".format(" You can't withdraw Amount because " + 'Atm Available Amount : ' +  str(atm_amount)+' '))  
                    else:
                        print("\n {0:*^50s} \n".format(" Multiple of 100  "))       
                else:
                    print(f"\nYour one day limit is over.\n")
            else:
                print("\n {0:*^70s}  \n ".format(" One time 10,000 Amount withdraw from ATM "))             
        else:
            print("\n {0:*^70s}  \n ".format(" One Day only 30,000 rupees withdrawal from ATM "))
    else:
        print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))                  
              
# ---------------------- Deposite --------------------------------------------------------
def deposite(data, bankname, atmname):

    # print('select_bank', bankname, 'select_bank', atmname)
    bankNameOfAtm = ''
    for bname in atm_dict:
        for atm_Name in atm_dict[bname]:
             if(atm_Name == atmname):
                  bankNameOfAtm = bname
    # print("bankNameOfAtm", bankNameOfAtm) 
    atm = atm_dict[bankNameOfAtm][atmname]
    deposite_amount = input("\nEnter Deposite Amount : ")
    if(deposite_amount.isnumeric()):
        deposite_amount = int(deposite_amount)    
        if(deposite_amount%10 == 0 ):
            if(data['bankname'] == bankname):
                data['balance'] += deposite_amount
                print("\n {0:*^50s}  \n ".format(" Successfully Deposit Amount "))
                print("\n {0:*^50s}  \n ".format(' Your Available Amount : ' + str(data['balance'])+' '))
            else:
                print("\n {0:*^50s}  \n ".format('Wrong Choose Bank Name '))
        else:
            print("\n {0:*^50s} \n".format(" Multiple of 10 "))     
    else:
        print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))

# ---------------------------- Administrator Feature ------------------

def moreFeature():
    is_admin_continue = True
    print("\n[1] User \t[2] ATM \t[3] Banks \t[4] Add Money in ATM \t[5] <--- BACK")
    choice = input("\nChoose option : ")
    if(choice.isnumeric()):
        choice = int(choice)
        if(choice == 1):
            print("\n[1] Insert User \t[2] Delete User \t[3] Update User \t[4] Show User Details \t[5] <--- BACK")
            user_choice = input("\nChoose option : ")
            if(user_choice.isnumeric()):
                user_choice = int(user_choice)
                if(user_choice == 1):
                    insertUser()
                elif(user_choice == 2):
                    deleteUser()
                elif(user_choice == 3):
                    updateUser()
                elif(user_choice == 4):
                     show_users_details()
                elif(user_choice == 5):
                    print("\n {0:*^50s}  \n ".format(" Thank You  "))        
                else:
                    print('\nWrong choice\n')
            else:
                print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))        
        elif(choice == 2):
            # deposite(data)
            # displayOption(data)
            print("\n[1] Insert ATM \t[2] Delete ATM \t[3] Update ATM \t[4] Show  ATM Details \t[5] <--- BACK")
            user_choice = input("\nChoose option : ")
            if(user_choice.isnumeric()):
                user_choice = int(user_choice)
                if(user_choice == 1):
                    insertAtm()
                elif(user_choice == 2):
                    deleteAtm()
                elif(user_choice == 3):
                    updateAtm()
                elif(user_choice == 4):
                   show_atm_details()
                elif(user_choice == 5):
                    print("\n {0:*^50s}  \n ".format(" Thank You  "))              
                else:
                    print('\nWrong choice\n')
            else:
                print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))        
            
        elif(choice == 3):
            print("\n[1] Insert Bank \t[2] Delete Bank \t[3] Update Bank \t[4] Show Users Bank Details \t[5] <--- BACK")
            user_choice = input("\nChoose option : ")
            if(user_choice.isnumeric()):
                user_choice = int(user_choice)    
                if(user_choice == 1):
                    insertBank()
                elif(user_choice == 2):
                    deleteBank()
                elif(user_choice == 3):
                    updateBank()
                elif(user_choice == 4):
                    show_users_details()
                elif(user_choice == 5):
                   print("\n {0:*^50s}  \n ".format(" Thank You  "))   
                   # is_admin_continue = False
                   # return is_admin_continue  
                else:
                    print('\nWrong choice\n')
            else:
                print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))        
        elif(choice == 4):
            insert_money_atm()
        elif(choice == 5):
            print("\n {0:*^50s}  \n ".format(" Thank You  "))
            is_admin_continue = False
            return is_admin_continue
                 
        else:
            print("\nWrong choice\n")
        return is_admin_continue    
    else:
        print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))   
        return is_admin_continue 

# ------------------- Insert Users by Administrator   ------------------------------
def insertUser():
    bank_name = bank_list()
    is_invalid = True
    if(bank_name != is_invalid):
        # print(userDetails)
        user_dict = {}
        user_name = input("\nEnter User Name : ")
        user_pin = random.randint(10,99)
        user_card_number = random.randint(1000,9999)
        # balance = int(input("\nEnter balance : "))
        mobile_number = input("\nEnter Mobile Number : ")
        Account_number =input("\nEnter Account Number : ")
        if(mobile_number.isnumeric() and Account_number.isnumeric()):
            if(len(mobile_number) == 10):
                user_dict = {"username":user_name,"userpin":user_pin,"balance": 0,"bankname":bank_name,"mobile number":int(mobile_number),"Account Number":int(Account_number),  'total_withdraw' : 0, 'limit' : 0, 'bankname': bank_name, 'isNewPin': True}
                user_details[bank_name][user_card_number] = user_dict
                print("\n {0:*^50s}  \n ".format(" Successfully User Details Inserted "))
            else:
                print("\n {0:*^50s}  \n ".format(" Mobile Number 10 digit Only  "))
                    
        else:    

           print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))

# -------------------  Users Deletes by Administrator   ------------------------------


def deleteUser():
    is_invalid  = True
    bank_name = bank_list()
    if(bank_name != is_invalid): 
        card_number = input("\nEnter card Number : ")
        if(card_number.isnumeric()):
            card_number  = int(card_number)
            if(card_number in user_details[bank_name]):
                if(user_details[bank_name][card_number]['balance'] == 0):
                  del user_details[bank_name][card_number]
                  print("\n {0:*^50s}  \n ".format(" Successfully User Details Deleted "))
                else:
                    print("\nYou can't Delete " + user_details[bank_name][card_number]['username'] +"'s Details because Available balance is "+ str(user_details[bank_name][card_number]['balance'] ))
                    print()   

            else:  
                print("\n {0:*^50s}  \n ".format(" Invalid Card Number "))
        else:
            print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))        

        # print(user_details)

# -------------------  Users Update by Administrator   ------------------------------

    
def updateUser():
    is_invalid = True
    bank_name = bank_list()
    if(bank_name != is_invalid):
        user_dict = {}
        user_card_number = input("\nEnter Card Number : ")
        if(user_card_number.isnumeric()):
            user_card_number = int(user_card_number)
            #print(userDetails[bank_name][user_card_number])
            if user_card_number in user_details[bank_name]:
                user_name = input("\nEnter User Name : ")
                # user_pin = input("\nEnter pin number ")
                mobile_number =  input("\nEnter Mobile Number : ")
                if(mobile_number.isnumeric() and len(mobile_number) == 10 ):
                    user_details[bank_name][user_card_number]['username'] = user_name
                    # user_details[bank_name][user_card_number]['userpin'] = user_pin
                    user_details[bank_name][user_card_number]['mobile number'] = int(mobile_number)
                    print("\n {0:*^50s}  \n ".format(" Successfully Update User Details "))
                else:
                    print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))
            else:
                print("\n {0:*^50s}  \n ".format(" Invalid Card Number "))
        else:
            print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))


# -------------------  NEW ATM LSIT ADD  by Administrator   ------------------------------


def insertAtm():
    is_invalid = True
    bank_name = bank_list()

    if(bank_name != is_invalid):
        which_atm = input("\nEnter NEW ATM Name : ")
        if(which_atm  not in atm_dict[bank_name]):

            location = input("\nEnter Location of ATM : ")
            atm_amount = input("\nEnter ATM Amount : ")
            if(atm_amount.isnumeric()):
                # {"total_atm_amount" : 40000,"Location" : "rajkot"},
                if(int(atm_amount)%100 == 0 ):
                    atm_details = {"total_atm_amount": int(atm_amount), 'Location': location}
                    atm_dict[bank_name][which_atm] = atm_details
                    print("\n {0:*^50s}  \n ".format(" Successfully Insert ATM Details "))
                    # print("atm_dict ---> ", atm_dict)
                else:
                    print("\n {0:*^50s} \n".format(" Multiple of 100  "))            
            else:
                print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))
        else:
                    
            print("\n {0:*^50s}  \n ".format(" Yon can't Insert ATM because it is already exist  "))

              

# -------------------  Delete exist ATM by Administrator   ------------------------------

def deleteAtm():
    is_invalid = True
    atmname = atm_list('temp')
    if(atmname != is_invalid):
        # atm_name =  atm_list(bank_name)
        bankNameOfAtm = ''
        for bname in atm_dict:
            for atm_Name in atm_dict[bname]:
                 if(atm_Name == atmname):
                      bankNameOfAtm = bname
        # print("bankNameOfAtm", bankNameOfAtm) 
        atm = atm_dict[bankNameOfAtm][atmname]
        if(atm_dict[bankNameOfAtm][atmname]['total_atm_amount'] == 0):
               del atm_dict[bankNameOfAtm][atmname]
               print("\n {0:*^50s}  \n ".format(" Successfully Deleted ATM Details "))   
        else:        
    
               print("\nYou can't Delete " + atmname +" because Available balance is "+ str(atm_dict[bankNameOfAtm][atmname]['total_atm_amount']))
        
# -------------------  Update exist ATM by Administrator   ------------------------------


def updateAtm():
    is_invalid = True
    bank_name = bank_list()
    if(bank_name != is_invalid):
        if(len(atm_dict[bank_name])):
            atm_name = atm_list(bank_name)
            if(atm_name != is_invalid):
            # if(bank_name != is_invalid and atm_name != is_invalid):
                atm_details = atm_dict[bank_name][atm_name]
                atm_details['Location'] = input("\nEnter ATM location : ")
                print("\n {0:*^50s}  \n ".format(" Successfully Updated  ATM Details "))
        else:
            print("\n {0:*^50s}  \n ".format(bank_name +" ATM is not Available  "))            

# -------------------  Insert Money exist ATM by Administrator   ------------------------------


def insert_money_atm():
    is_invalid = True
    bank_name = bank_list()
    if(bank_name != is_invalid):
        atm_name = atm_list(bank_name)
        if(atm_name != is_invalid):
    # if(bank_name != is_invalid and atm_name != is_invalid):
            insertMoneyAtm = input("\nEnter Amount for insert Money into ATM :  ")
            if(insertMoneyAtm.isnumeric()):
                insertMoneyAtm = int(insertMoneyAtm)
                if(insertMoneyAtm %100 == 0):
                    atm_dict[bank_name][atm_name]['total_atm_amount'] +=  insertMoneyAtm
                    # print('Updated amount : ',atm_dict[bank_name][atm_name])
                    print("\n {0:*^50s}  \n ".format(" Successfully Insert Money in  ATM "))
                else:
                    print("\n {0:*^50s} \n".format(" Multiple of 100  "))         
            else:
                print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))
                     

# -------------------  New Bank Insert in Bank dict and ATM dict by Administrator   ------------------------------

def insertBank():

    new_Bank_name = input("\nEnter new Bank Name : ")
    if(new_Bank_name.upper() not in user_details):
        user_details[new_Bank_name.upper()] = {}
        atm_dict[new_Bank_name.upper()] = {}
        print("\n {0:*^50s}  \n ".format(" Successfully Insert Bank Details "))
    else:
        print("\n {0:*^50s}  \n ".format(" You can't insert Bank because Bank already exist "))
            

    # print(user_details)

# -------------------  Delete Bank in BANK Dict and Atm Dict   by Administrator   ------------------------------
def deleteBank():
    is_invalid = True
    bank_name = bank_list()
    if(bank_name != is_invalid):
       # del user_details[bank_name]
       # if(bank_name in atm_dict):
          if(len(user_details[bank_name]) == 0):
            # del atm_dict[bank_name]
            del user_details[bank_name]

            print("\n {0:*^50s}  \n ".format(" Successfully Delete Bank Details "))

          else:
            print("\nYou can't Delete because Users already exist in bank \n" )

# -------------------  Update Bank in BANK Dict and Atm Dict   by Administrator   ------------------------------
def updateBank():
    is_invalid = True
    bank_name = bank_list()
    if(bank_name != is_invalid):
       bank_details =  user_details[bank_name]
       atm_details =  atm_dict[bank_name]
       update_bank_name = input("Enter Update Bank Name : ")
       if(update_bank_name.upper() not in user_details):
           user_details[update_bank_name] = bank_details 
           atm_dict[update_bank_name] = atm_details
           del user_details[bank_name]
           del atm_dict[bank_name]
           print("\n {0:*^50s}  \n ".format(" Successfully Updated Bank Details "))
       else:
           print("\n {0:*^50s}  \n ".format(" You can't update Bank Name  "))

               
           

# -------------------  Create Bank list and user or administrator given choose bank   --------------
def bank_list():
    is_invalid = True
    bankList = [ '' for i in range(len(user_details))]
    index = 0 
    for keys in user_details:
        bankList[index] = keys
        index += 1 
    if(len(user_details)):
        print("\n----- BANK LIST -------\n")
        for i in range(len(bankList)):
            print(f"[{i+1}] {bankList[i]}")
        print("\n-------------------------\n")
        select_bank = input("\nChoose Bank Name : ")
        if(select_bank.isnumeric()):
            select_bank = int(select_bank)
            if(select_bank <= len(bankList)):
                bank_name = bankList[select_bank-1]
                # print('bank Name : ', bank_name)
                return bank_name
            else:
                print("\nPlease Enter valid input as Number \n")   
                # return is_invalid
        else:
             print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))
        return is_invalid
    else:
        print("\n {0:*^100s}  \n ".format(" BANK List isn't Available because Bank List deleted by Administrator. "))
        return is_invalid

# -------------------  Create ATM list and user or administrator given choose which atm   --------------


def atm_list(select_bank):
    is_invalid = True
    if(len(atm_dict.keys()) != 0):
        atmList = []
        index = 0 
        print("\n {0:*^60s}  \n ".format(" ATM LIST "))
        for bankName in atm_dict:
            print("\n {0:-^50s}  \n ".format(bankName))
            for atmName in atm_dict[bankName]:
                print(f"[{index+1}] {atmName}")
                index += 1 
                atmList.append(atmName)
        print("\n {0:*^60s}  \n ".format(''))

        select_atm = input("\nChoose ATM Name : ")
        if(select_atm.isnumeric()):
            select_atm = int(select_atm)
            if(select_atm > 0 and   select_atm <= len(atmList)):
                atm_name = atmList[select_atm-1]
                return atm_name
                   
            else:
                print('\nPlease Enter valid input as Number\n')
                # return is_invalid
        else:
             print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))
        return is_invalid     

# --------------- Show Bank Details -----------------------        

def show_users_details():   
    for bankName in user_details:
        print("\n {0:*^50s}  \n ".format(' '+ bankName +' '))

        for cardNumber in  user_details[bankName]:
            print("Card Number : " + str(cardNumber), end='\t')
            for detail in user_details[bankName][cardNumber]:
                if(detail != 'bankname' and  detail != 'userpin'):
                   print(str(detail) + ' : '+str(user_details[bankName][cardNumber][detail]),end='\t')

            print("\n\n")
        print('\n') 
    # print(user_details)    

# ----------------- Show ATM Details -------------------------------------------           

def show_atm_details():
    for bankName in atm_dict:
        print("\n {0:*^50s}  \n ".format(' '+ bankName +' '))
        for atmName in atm_dict[bankName]:
            print("ATM LIST : " + str(atmName), end='\t')
            for atm_detail in atm_dict[bankName][atmName]:
                print(str(atm_detail) + ' : '+str(atm_dict[bankName][atmName][atm_detail]),end='\t')
            print('\n\n')
        print()    

# -------------- One Day limt of Transaction --------------------------------            
day_limit_transaction = 30000
# -------------- One time limt of Transaction --------------------------------            
one_time_transaction = 10000
one_day_limit = 5
# --------------------- How many Amout withdraw from our Bank  --------------------

isContinue = True
while(isContinue):
    print("\n[1] Users \t[2] Administrator \t[3] Quit")
    users = input("\nChoose Option : ")
    if(users.isnumeric()):
        users = int(users)
        #----------------- Normal user ---------------------------------------
        if(users == 1):
            print("\n {0:*^50s}  \n ".format(" Welcome to AtM  "))
            condition = True
            while condition:
                is_invalid = True
                bank_name = bank_list()
                if(bank_name != is_invalid):
                   atm_name = atm_list(bank_name)
                   if(atm_name != is_invalid):
                       condition = userValidation(bank_name,atm_name)
                   else:
                        condition = False
                else:
                    condition = False

        # ----------------------------- For Administrator ---------------------------------
        elif(users==2):
        # --------------------- Username and password ---------------------------------
            print("UserName : krishna, password: krishna123 ")
            username = input("Enter Username :  ")
            password = input("Enter Password :  ")
            # print("Administrator : ",administrator_details)
            #------------------ Administrator Validation ------------------------------------
            if(username in administrator_details):
                isValidPassword = administrator_details[username]['password']
                if(isValidPassword == password):
                    is_admin_continue = True
                    while(is_admin_continue):
                        is_admin_continue = moreFeature()
                else:
                    print("\n {0:*^50s}  \n ".format(" Invalid Password "))
            else:
                print("\n {0:*^50s}  \n ".format(" Invalid Username "))                 
        elif(users==3):
            isContinue = False     
        else:
            print("\n {0:*^50s}  \n ".format(" Wrong choice "))                           
    else:
        print("\n {0:*^50s}  \n ".format(" Please Enter valid Input  "))
