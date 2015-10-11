##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 September, 2015
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################


import Globals
from Products.ZenModel.ZenPack import ZenPack as ZenPackBase


# Required to test the relationships with command zenchkschema
productNames = (
  'IBMV7000Device',
  'Enclosure',
  'Battery',
  'Drive',
  )


class ZenPack(ZenPackBase):

  def install(self, dmd):
    # create the required device class 
    dc = dmd.Devices.createOrganizer('/Storage/IBMV7000')
    ZenPackBase.install(self, dmd)

  def remove(self, dmd, leaveObjects=False):
    
    if not leaveObjects:
      
      # Delete all instances of devices in /Storage/IBMV7000 - completely - including history and events
      #
      for dev in dmd.Devices.Storage.IBMV7000.getSubDevices():
        dev.deleteDevice(deleteStatus=True, deleteHistory=True, deletePerf=True)
         

      # Next line delete all subclasses too
      dmd.Devices.manage_deleteOrganizer('/Storage/IBMV7000')

      ZenPackBase.remove(self, dmd, leaveObjects=leaveObjects)

  
