import socket  #importing library  
ip = 127.0.0.1 
  
for port in range(80,82):      #check for all available ports 
  
    try: 
   
        serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket 
  
        serv.bind((ip,port)) # bind socket with address 
             
    except: 
  
        print('[OPEN] Port open :',port) #print open port number 
  
    serv.close() #close connection 
