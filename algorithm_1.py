from datetime import datetime
import math
from decimal import Decimal





'''
##return combined update list
def combineTwoListAndSort(old_list,new_list):
    for item in new_list:
        if item[1] == 0:
            for i in range(len(old_list)):
                if item[0] == old_list[i][0]:
                    old_list.pop(i)
                    break
        else:
            ##如果价格相等，后者数量替代前者
            


            
            for i in range(len(old_list)):
                print(item)
                print(old_list[i])

                price=item[0]
                for item_1 in range(len(old_list)):
                    
                
                if item[0] == old_list[i][0]:
                    old_list[i][1] = item[1]
                    break
                else:
                    old_list.append(item)
                    break
    ###d2进行排序，ask升序,bid降序    
    old_list.sort(key=lambda x:(x[0]),reverse = False)
    return old_list
'''



##return combined update list
def produceSafisfiedList(old_list,new_list):
    for item in new_list:
        price = item[0]
        amount = item[1]
        if amount == 0:
            for i in range(len(old_list)):
                if price == old_list[i][0]:
                    old_list.pop(i)
                    break
                
        if amount != 0:
            flag = True
            for i in range(len(old_list)):
                if price == old_list[i][0]:
                    old_list[i][1] = amount
                    flag = False
                    break
                if price != old_list[i][0]:
                    continue
            ##追加价格与数量均不相等
            if flag:
                old_list.append(item)
            
    ###排序，ask升序,bid降序    
    old_list.sort(key=lambda x:(x[0]),reverse = False)
    return old_list
                
                
[6670.0, 0.8809]
[6669.5, 0.72774121]

[6670.0, 0.8809]
[6670.0, 0.28]

[6670.0, 0.8809]
[6671.5, 0.6679]

[6670.0, 0.8809]
[6674.3, 0.1]

[6670.0, 0.8809]
[6676.0, 0.72085439]     
                    
                         
new_list = [[6670.0, 0.8809], [6671.5, 0.1038],[6674.3, 0],[6675,0.9]]

old_list = [[6669.5, 0.72774121], [6670.0, 0.28], [6671.5, 0.6679], [6674.3, 0.1], [6676.0, 0.72085439]]

##[[6669.5, 0.72774121], [6670.0, 0.28], [6670.0, 0.8809], [6671.5, 0.6679], [6671.5, 0.1038], [6674.3, 0.1], [6676.0, 0.72085439]]
#[[6669.5, 0.72774121], [6670.0, 0.28], [6670.0, 0.8809], [6671.5, 0.6679], [6671.5, 0.1038], [6674.3, 0.1], [6676.0, 0.72085439]]
st_list = produceSafisfiedList(old_list,new_list)

print(st_list)

 

 
 

 
