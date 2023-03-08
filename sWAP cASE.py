def swap_case(s):
    st=""
    for i in s:
        if i.isupper():
            st+=i.lower()
        elif i.islower():
            st+=i.upper()
        else:
            st+=i
    return st
