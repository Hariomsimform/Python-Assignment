def solution(n):
    stack=[]
    result=[]
    def gen_paranthesis(openP,closeP):
   
        if openP==n and closeP==n:
            result.append("".join(stack))
            return
        if openP<n :
            
            stack.append('{')
            gen_paranthesis(openP+1,closeP)
            stack.pop()
        if openP>closeP:
            
            stack.append('}')
            gen_paranthesis(openP,closeP+1)
            stack.pop()
    gen_paranthesis(0,0)    
    return result
 

if __name__=='__main__':
    n=int(input())
    
    print(solution(n))