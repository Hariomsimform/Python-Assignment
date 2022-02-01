
class Gcd:

    final_string='' #this varialbe return the final ansewer from IntToWord Function...
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.sdata=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        
        self.word_to_int_con(num1,num2) 

     #this function outer function of inner funciton that will convert string to numeric string of given input  
    def word_to_int_con(self, string1, string2):  
       
       #in these given variables numeric string of given input will store
        int_num1 = ''
        int_num2 = ''
     
     # converter function will acutlly convert the string in numeric string
        def converter(string1,string2,int_num1,int_num2):
            
            
            #this if condition will check the length of remaining string to convert it into numeric string
            #if condition this conditio is true it means both the stirng is converted into numeric string
            if len(string1) <= 0 and len(string2) <= 0:
                
                #as enter here it will take two input int_num1 and int_num2 and convert it into int and start calculating GDC
                final_int = self.gdc_calc(int(int_num1),int(int_num2))  
            
               
                final_ans = self.int_to_word_con(final_int)
                print(final_ans)
                
                return 0
          
            else:
                def searcher(string1,int_num1):
                    if string1[:3] in self.sdata:
                        int_num1 += str(self.sdata.index(string1[:3]))
                        string1 = string1[3:]
                        
                    elif string1[:4] in self.sdata:
                        int_num1 += str(self.sdata.index(string1[:4]))
                        string1 = string1[4:]    
                        
                    elif string1[:5] in self.sdata:
                        int_num1 += str(self.sdata.index(string1[:5]))
                        string1 = string1[5:]  
                    elif len(string1)>0:
                        print(f'Your string "{string1}" is not valid, your words is not from this list {self.sdata}') 
                    return string1,int_num1    
   
            string1,int_num1=searcher(string1,int_num1)     
           
            string2,int_num2=searcher(string2,int_num2)     
                        
            converter(string1,string2,int_num1,int_num2)
        
        converter(string1,string2,int_num1,int_num2) 
        
    def gdc_calc(self, num1, num2):
       
        if num1==0:
            return num2
        if num2==0:
            return num1
        if num1==num2:
            return num1    
        
        if num1 > num2:
            return self.gdc_calc(num1-num2,num2)  
        return self.gdc_calc(num1,num2-num1)      

        # this function will convert digit to word that is final answer 
    def int_to_word_con(self,final_int):
        
      
       
        if final_int==0:
            return
        temp=final_int%10
        final_int=final_int//10
        self.int_to_word_con(final_int)
        self.final_string += self.sdata[temp]    
       
        return self.final_string    

if __name__ == "__main__":
    input1=input()
    input2=input()
    c=Gcd(input1,input2)

