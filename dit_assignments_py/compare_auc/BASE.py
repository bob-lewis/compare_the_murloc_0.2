__author__ = 'Bob Lewis'
#compare the murloc , main module
##'''{"auc":1879400563,"item":82800,"owner":"Angeliza","ownerRealm":"Darksorrow",
# "bid":28500000,"buyout":30000000,"quantity":1,"timeLeft":"LONG","rand":0,
# "seed":979244928,"context":0,"modifiers":[{"type":3,"value":1237},{
# "type":4,"value":50331656},{"type":5,"value":1}],"petSpeciesId":1237,"petBreedId":8,"petLevel":1,"petQualityId":3},

import  Petlist
from Infograb import realmget
server1='darksorrow'
server2='killrog'
count=0
REALM_1='http://eu.battle.net/auction-data/202821d1c5cd21159ede2548cc838c23/auctions.json'
REALM_2='http://eu.battle.net/auction-data/ecee6e0f05b6c1c05d9e1c1822a5c11b/auctions.json'
#REALM_1= str('http://eu.battle.net/api/wow/auction/data/'+server1)
#REALM_2= str('http://eu.battle.net/api/wow/auction/data/'+server2)
r1_hi={}
r1_lo={}
r2_hi={}
r2_lo={}
def main():
    create_pet_auction_lists(realmget(REALM_1))
    create_pet_auction_lists(realmget(REALM_2))


    pass

def create_pet_auction_lists(realm):

    working_list=[]
    if len(r1_hi)==0:
        hi=r1_hi
        lo=r1_lo
    else:
        hi=r2_hi
        lo=r2_lo
    for line in realm:
        working_list_temp_line=[]
        if line[1]=='item:82800':
            #print ('found')
            working_list_temp_line.append(line[2])
            working_list_temp_line.append(line[3])
            working_list_temp_line.append(line[5])
            working_list_temp_line.append(line[17])
            working_list_temp_line.append(line[18])
           #print('!!')
            working_list.append(working_list_temp_line)
    for line in working_list:
        print(line,'\n')





#'''{"auc":1879400563,"item":82800,"owner":"Angeliza","ownerRealm":"Darksorrow",
# "bid":28500000,"buyout":30000000,"quantity":1,"timeLeft":"LONG","rand":0,
# "seed":979244928,"context":0,"modifiers":[{"type":3,"value":1237},{
# "type":4,"value":50331656},{"type":5,"value":1}],"petSpeciesId":1237,"petBreedId":8,"petLevel":1,"petQualityId":3},

main()