import pickle
import re

class Lib():
    def __init__(self):
        self.D = dict()
        self.D['name'] = 'Python'
        self.D['scalar'] = 10.0
        self.D['vector'] = [6,6,6,6,6]
        self.D['matrix'] = [[3.0e3,3.0,3.0],[4.0,4.0,4.0]]

    def save(self):

        for k,v in self.D.items():
            if type(v) is str:
                pass
            elif type(v) is dict:
                pass
            elif type(v) is (float or int):
                v = str(v)
            else:
                v = str(v).replace('], [',';')
                v = v.replace('[[','[')
                v = v.replace(']]',']')
                v = v.replace(',','')
            self.D[k] = v

        with open('data.p','wb') as file:
            pickle.dump(self.D,file)
    
    def load(self):
        with open('data.p','rb') as file:
            self.D = pickle.load(file)

        for k,v in self.D.items():
            if re.search(r'[a-zA-Z]',v): # string
                pass
            else:
                if re.search(r'\.',v): # float
                    v = self.Str_to_List(v,float)
                else: # int
                    v = self.Str_to_List(v,int)
            self.D[k] = v

        print('name:  ',self.D['name'])
        print('scalar:',self.D['scalar'])
        print('vector:',self.D['vector'])
        print('matrix:',self.D['matrix'])

    def Str_to_List(self,s,typ):
        l = s.replace(',','')
        l = l.split(';')
        l[0] = l[0].replace('[','')
        l[-1] = l[-1].replace(']','')
        for i in range(len(l)):
            l[i] = [typ(x) for x in re.split(' ',l[i])]
        if(len(l[0]) == 1): # number
            return l[0][0]
        elif(len(l) == 1): # vector
            return l[0]
        else: # matrix
            return l

A = Lib()
A.save()
A.load()