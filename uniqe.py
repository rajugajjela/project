def get_uniq(list):
    uniq_list = []
    for x in list:
        x=x.lower()
        if x not in uniq_list:
            uniq_list.append(x)
    return uniq_list
list =['One','one','oNe','Two','TWO','ToW','Three','THREE','Four','FOUR']
print(get_uniq(list))
