##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 September, 2015
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class Enclosure(DeviceComponent,ManagedEntity):
  meta_type = portal_type = "IBMV7000Enclosure"

  enclosure_status = None
  enclosure_type = None
  product_MTM = None
  serial_number = None
  total_canisters = None
  online_canisters = None
  total_PSUs = None
  online_PSUs = None
  drive_slots = None
  total_fan_modules = None
  online_fan_modules = None


  _properties = ManagedEntity._properties + (
    {'id': 'enclosure_status', 'type': 'string'},
    {'id': 'enclosure_type', 'type': 'string'},
    {'id': 'product_MTM', 'type': 'string'},
    {'id': 'serial_number', 'type': 'string'},
    {'id': 'total_canisters', 'type': 'int'},
    {'id': 'online_canisters', 'type': 'int'},
    {'id': 'total_PSUs', 'type': 'int'},
    {'id': 'online_PSUs', 'type': 'int'},
    {'id': 'drive_slots', 'type': 'int'},
    {'id': 'total_fan_modules', 'type': 'int'},
    {'id': 'online_fan_modules', 'type': 'int'},
  )

  _relations = ManagedEntity._relations + (
    ('enclosure_device', ToOne(ToManyCont,
      'ZenPacks.community.IBMV7000.IBMV7000Device','enclosures',
      ),
    ),
  )


  factory_type_information = ({
    'actions': ({
      'id': 'perfConf',
      'name': 'Template',
      'action': 'objTemplates',
      'permissions': (ZEN_CHANGE_DEVICE,),
    },),
  },)

  def device(self):
    return self.enclosure_device()

  def getRRDTemplateName(self):
    return 'IBMV7000Enclosure'

