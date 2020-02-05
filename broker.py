#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import threading
import time
import zmq

#topicPubIDDict=dict()
topicPubIpAddrDict=dict()
topicSubIpAddrDict=dict()
topicValueDict=dict()

def zmq_server_recv_pub_req_send_rsp():
    
    port=5555

    while True:
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        #socket.bind("tcp://*:5555")
        socket.bind("tcp://127.0.0.1:5555")


        #Wait for next request from client
        message = socket.recv_string()
        print("Received pub_req: %s" % message)
        topic=message[0]
        pubID=message[1]

        #topicPubIDDict[topic]=pubID

        #  Do some 'work'
        #time.sleep(1)
        port=port+1

        msg='tcp://127.0.0.1:'+str(port)
        topicPubIpAddrDict[topic]=msg
        #start the new pub socket to recv
        recv_pub_init(topic)
        #  Send reply back to client with new ip_addr_str
        socket.send_string(msg)

        



def zmq_server_recv_pub(addr_str):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(addr_str)

    #  Wait for next request from client
    message = socket.recv_string()
    print("Received sub_req: %s" % message)
    return message

def zmq_server_send_sub(addr_str,data):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.bind(addr_str)

    #  Wait for next request from client
    socket.send_string(data)
    print("send sub_req: %s" % data)
    




def zmq_server_recv_sub_req_send_rsp():
    port=6666

    while True:
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        #socket.bind("tcp://*:6666")
        socket.bind("tcp://127.0.0.1:6666")
        

        #Wait for next request from client
        message = socket.recv_string()
        print("Received sub_req: %s" % message)
        topic=message[0]
        pubID=message[1]

        #topicPubIDDict[topic]=pubID
        #  Do some 'work'
        #time.sleep(1)
        port=port+1

        msg='tcp://127.0.0.1:'+str(port)
        topicSubIpAddrDict[topic]=msg
        #start the new pub socket to recv
        send_sub_init(topic)
        #  Send reply back to client with new ip_addr_str
        socket.send_string(msg)





# 
# Receive req_pub - Create thread 
#
def recv_req_pub_init():

    threading.Thread(target=zmq_server_recv_pub_req_send_rsp).start()
    #zmq_server_recv_pub_req_send_rsp()

def recv_req_sub_init():

    threading.Thread(target=zmq_server_recv_sub_req_send_rsp).start()


def recv_pub_init(topic):
    threading.Thread(target=recv_publish,args=[topic]).start()

def send_sub_init(topic):
    threading.Thread(target=send_subscribe,args=[topic]).start()



def recv_publish(topic):

    
    while(1):
        ip_addr_str=topicPubIpAddrDict[topic]
        data=zmq_server_recv_pub(ip_addr_str)
        topicValueDict[topic]=data
        #time.sleep(1)


def send_subscribe(topic):
    while(1):
        try:
            ip_addr_str=topicSubIpAddrDict[topic]

            data=topicValueDict[topic]
                
            zmq_server_send_sub(ip_addr_str,data)
            del topicValueDict[topic]

        except Exception as e:
            #print("No data for topic\n")
            pass

        #time.sleep(1)
    


    


def main():
    print("*************Running BROKER ...\n***********")
    recv_req_pub_init()

    recv_req_sub_init()
   


if __name__ == '__main__':
    main()
