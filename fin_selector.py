fin_config_check = ['thruster', 'quad', '5-fin', 'quad rear']
fin_config = None #thrusters, quads, 5-fins
weight = None
ride_num = None #customers ride number
x_small_thrusters = ['HS3 Generation Series', 'F2 Honeycomb', 'John Grom Honeycomb'] #fill with all Thrusters in x-small category
x_small_quads = []
x_small_5fins = []
small_thrusters = ['F4 Blackstix', 'F4 Alpha', 'AM3 Honeycomb', 'F4 Honeycomb', 'Jordy Small Honeycomb', 'John John Small Techflex', 'F4 Control Series'] #fill with all thrusters is small category
small_quads = ['F4 Honeycomb']
small_5fins = ['F4 Alpha', 'F4 Generation',]
small_qrs = ['QD2 3.75 Blackstix', 'QD2 3.75 Alpha', 'QD2 3.75 Honeycomb']
medium_thrusters = ['AM1 Blackstix', 'Machado Blackstix', 'R1 Blackstix', 'EA Blackstix', 'HS2 Generation Series', 'Lost Medium Generation Series', 'John John Medium Alpha',
                    'F6 Alpha', 'AM1 Honeycomb', 'WCT Honeycomb', 'F6 Honeycomb', 'Firewire Medium Honeycomb', 'Jordy Medium Honeycomb',
                    'AM1 Techflex', 'John John Medium Techflex', 'AM1 Control Series', 'Pyzel Medium Control Series', 'EA Control Series' ] #fill with all thrusters in the medium category
medium_quads = ['F6 Honeycomb', 'EA Hawaii Control Series', 'Rasta Quad Honeycomb/Bamboo']
medium_5fins = ['Roberts Generation Series', 'Stamps Generation Series', 'F6 Generation Series', 'F6 Alpha', 'F6 Honeycomb']
medium_qrs = ['QD2 4.0 Blackstix', 'QD2 4.0 Alpha', 'QD2 4.0 Honeycomb']
large_thrusters = ['Ando Blackstix', 'F8 Blackstix', 'Roberts Large Generation Series', 'Freestone Generation Series', 'HS1 Generation Series', 'F8 Alpha', 'AM2 Honeycomb',
                   'F8 Honeycomb', 'Firewire Large Honeycomb', 'Jordy Large Honeycomb', 'AM2 Techflex', 'John John Large Techflex', 'Freestone Control Series',
                   'Pyzel Large Control Series', 'Pancho Large Control Series' ] #fill with all thrusters in the large category
large_quads = ['Controller Alpha', 'Controller Honeycomb/Bamboo', 'F8 Honeycomb']
large_5fins = ['F8 Alpha', 'F8 Honeycomb', 'Firewire Large Honeycomb', 'Lost Large Honeycomb', 'AM2 Techflex', 'Twiggy Control Series']
large_qrs = ['QD2 4.15 Blackstix', 'HS QR Generation Series', 'QD2 4.15 Honeycomb']
fin_selection = [] #the running list filled with selections given in each category
fin_dict = dict() #the dictionary that runs the .get count
ride_dict = {'HS3 Generation Series' : 8.5, 'F2 Honeycomb': 4.6, 'John Grom Honeycomb' : 6.1, 'F4 Blackstix' : 9.6, 'F4 Alpha' : 5.5,
             'AM3 Honeycomb' : 4.7, 'F4 Honeycomb' : 4.6, 'Jordy Small Honeycomb' : 5.0, 'John John Small Techflex' : 4.0, 'F4 Control Series' : 1.5,
             'F4 Generation' : 7.0, 'QD2 3.75 Blackstix' : 8.1, 'QD2 3.75 Alpha' : 6.5, 'QD2 3.75 Honeycomb' : 4.6, 'AM1 Blackstix' : 9.8, 'Machado Blackstix' : 9.7,
             'R1 Blackstix' : 9.5, 'EA Blackstix' : 9.8, 'HS2 Generation Series' : 8.3, 'Lost Medium Generation Series' : 7.3, 'John John Medium Alpha' : 5.5,
             'F6 Alpha' : 5.5, 'AM1 Honeycomb' : 6.1, 'WCT Honeycomb' : 5.1, 'F6 Honeycomb' : 5.3, 'Firewire Medium Honeycomb' : 4.0, 'Jordy Medium Honeycomb' : 5.0,
             'AM1 Techflex' : 4.0, 'John John Medium Techflex' : 4.0, 'AM1 Control Series' : 3.0, 'Pyzel Medium Control Series' : 3.0, 'EA Control Series' : 2.2,
             'EA Hawaii Control Series' : 3.0, 'Rasta Quad Honeycomb/Bamboo' : 8.5, 'Roberts Generation Series' : 8.2, 'Stamps Generation Series' : 7.4, 'F6 Generation Series' : 7.2,
             'QD2 4.0 Blackstix' : 8.2, 'QD2 4.0 Alpha' : 6.5, 'QD2 4.0 Honeycomb' : 5.3, 'Ando Blackstix' : 9.8, 'F8 Blackstix' : 9.4, 'Roberts Large Generation Series' : 7.9,
             'Freestone Generation Series' : 8.0, 'HS1 Generation Series' : 8.4, 'F8 Alpha' : 6.5, 'AM2 Honeycomb' : 4.6, 'F8 Honeycomb' : 5.2, 'Firewire Large Honeycomb' : 4.0,
             'Jordy Large Honeycomb' : 5.1, 'AM2 Techflex' : 4.0, 'John John Large Techflex' : 4.0, 'Freestone Control Series' : 3.0, 'Pyzel Large Control Series' : 3.0,
             'Pancho Large Control Series' : 1.0, 'Lost Large Honeycomb' : 6.7, 'Twiggy Control Series' : 3.0, 'Controller Alpha' : 5.7, 'Controller Honeycomb/Bamboo' : 6.9,
             'QD2 4.15 Blackstix' : 8.1, 'HS QR Generation Series' : 7.2, 'QD2 4.15 Honeycomb' : 5.2 }

