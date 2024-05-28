

def linear_search(list_of_item,key):
    is_found = False
    for i in list_of_item:
        if i == key :
            is_found =True
    
    return is_found
  

list_of_item =["dev","stg","prd"]

key = "mon"

found = linear_search(list_of_item,key)

print(found)

