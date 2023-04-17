# ESP-NOW Communication between 2 M5Stack boards: sender example 

from m5stack import *
from machine import Pin
from time import *
from libs.m5_espnow import M5ESPNOW

local_mac = None  # variable for local MAC address (this board)
peer_mac = None  # variable for peer MAC address 
counter = 0 

# initialize ESP-NOW:
espnow = M5ESPNOW(1)  

# get the local MAC address:
local_mac = espnow.espnow_get_mac()
print('MAC address of this board: ', local_mac)

# get the peer MAC address:
while (peer_mac == None):
    print('scanning for peer board..')
    peer_mac = espnow.espnow_scan(1, 'M5_Receiver')
print('MAC address of peer board: ', peer_mac)

# establish communication with the peer board:
espnow.espnow_add_peer(peer_mac) 

# send message callback function:
def send_cb(flag):
    if(flag == True):
        print('succeed!')
    else:
        print('failed..')

# register send message callback function:
espnow.espnow_send_cb(send_cb)  

while True:
    # send counter value as a key:value string:
    send_str = 'counter:' + str(counter)
    print('sending.. ' + send_str)
    espnow.espnow_send_str(1, send_str)
    counter += 1  # increment counter
    sleep_ms(1000)