# figure out what setup the person is using
while True:
    fin_fun = input("what kind of setup are you on?(thruster/quad/5-fin/Quad Rear) or for more information type 'help'. To exit type 'exit'")
    if fin_fun.lower() in fin_config_check:
        fin_config = fin_fun.lower()
        break
    if fin_fun.lower() == 'help':
        print('A thruster set means that your board is setup for 3 fins, a quad is 4 and a 5-fin is (you guessed it) 5.  If you do have a 5-fin setup you can choose any of the above choices ')
        continue
    if fin_fun.lower() == 'exit':
        exit()
    else:
        print("please choose from the list.  ")
print(fin_config)

while True:
    weight_test = input("How much do you weigh?")
    try:
        weight = int(weight_test)
    except:
        print('please put in a number only')
        continue
    break

if weight <= 115:
    if fin_config.lower() == 'thruster':
        for stuff in x_small_thrusters:
            fin_selection.append(stuff)

    if fin_config.lower() == 'quad':
        for stuff in x_small_quads:
            fin_selection.append(stuff)

    if fin_config.lower() == '5-fin':
        for stuff in x_small_5fins:
            fin_selection.append(stuff)

    if fin_config.lower() == 'quad rear':
        for stuff in x_small_qrs:
            fin_selection.append(stuff)


if weight >= 105 and weight <= 155:
    if fin_config.lower() == 'thruster':
        for stuff in small_thrusters:
            fin_selection.append(stuff)

    if fin_config.lower() == 'quad':
        for stuff in small_quads:
            fin_selection.append(stuff)

    if fin_config.lower() == '5-fin':
        for stuff in small_5fins:
            fin_selection.append(stuff)

    if fin_config.lower() == 'quad rear':
        for stuff in small_qrs:
            fin_selection.append(stuff)


if weight >= 145 and weight <= 195:
    if fin_config.lower() == 'thruster':
        for stuff in medium_thrusters:
            fin_selection.append(stuff)

    if fin_config.lower() == 'quad':
        for stuff in medium_quads:
            fin_selection.append(stuff)

    if fin_config.lower() == '5-fin':
        for stuff in medium_5fins:
            fin_selection.append(stuff)

    if fin_config.lower() == 'quad rear':
        for stuff in medium_qrs:
            fin_selection.append(stuff)

if weight >= 180:
    if fin_config.lower() == 'thruster':
        for stuff in large_thrusters:
            fin_selection.append(stuff)

    if fin_config.lower() == 'quad':
        for stuff in large_quads:
            fin_selection.append(stuff)

    if fin_config.lower() == '5-fin':
        for stuff in large_5fins:
            fin_selection.append(stuff)

    if fin_config.lower() == 'quad rear':
        for stuff in large_qrs:
            fin_selection.append(stuff)

while True:
    ride_check = input("Do you happen to know your Ride Number?(y/n)_")
    num_fun = ride_check.lower()
    if not(num_fun == 'y' or num_fun == 'n'):
        print("please answer 'y' or 'n'")
        continue
    elif ride_check.lower() == 'y':
        ride_num_try = input("what is it? (1-10)_")
        try:
            ride_num_int = float(ride_num_try)
        except:
            print("Please enter a number only")
            continue
        if ride_num_int < 1 or ride_num_int > 10:
            print("Please choose a number between 1 and 10")
            continue
        else:
            ride_num = round(ride_num_int,0)
            break
    else:
        break
ride_no_list = []
if ride_num:
    for stuff in fin_selection:
        for key, values in ride_dict.items():
            if stuff == key:
                if values > (ride_num - 1) and values < (ride_num + 1):
                    ride_no_list.append(key)
            else:
                continue

if not ride_num:
    print("No worries!")
    while True:
        new_ride_no = input("If these fins are primarily going to be used in crummy surf enter '1'. If these fins are primarily going to be in big surf enter '2'. If you want something that is a little of both enter '3'__")
        try:
            new_ride_no = int(new_ride_no)
        except:
            print("Please choose an actual number")
            continue
        if new_ride_no < 1 or new_ride_no > 3:
            print("only 1-3 please")
            continue

        elif new_ride_no == 1:
            for stuff in fin_selection:
                for key, values in ride_dict.items():
                    if stuff == key:
                        if values >= 7.0 and values <= 10.0:
                            ride_no_list.append(key)
                        else:
                            continue

        elif new_ride_no == 3:
            for stuff in fin_selection:
                for key, values in ride_dict.items():
                    if stuff == key:
                        if values >= 4.0 and values <= 7.0:
                            ride_no_list.append(key)
                        else:
                            continue

        elif new_ride_no == 2:
            for stuff in fin_selection:
                for key, values in ride_dict.items():
                    if stuff == key:
                        if values >= 1.0 and values <= 4.0:
                            ride_no_list.append(key)
                        else:
                            continue
        break
fun = []
for stuff in ride_no_list:
    for key, value in ride_dict.items():
        if stuff == key:
            fun.append((value,key))
fun.sort()
for value,key in fun:
    print(key,fin_config,"--Ride number",value)
if len(fun) < 1:
    print("sorry, looks like nothing matches your parameters.  Check our website for more details or try again")
