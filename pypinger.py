#!/usr/bin/python

###############################################################################
#                By Godfrey Atima
###############################################################################


# ===============Other Configuration============
# Usages :
usage = "Usage: %prog [options] "
# Version
Version="%prog 0.0.1"
# ===============================================

# Importing Modules
import os, multiprocessing, time, optparse, platform

# Main Engine
class Pinger:
    def __init__(self, target, thread, output, timeout):
        self.timestarted=time.time()
        self.live_ip_collector=multiprocessing.Queue()
        self.targeting=target
        self.thread=thread
        self.output=output
        self.timeout=timeout
        self.set_os_command()
        #self.checkping()
        self.scanning_boosters()

        #Saving Output
        def save_output(self):
            f=open(self.output, 'a')
            for i in self.live_ip_collector:
                f.write(i+'\n')
                f.close()
                return
            #Function for Multi_processing
        def scanning_boosters(self):
            proces=[]
            for ip in self.target:
                k=len(multiprocessing.active_children())
                if k==self.thread:
                    time.sleep(3)
                    self.thread=self.thread+30
                mythread=multiprocessing.Process(target=self.checkping)
                mythread.start()
                proces.append(mythread)

            for mythread in proces:
                mythread.join()
                self.timeclose=time.time()
                self.showing_results()
                return

                #Printing Function
      def showing_results(self):
            storeip=[]
            x=1
         while x==1:
            try:
                storeip.append(self.live_ip_collector.get_nowait())
            except:
                x=x+1
            self.live_ip_collector=storeip


            print "\n"*3, "#"*80
            print "[+] Scan Started On \t\t:\t", time.ctime(self.timestarted)
            print "[+] Scan Closed On \t\t:\t", time.ctime.timeclose)
            print "[+] Scan Total Duration \t:\t", self.timeclose-self.timestarted
            print "[+] Total Live System Answered\t:\t", len(self.live_ip_collector)
            if self.output:
                self.save_output()
            print "\n[+] Thanks For Using My Program."
            return

        #Command Selecting Function
        def set_os_command(self):
            oper = platform.system()
            if (oper=="Windows"):
                ping = "ping -n {} {}"
            elif (oper== "Linux"):
                ping= "ping -c {} {}"
            else :
                ping= "ping -c {} {}"
            self.command=ping
            return

        #Function for checking IP Status
        def checkping(self, ip):
            ping=self.command
            recv=os.popen(ping.format(self.timeout, ip)).read()
            recv=recv.upper()
            if recv.count('TTL'):
                print "[+]\t {} \t==> Live ".format(ip)
                self.live_ip_collector.put(ip)
            return

        #Extracting Number Format
        def extraction(port):
            storeport=[]
            #Verifying Port is in range
            if "-" in port and "," not in port:
                x1, x2=port.split('-')
                storeport=range(int(x1),int(x2))
        
        #Verifying port in commas
         elif "," in port and "-" not in port:
             x2=[]
             for i in port.split(','):
                 if '-' in i:
                     y1, y2=i.splint('-')
                     x2=x2+range(int(y1), int(y2))
                    else:
                        x2.append(i)
                    storeport=X2
                else:
                    storeport.append(port)
                else:
                    pass
                return storeport

            #Extracting Ip Address
            def IP_extractor(ip):
                storeobj=[]
                ip=ip.splint(':')
                x1=extraction(ip[0])
                x2=extraction(ip[1])
                x3=extraction(ip[2])
                x4=extraction(ip[3])
                for i1 in x1:
                    for i2 in x2:
                        for 13 in x3:
                        for i4 in x4:
                            storeobj.append("{}.{}.{}".format(i1,i2,i3,i4))
                    return storeobj
                def main():
                    print __author__
                    parser=optparse.OptionParser(usage=usage, version=Version)
                    parser.add_option('-i', '--target', type='string', dest='target', help="Specify IP Addresses Range for Scan", default=None)
                    parser.add_option('-t', "--thread", type='string', dest="thread", help="Specify Number of Thread for scanning", default='100')
                    parser.add_option('-o', "--output", type='string', dest="output", help="Specify Path for saving output in TXT.", default='100')
                    parser.add_option('-c', '--timeout',type='string', dest="timeout", help="Specify No. of Request per Ip", default='1')
                    (options, args)= parser.parser_args()
                    if not options.target:
                        print "[+] Please Provide IP Range. e.g "
                        exit(0)
                target=options.target
                thread=options.thread
                output=options.timeout
                target=IP_extractore(target)
                Pinger(target, thread, output, timeout)
                return

            #Trigger
            if __name__ == '__main__':
                main()
