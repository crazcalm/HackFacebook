import webbrowser, time, random
from sad import depression

def create_magic():
    
    stack = depression()
    
    for x in range(len(stack)):
        stack.append("http://www.pickuplinegenerator.com/")
        
    #print len(stack)
    return stack

def haha():
    
    stack = create_magic()
    
    for num in range(3):
        
        url = random.choice(stack)
        webbrowser.open(url)
        time.sleep(3)
        
if __name__ == '__main__':
    haha()