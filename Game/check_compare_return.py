#module to compare user value and randomly generated value
#b is the computer generated pattern
#a is the user given pattern


def check_compare(user_patt,rand_patt):
    ret_show=[]
    for i in range(0,4):
        if(user_patt[i] in rand_patt):
            if(user_patt[i]==rand_patt[i]):
                ret_show.append('r')
            else:
                ret_show.append('s')
        else:
            ret_show.append('_')
    return ret_show

