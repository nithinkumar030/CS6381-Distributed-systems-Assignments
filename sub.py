#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#


#
# layer 1 ZMQ functions
#
import zmq
import time
import threading

def zmq_client_req_snd_and_recv( zmq_addr,value):

    context = zmq.Context()
    #  Socket to talk to server
    socket = context.socket(zmq.REQ)
    socket.connect(zmq_addr)
    print("Sending req_sub...\n")
    socket.send_string(value)
    print("send done")
    #time.sleep(1)
    print("Receiving req_sub_rep\n")
    value=socket.recv_string()
    print("Received req_sub_rep\n")
    return value

def zmq_client_recv_sub( zmq_addr):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    print(zmq_addr)
    socket.connect(zmq_addr)
    print("Receiving sub...\n" )
    value=socket.recv_string()
    print("got sub\n")
    return value


#
#layer 2 ZMQ function
#
topicDict=dict()

def register_sub(topic,subID):
    #let the broker default addr is localhost:6666
    msgData=[0,1] 
    ip_addr_str = 'tcp://localhost:6666'
    sub_ipaddr_str=zmq_client_req_snd_and_recv(ip_addr_str,topic)
    topicDict[topic]=sub_ipaddr_str
    return

def subscribe(topic):
    sub_ipaddr_str=topicDict[topic]
    
    data=zmq_client_recv_sub(sub_ipaddr_str)
    return data



#
# Test function - later 3 app
#


def sub1_init():

    register_sub('Weather','sub1')


def sub1():
    while(1):

        data1=subscribe('Weather')
        start_time = time.time()
        print("sub1  recvd  timestamp:\n",start_time)
        print("Sub1:\n",data1)
        
        #time.sleep(1)
    #data2=subscribe('Stock')
    #print("Sub1:\n",data2)

def sub2_init():
    register_sub('News','sub2')

def sub2():
    while(1):
        data1=subscribe('News')
        start_time = time.time()
        print("sub2  recvd  timestamp:\n",start_time)
        print("Sub2:\n",data1)


        #time.sleep(1)

def sub3_init():
    register_sub('Stock','sub3')
    register_sub('Movie','sub4')

def sub3():
    while(1):
        data1=subscribe('Stock')
        print("Sub3:\n",data1)
        start_time = time.time()
        print("sub3  recvd  timestamp:\n",start_time)
        print("Sub3:\n",data1)
        data1=subscribe('Movie')
        start_time = time.time()
        print("sub3  recvd  timestamp:\n",start_time)
        print("Sub3:\n",data1)




        #time.sleep(1)

def sub4_init():
    register_sub('Sports','sub4')
    


def sub4():
    while(1):

        data1=subscribe('Sports')
        start_time = time.time()
        print("sub4  recvd  timestamp:\n",start_time)
        print("Sub4:\n",data1)
        






def main():

    print("***************Subcriber runnning***********\n")
    sub1_init()
    threading.Thread(target=sub1).start()

    sub2_init()
    threading.Thread(target=sub2).start()

    sub3_init()
    threading.Thread(target=sub3).start()

    #sub4_init()
    #threading.Thread(target=sub4).start()


   


if __name__ == '__main__':
    main()
      



#  Do 10 requests, waiting each time for a response
#for request in range(10):
#    print("Sending request %s …" % request)
#    socket.send(b"Hello")

#    #  Get the reply.
#    message = socket.recv()
#    print("Received reply %s [ %s ]" % (request, message))

