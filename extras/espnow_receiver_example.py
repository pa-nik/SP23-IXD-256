# ESP-NOW Communication between 2 M5Stack boards: receiver example 

from m5stack import *
from machine import Pin
from time import *
from libs.m5_espnow import M5ESPNOW

local_mac = None  # variable for local MAC address (this board)
peer_mac = None  # variable for peer MAC address 

# initialize ESP-NOW:
espnow = M5ESPNOW(1) 

# get the local MAC address:
local_mac = espnow.espnow_get_mac()
print('MAC address of this board: ', local_mac)

# receive message callback function:
def recv_cb(dummy):
    mac_addr, data_str = espnow.espnow_recv_str()
    print('received from ' + mac_addr + '.. ' + data_str)
    # split data string into key:value pair:
    if(':' in data_str):
        data_list = data_str.split(':')  # split string by colon
        data_key = data_list[0]
        data_val = data_list[1]
        if(data_key == 'counter'):
            print('counter = ' + data_val)

# register receive message callback function:
espnow.espnow_recv_cb(recv_cb)

# set the ID of this board:
espnow.espnow_set_ap('M5_Receiver', '')

print('waiting for messages from sender..')

while(True):
    sleep_ms(1000)
