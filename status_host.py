#################################################
Author: Yakov Myagkov, Russia, Moscow
Date: 18.09.2021
################################################
import atexit
from pyVim.connect import Disconnect, SmartConnectNoSSL
import datetime
time = datetime.datetime.now().strftime(('%Y-%m-%d_%H-%M'))
from threading import *


printHost = True


def printHostInformation(host):
    try:
        connection = host.runtime.connectionState
        maintenanceMode = host.runtime.inMaintenanceMode
        if maintenanceMode == True and connection == 'connected':
            print(f'{host.name}; Maintenance')
        elif connection == 'disconnected':
            print(f'{host.name}; Disconnected')
        elif maintenanceMode == False and connection == 'connected':
            print(f'{host.name}; Connected')
        elif connection == 'notResponding':
            print(f'{host.name}; NotResponding')
    except Exception as error:
        print("Unable to access information for host: ", host.name)
        print(error)
        pass


def printComputeResourceInformation(computeResource):
    try:
        hostList = computeResource.host
        for host in hostList:
            printHostInformation(host)
    except Exception as error:
        print("Unable to access information for compute resource: ",
              computeResource.name)
        print(error)
        pass


def main1():
    vcenter1 = SmartConnectNoSSL(host='your_url_Vcenter', user='your_login', pwd='your_password')
    atexit.register(Disconnect, vcenter1)
    content = vcenter1.RetrieveContent()
    for datacenter in content.rootFolder.childEntity:
        if printHost:
            if hasattr(datacenter.hostFolder, 'childEntity'):
                hostFolder = datacenter.hostFolder
                computeResourceList = hostFolder.childEntity
                for computeResource in computeResourceList:
                    printComputeResourceInformation(computeResource)


# def main2():
#     vcenter2 = SmartConnectNoSSL(host='your_url_Vcenter', user='your_login', pwd='your_password')
#     atexit.register(Disconnect, vcenter2)
#     content = vcenter2.RetrieveContent()
#     for datacenter in content.rootFolder.childEntity:
#         if printHost:
#             if hasattr(datacenter.hostFolder, 'childEntity'):
#                 hostFolder = datacenter.hostFolder
#                 computeResourceList = hostFolder.childEntity
#                 for computeResource in computeResourceList:
#                     printComputeResourceInformation(computeResource)
#
#
# def main3():
#     vcenter3 = SmartConnectNoSSL(host='your_url_Vcenter', user='your_login', pwd='your_password')
#     atexit.register(Disconnect, vcenter3)
#     content = vcenter3.RetrieveContent()
#     for datacenter in content.rootFolder.childEntity:
#         if printHost:
#             if hasattr(datacenter.hostFolder, 'childEntity'):
#                 hostFolder = datacenter.hostFolder
#                 computeResourceList = hostFolder.childEntity
#                 for computeResource in computeResourceList:
#                     printComputeResourceInformation(computeResource)
#
#
# def main4():
#     vcenter4 = SmartConnectNoSSL(host='your_url_Vcenter', user='your_login', pwd='your_password')
#     atexit.register(Disconnect, vcenter4)
#     content = vcenter4.RetrieveContent()
#     for datacenter in content.rootFolder.childEntity:
#         if printHost:
#             if hasattr(datacenter.hostFolder, 'childEntity'):
#                 hostFolder = datacenter.hostFolder
#                 computeResourceList = hostFolder.childEntity
#                 for computeResource in computeResourceList:
#                     printComputeResourceInformation(computeResource)
#
#
# def main5():
#     vcenter5 = SmartConnectNoSSL(host='your_url_Vcenter', user='your_login', pwd='your_password')
#     atexit.register(Disconnect, vcenter5)
#     content = vcenter5.RetrieveContent()
#     for datacenter in content.rootFolder.childEntity:
#         if printHost:
#             if hasattr(datacenter.hostFolder, 'childEntity'):
#                 hostFolder = datacenter.hostFolder
#                 computeResourceList = hostFolder.childEntity
#                 for computeResource in computeResourceList:
#                     printComputeResourceInformation(computeResource)
#
#
# def main6():
#     vcenter6 = SmartConnectNoSSL(host='your_url_Vcenter', user='your_login', pwd='your_password')
#     atexit.register(Disconnect, vcenter6)
#     content = vcenter6.RetrieveContent()
#     for datacenter in content.rootFolder.childEntity:
#         if printHost:
#             if hasattr(datacenter.hostFolder, 'childEntity'):
#                 hostFolder = datacenter.hostFolder
#                 computeResourceList = hostFolder.childEntity
#                 for computeResource in computeResourceList:
#                     printComputeResourceInformation(computeResource)


t1 = Thread(target=main1, args=())
# t2 = Thread(target=main2, args=())
# t3 = Thread(target=main3, args=())
# t4 = Thread(target=main4, args=())
# t5 = Thread(target=main5, args=())
# t6 = Thread(target=main6, args=())

if __name__ == "__main__":
    t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()

