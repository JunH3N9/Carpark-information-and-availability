filename= 'carpark-information.csv'
file=open(filename,'r') #accessing the file

list2=[]
for line in file:
    list1 = line.strip('\n').split(',')     #split into carpark number, carpark type, parking system and address
    string = ','.join(list1[3:]).strip('"')            #combine address together since some have commas in them
    list1[3:] = [string]
    list2.append(list1)
file.close()    #Closing the file

carpark_list = []
for item in list2[1:]:
    dict1 = {item[0]: [item[1], item[2], item[3]]} #obtaining dictionaries
    carpark_list.append(dict1) #obtaining list of dictionaries
print(carpark_list[782])    

def option1(): #option 1 
    print("Option 1: Display Total Number of Carparks in 'carpark-information.csv'")     #display selected option
    print("Total Number of carparks in 'carpark-information.csv': {:4}.\n".format(len(carpark_list)))
        

def option2(): #option 2
    print("Option 2: Display All Basement Carparks in 'carpark-information.csv'")       #display selected option
    print('{:12}{:23}{:>7}'.format('Carpark No', 'Carpark Type', 'Address'))           #header
    
    i=0
    for element in carpark_list:    
        for carpark, info in element.items():  #accessing the values in the dictionary
            if info[0]  =='BASEMENT CAR PARK':
                print('{:12}{:23}{:>10}'.format(carpark, info[0], info[2]))
                i+=1    #counting number of basement carparks
    print('Total number:', i, '\n')
    

def option3(): #option 3 
    print('Option 3: Read Carpark Availablity Data File') #display selected option
    filename=input('Enter the file name: ')
    file= open(filename, 'r')   #accessing the file

    #declare the temporary lists and dictionary
    list2 = []
    availability_list = []

    for line in file:
        list1 = line.strip('\n').split(',')     #split into carpark number, total lots and lots available
        list2.append(list1)
    file.close()
                
    for item in list2[2:]:
        dict1 = {item[0]: [item[1], item[2]]}   #obtaining dictionary
        availability_list.append(dict1)     #obtaining list of dictionaries    

    print(str(list2[0][0]), '\n')       #timestamp
    return availability_list


def option4(): #option 4
    print('Option 4: Print Total Number of Carparks in the File read in [3]') #display selected option
    print('Total Number of Carparks in the File: {}\n'.format(len(availability_list)))
    

def option5(): #option 5 
    print('Option 5: Display Carparks Without Available Slots') #display selected option
    
    i=0
    for element in availability_list:
        for carpark, lots in element.items():
            if lots[1]  =='0':     #obtaining the carpark with no available slot
                print('Carpark Number: ',carpark)
                i+=1                    #counting number of carparks with no slots
    print('Total Number: ',i, '\n')


def option6(): #option 6
    print('Option 6: Display Carparks With At Least x% Available Lots') #display selected option
    percent = float(input('Enter the percentage required: ')) #percentage input
    
    print('{:12}{:12}{:16}{:15}'.format('Carpark No', 'Total Lots', 'Lots available', 'Percentage')) #header

    i=0
    for element in availability_list:       #going through all the list eleents
        for carpark, lots in element.items():   #obtaining key and value list
            total_lots=int(lots[0])
            available_lots= int(lots[1])
            
            if int(total_lots) > 0:  #If total lot = 0, percent is 0 
                availability_percentage = (available_lots / total_lots) * 100

                if percent == 0 or availability_percentage >= percent:  #if input is >= 0, total lots not 0
                    print('{:12}{:>10}{:>16}{:12.1f}'.format(carpark, total_lots, available_lots, availability_percentage))
                    i += 1
                
            elif percent == 0 and available_lots == 0:  #if input and total lots is 0
                print('{:12}{:>10}{:>16}{:>12}'.format(carpark, total_lots, available_lots, '0.0'))
                i += 1
                
    print('Total number: ',i, '\n')
    

def option7(): 
    print('Option 7: Display Addresses Of Carparks With At Least x% Available Lots') #display selected option
    percent = float(input('Enter the percentage required: ')) #percentage input
    
    print('{:12}{:12}{:16}{:15}{:20}'.format('Carpark No', 'Total Lots', 'Lots available', 'Percentage', 'Address')) #header

    i=0
    for element in availability_list:       #going through all the list elements 
        for carpark, lots in element.items(): #obtaining key and value list
            total_lots=int(lots[0])
            available_lots= int(lots[1])
            
            for dictionary in carpark_list:     
                for carpark_name, details in dictionary.items():    
                    if carpark_name == carpark: 
                        address=details[2]      #obtain address of carpark
                        
                        if int(total_lots) > 0:
                            availability_percentage = (available_lots / total_lots) * 100
                            
                            if percent == 0 or availability_percentage >= percent:  #if input is >= 0, total lots not 0
                                print('{:12}{:>10}{:>16}{:>12.1f}{:5}{:<40}' \
                                      .format(carpark, total_lots, available_lots, availability_percentage, '', address))
                                i += 1
                                
                        elif percent == 0 and available_lots == 0:  #if input and total lots is 0
                            print('{:12}{:>10}{:>16}{:>12}{:5}{:<40}' \
                                  .format(carpark, total_lots, available_lots, '0.0', '', address))
                            i += 1
                                
    print('Total number: ',i, '\n')
    
