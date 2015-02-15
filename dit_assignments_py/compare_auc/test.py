__author__ = 'Bob'
import httplib2
import json
from Infograb import realmget
from  Petlist import getpet
second_round=False
r1_hi={}
r1_lo={}
r2_hi={}
r2_lo={}


valid_realms=['kilrogg','darksorrow','mazrigos','frostwhisper']

def page_get(server):
    print(str('http://eu.battle.net/api/wow/auction/data/'+server))
    request= str('http://eu.battle.net/api/wow/auction/data/'+server)
    h = httplib2.Http(".cache")
    content_headers, content = h.request(request)
    content = content.decode()
    obj = json.loads(content)
    for key,value in obj.items():
        x = (value[0])
        return (x['url'])
def get_server():
    if second_round == True:
        order='second'
    else:
        order='first'
    message='Enter '+order+' server name :kilrogg,darksorrow,mazrigos,frostwhisper\n>>'
    server=str(input(str(message)))
    if server in valid_realms:
        return(page_get(server))
    else:
        server='kilrogg'
        print('Not a valid server, using default, kilrogg..\n.....\n..........')
        return(page_get(server))


def main():
    global second_round
    server1=get_server()
    print ('Accessing\n',server1)
    create_pet_auction_lists(realmget(server1))
    second_round=True
    server2=get_server()
    print ('Accessing\n',server2)
    create_pet_auction_lists(realmget(server2))



def create_pet_auction_lists(realm):
    if second_round==False:
        hi=r1_hi
        lo=r1_lo
    else:
        hi=r2_hi
        lo=r2_lo

    working_list=[]
    for line in realm:
        working_list_temp_line=[]
        if line[1]=='item:82800':
            working_list_temp_line.append(line[2])
            working_list_temp_line.append(line[3])
            working_list_temp_line.append(line[5])
            working_list_temp_line.append(getpet(line[17]))
            working_list_temp_line.append(line[18])
            working_list.append(working_list_temp_line)
    for line in working_list:
        print(line,'\n')

main()