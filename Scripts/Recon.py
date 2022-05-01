import random
import nmap 


def nmap_scan_1():
    nm = nmap.PortScanner()
    nm.scan('127.0.0.1', '22-500')
    nm.scaninfo()



if __name__ == "__main__":


    nmap_scan_1()