def option8():
    i=0
    list1=[]
    location=input('Enter a location: ').upper()
    location=location.upper()   #Carpark address locations are in capitals
    print('{:12}{:12}{:16}{:15}{:20}'.format('Carpark No', 'Total Lots', 'Lots available', 'Percentage', 'Address')) #header
    
    for element in carpark_list:
        for carpark, details in element.items():
            if location in details[2]:
                address=details[2]  #obtaining address
                
                for element in availability_list:
                    for key, lots in element.items():
                        total_lots=lots[0]
                        lots_available=lots[1]
                        if total_lots == 0 or int(lots[1]) == 0:  #if total or available lots is 0, percentage is 0   
                            percentage = 0.0
                        else:
                            percentage=int(lots[1])/int(lots[0])*100    #obtain percentage
                                
                        if key == carpark:  #obtaining carpark number
                            list1.append(key)   #list of carparks added already                          
                            print('{:12}{:>10}{:>16}{:>12.1f}{:5}{:<40}'\
                                .format(key, total_lots, lots_available, percentage,'', address)) 
                            i+=1
                                
                if carpark not in list1:    #if carpark does not have data on total and available lots
                    print('{:12}{:>10}{:>16}{:>12}{:5}{:<40}'\
                        .format(carpark, '-', '-', '-','', address))
                    i+=1                            
    if i != 0:
        print('Total number: ',i, '\n')
    else:
        print('No carpark found\n')
        

def option9():
    lot_list=[]
    list1=[]
    most_lot=0
  
    for element in availability_list:
        for carpark, lots in element.items(): 
            total_lot=int(lots[0])                 
            if total_lot > most_lot:  #Check if total lot is more than current number of lots
                most_lot=total_lot
                carpark_num=carpark
                lot_available=int(lots[1])
                percentage= (lot_available/total_lot)*100
                
    for element in carpark_list:
        for carpark, details in element.items():
            if carpark_num == carpark:      #obtain address of carpark
                address=details[2]
    
    
    print('{:12}{:12}{:16}{:15}{:20}'.format('Carpark No', 'Total Lots', 'Lots available', 'Percentage', 'Address')) #header
    print('{:12}{:>10}{:>16}{:>12.1f}{:5}{:<40}\n'\
                                      .format(carpark_num, most_lot, lot_available, percentage,'', address))


def option10():  
    filename= 'carpark-availability-with-addresses.csv'
    file=open(filename, 'w')    #create csv file
    
    #add items not in dictionary
    file.write('Timestamp: 2023-06-19T11:10:27+08:00\n')    
    file.write('Carpark Number, Total Lots, Lots Available, Address\n')

    list1=[]
    list2=[]
    for element in availability_list:       #going through all the list elements 
        for carpark, lots in element.items(): #obtaining key and value list
            total_lots=lots[0]
            lots_available=lots[1]
            
            for dictionary in carpark_list:     
                for carpark_name, details in dictionary.items():    
                    if carpark_name == carpark:
                        address=details[2]
                        list1.append([carpark, total_lots, lots_available, address])
                        list2.append(carpark)   #list of carparks added already   
                        
            if carpark not in list2:    #adding carparks that do not have address
                list1.append([carpark, total_lots, lots_available, '-'])

                        
    list1=sorted(list1, key=lambda details: int(details[2]))    #sort list in order of available lots

    i=0
    for x in list1:
        data = f"{x[0]},{x[1]},{x[2]},{x[3]}\n"
        file.write(data)
        i+=1

    print(i+2, 'lines added to', "'carpark-availability-with-addresses.csv'\n")
    

option_list=[]
#Main menu
while True:
    print("MENU\n\
====\n\
[1] Display Total Number of Carparks in 'carpark-information.csv'\n\
[2] Display All Basement Carparks in 'carpark-information.csv'\n\
[3] Read Carpark Availability Data File\n\
[4] Print Total Number of Carparks in the File read in [3]\n\
[5] Display Carparks Without Available Slots\n\
[6] Display Carparks With At Least x% Available Lots\n\
[7] Display Addresses Of Carparks With At Least x% Available Lots\n\
[8] Display All Carparks at a Given Location\n\
[9] Display Carparkwith the Most Parking Lots\n\
[10] Create an output file with Carpark Availability and Address, sorted by Lots Available \n\
[0] Exit\n")
    
    option=input('Enter your option: ') #user input
    option_list.append(option)

    if option == '1': #option 1 
        option1()

    elif option == '2': #option 2
        option2()
            
    elif option == '3': #option 3
        availability_list=option3()
        
    elif option == '4': #option 4
        if option_list.count('3')!=0: #check that option 3 was done
            option4()
        else:
            print('User can only perform this option after option 3 is done. \n')

    elif option == '5': #option 5
        if option_list.count('3')!=0: #check that option 3 was done
            option5()

        else:
            print('User can only perform this option after option 3 is done. \n')

    elif option == '6': #option 6
        if option_list.count('3')!=0: #check that option 3 was done
            option6()
        else:
            print('User can only perform this option after option 3 is done. \n')
        
    elif option == '7': #option 7
        if option_list.count('3')!=0: #check that option 3 was done
            option7()
        else:
            print('User can only perform this option after option 3 is done. \n')

    elif option == '8': #option 8
        if option_list.count('3')!=0: #check that option 3 was done
            option8()
        else:
            print('User can only perform this option after option 3 is done. \n')

    elif option == '9': #option9
        if option_list.count('3')!=0: #check that option 3 was done
            option9()
        else:
            print('User can only perform this option after option 3 is done. \n')

    elif option == '10': #option10
        if option_list.count('3')!=0: #check that option 3 was done
            option10()
        else:
            print('User can only perform this option after option 3 is done. \n')

    elif option == '0':
        break

    else:
        print('Invalid option \n')
