import bcrypt

class Encoder:

    def encode(self, string):   
        result=bcrypt.hashpw(string.encode('utf-8'), bcrypt.gensalt())    
        #resulta = bcrypt.hashpw('12345678'.encode('utf-8'),bcrypt.gensalt())        
        return result.decode('utf-8')
    def decode(self, string, password):
        result = bcrypt.checkpw(string.encode('utf-8'),password.encode('utf-8'))
        return result

if __name__ == '__main__':
    print(Encoder().encode("123")) #$2b$12$XGNJNq/ak0RiBYgAQP0G3OXcls7wXGcQ5IbE0Uy93uH6KsxHe4Myy