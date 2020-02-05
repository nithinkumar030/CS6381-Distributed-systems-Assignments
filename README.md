# CS6381-Distributed-systems-Assignments

Assignment -1 
The assignment creates the pub/sub and broker demonstration using a multithreaded architecture.

The unit test that the pub/sub has 2 parts - 1) topic test – which tests how the selection of number of  topics by pub/sub affect the latencies of message dissemination. 2) Data size test here the publisher sends data of various size like 1k 10k and 100k to the subscriber and latency of message dissemination is calculated.

To run the test first start the broker by typing the python broker.py in one console. Then start the subscriber on the other console by typing python sub.py and finally start the publisher on another console by typing python pub.py.
The Unit test runs 4 test modules  -
1)pub1 -> sub1(topic Weather ), 2)pub2-> sub2(topic news), 3)pub3-> sub3(topic Stock and topic movie) and prints the time stamp at pub and sub . We need to calculate the delta of time from Pub to sub as shown in excel sheet by entering the timestamp values of pub and sub .
4)Data size test – This prints the timestamps for pub and sub for  1k 10k and 100k data size. The timestamp at both pub and sub sides are noted entered in excel sheet to calculate the graphs .
