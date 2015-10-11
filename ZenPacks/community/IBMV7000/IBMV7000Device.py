##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 September, 2015
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################


from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class IBMV7000Device(Device):
  
  
  meta_type = portal_type = 'IBMV7000Device'
 

  total_mdisk_capacity = None
  total_used_capacity  = None

  _properties = Device._properties + (
    {'id': 'total_mdisk_capacity','type':'string'},
    {'id': 'total_used_capacity', 'type':'string'},
  )
  
  _relations = Device._relations + (
    ('enclosures',ToManyCont(ToOne,'ZenPacks.community.IBMV7000.Enclosure','enclosure_device',)),
    ('batteries',ToManyCont(ToOne,'ZenPacks.community.IBMV7000.Battery','battery_device',)),
    ('drives',ToManyCont(ToOne,'ZenPacks.community.IBMV7000.Drive','drive_device',)),
  )

