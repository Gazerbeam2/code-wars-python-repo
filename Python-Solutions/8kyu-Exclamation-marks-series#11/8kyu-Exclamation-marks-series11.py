# Solution

def replace_exclamation(st):
     table = str.maketrans('aeiouAEIOU','!!!!!!!!!!')
     return st.translate(table)
