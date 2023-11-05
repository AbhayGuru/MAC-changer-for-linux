#!usr/bin/env python
import subprocess
import optparse
def read_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change mac_address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Enter New mac_address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("\n[-] Please provide interface, for more information -h or --help.")
    if not options.new_mac:
        parser.error("\n[-] Please provide new_mac address, for more information -h or --help.")
    return options

def mac_changer(port,mac):
    '''
    subprocess.call("ifconfig eth0 down", shell=True)
    subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:44", shell=True)
    subprocess.call("ifconfig eth0 up", shell=True)
    subprocess.call("ifconfig",shell=True)

    port= input("Enter the Interface >")
    mac= input("Enter the New_Mac address >")
    port= options.interface
    mac= options.new_mac
    '''

    subprocess.call(["ifconfig", port, "down"])
    subprocess.call(["ifconfig", port, "hw", "ether", mac])
    subprocess.call(["ifconfig", port, "up"])
    print("[+] Changed MAC address to", mac, "of interface", port +"...")
    print("[+] Done...")
    #subprocess.call(["ifconfig"])

options=read_arguments()
#(options, arguments)=read_arguments()
mac_changer(options.interface,options.new_mac)
