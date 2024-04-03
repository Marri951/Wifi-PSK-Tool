import subprocess

file_a = open('network_names_list.txt', 'a')
file_b = open('network_names_list.txt', 'r')
file_c = open('Final.txt', 'a')

networks = str(subprocess.check_output('netsh wlan show profiles'))
LineOfNetworks = networks.split('Profile')
Number = range(len(LineOfNetworks))
w = 2

for i in Number:
    try:
        Lines = str(LineOfNetworks[w].split(':'))
        Line = Lines.split(str('\\'))
        w = w + 1
        NetworkIndex = Line[0]
        file_a.write('\n' + str(NetworkIndex[12:]))
    except IndexError:
        print('part 1 complete')

file_a.close()

Starting_Network_Names = str(file_b.read())
Final_Network_Names = Starting_Network_Names.split('\n')
FN = Final_Network_Names[1:]

L = 0

for i in FN:
    try:
        Name = FN[L]
        profile = str(subprocess.check_output('netsh wlan show profile name="' + Name + '" key=clear'))
        temp = profile.split(str('\\r\\n'))

        if len(str(temp)) < 100:
                print(len(str(temp)))
                print('to short')
        else:
                name = temp[10]
                SSID = temp[20]
                PSWRD = temp[32]
                file_c.write('\n -------------------------------------------- \n' + name + '\n' + SSID + '\n' + PSWRD)
                L = L + 1
    except subprocess.CalledProcessError:
        print('error')
        L = L + 1

file_c.close()
