import itertools

def find_anagrams(l):
    final=[]
    bool_var=True
    while bool_var:
        s=l[0]
        nums = list(s)
    
        permutations = list(itertools.permutations(nums))
        innerl=[''.join(permutation) for permutation in permutations]
    
        templ=[]
    
        for temp in innerl:
            if temp in l:
                templ.append(temp)
                l.remove(temp)
        final.append(templ)
        
        if len(l)==0:
            bool_var=False
    return final
if __name__=="__main__":
    print("Your Input must be in this format- dog god odg cat tac cta")
    l=list(map(str,input().split(' ')))
    
    print(find_anagrams(l))    