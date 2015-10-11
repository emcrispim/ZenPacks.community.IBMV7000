================================
ZenPacks.community.IBMV7000
================================


About
=====

This project is a extension (ZenPack) for the Zenoss, it models and monitors the
IBM V7000 storwize through SSH 


Requirements
============

Zenoss
------

You must first have, or install, Zenoss 4.2 or later. This ZenPack was tested
against Zenoss 4.2 only

Installation

============


Normal Installation (packaged egg)
----------------------------------

Download the IBMV7000 ZenPack  [http://community.zenoss.org/docs/DOC-XXXX](http://community.zenoss.org/docs/DOC-XXXX).
Copy this file to your Zenoss server and run the following commands as the zenoss
user.


        zenpack --install ZenPacks.community.IBMV7000.egg
        zenoss restart

Developer Installation (link mode)
----------------------------------

If you wish to further develop and possibly contribute back to the IBMV7000
ZenPack you should clone the git [https://github.com/emcrispim/ZenPacks.community.IBMV700](https://github.com/emcrispim/ZenPacks.community.IBMV7000),
then install the ZenPack in developer mode using the following commands.


        git clone git://github.com/emcrispim/ZenPacks.community.IBMV7000.git
        zenpack --link --install ZenPacks.community.IBMV7000
        zenoss restart

After Installation
-------------------

The IBM7000 ZenPack will create a new device class organizer "/Storage/IBMV7000". 

Usage
=====

 A user account is required in order to login against the IBMV7000 SSH service. The account only requires a low level permission ("Monitor" User Group), this can be achieved browsing the web console menu:
 access > users


Use the account in the follow Configurations Properties

Configuration Properties
------------------------
- zCommandUsername
- zCommandPassword

The IBMV7000 SSH service can also be authenticated with SSH Keys.

Modeler Plugins
---------------

- community.cmd.IBMV7000

Monitoring Templates
--------------------

- IBMV7000

Performance graphs
------------------

- CPU utilization
- Interfaces throughput
- Volumes
  - Read and Write (MBps)
  - Read and Write Latency (ms)
- MDisks
  - Read and Write (MBps)
  - Read and Write Latency (ms)
