#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import time

#
# layer 1 functions
#


def zmq_client_req_snd_and_recv( zmq_addr, value):

    context = zmq.Context()
    #  Socket to talk to server
    socket = context.socket(zmq.REQ)
    socket.connect(zmq_addr)
    print("Sending req_pub...\n")
    socket.send_string(value)
    print("send done")
    #time.sleep(1)
    print("Receiving req_pub_rep\n")
    value=socket.recv_string()
    print("Received req_pub_rep\n")
    return value




def zmq_client_send_pub( zmq_addr,value):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    print(zmq_addr)
    socket.connect(zmq_addr)
    print("Sending pub...\n" )
    socket.send_string(value)
    print("Sent pub\n")

#
# middleware 2 functions
#

topicDict=dict()

def register_pub(topic,pubID):
     msgData=[0,1]
     #let the broker default addr is localhost:5555
     ip_addr_str = 'tcp://127.0.0.1:5555'
     msgData[0]=topic
     msgData[1]=pubID
     pub_ipaddr_str=zmq_client_req_snd_and_recv(ip_addr_str,topic)
     topicDict[topic]=pub_ipaddr_str
     return



def publish(topic,data):
    print(topicDict) 
    pub_ipaddr_str=topicDict[topic]
      
    zmq_client_send_pub(pub_ipaddr_str,data)

#
# Test function - later 3 app
#


def weather_pub1_init():
     topic='Weather'
     pubID='met-010'

     register_pub(topic,pubID)

def weather_pub1():
     publish('Weather','Nashville-40F')

def weather_pub1_data(size):
     data=data_size_supply(size)
     publish('Weather',data)

def news_pub2_init():
     register_pub('News','Breaking news!')
     
def news_pub2():
     publish('News','Elections in USA')
     

def stock_pub3_init():
     register_pub('Stock','NYSE')
     register_pub('Movie','latest-films')
    

def stock_and_movie_pub3():
     publish('Stock','GOOG-1543')
     start_time = time.time()
     print("pub3 Movie  publish start timestamp",start_time)
     publish('Movie','Avatar2')


def data_size_supply(size):
    if size == 1:
        f = open("1k.txt", "r")
        data =  f.read()
    elif size == 2:
        f = open("10k.txt", "r")
        data =  f.read()
    elif size == 3:
        f = open("100k.txt", "r")
        data =  f.read()
    else:
        pass

    return data


     


def perf_test_1_pub():
    weather_pub1_init()
    count = 0

    while(1):
        start_time = time.time()
        print("pub1 publish start timestamp",start_time)
    
        weather_pub1()
        count=count+1
        time.sleep(1)
        if count == 1:
            print("pub test done")
            count=0
            break

    return



def perf_test_2_pub():
    news_pub2_init()
    count = 0

    while(1):
        start_time = time.time()
        print("pub2 publish start timestamp",start_time)
    
        news_pub2()
        count=count+1
        time.sleep(1)
        if count == 1:
            print("pub2 test done")
            count=0
            break

    return

def perf_test_3_pub():
    stock_pub3_init()
    count = 0

    while(1):
        start_time = time.time()
        print("pub3 publish start timestamp",start_time)
    
        stock_and_movie_pub3()
        count=count+1
        time.sleep(1)
        if count == 1:
            print("pub3 test done")
            count=0
            break

    return


def data_test_pub():
    count = 1

    while(1):
        start_time = time.time()
        print("pub publish start timestamp",start_time)
    
        weather_pub1_data(count)
        count=count+1
        time.sleep(1)
        if count == 4:
            print("pub1 data size test done")
            count=0
            break

    return



def main():
        
    print("***********1 PUB perf test **************\n")
    perf_test_1_pub()
    time.sleep(1)
    print("***********2 PUB perf test **************\n")
    perf_test_2_pub()
    time.sleep(1)
    print("***********3 PUB perf test **************\n")
    perf_test_3_pub()
    print("***********4 Data test pub sub ***********\n")
    data_test_pub()

    print("Test over!")

    return
   


if __name__ == '__main__':
    main()
      



#  Do 10 requests, waiting each time for a response
#for request in range(10):
#    print("Sending request %s …" % request)
#    socket.send(b"Hello")

#    #  Get the reply.
#    message = socket.recv()
#    print("Received reply %s [ %s ]" % (request, message))

