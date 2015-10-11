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

class Drive(DeviceComponent,ManagedEntity):
  meta_type = portal_type = "IBMV7000Drive"

  drive_status = None
  error_sequence_number = None
  use = None
  tech_type = None
  capacity = None
  enclosure_id = None
  slot_id = None
  

  _properties = ManagedEntity._properties + (
    {'id': 'drive_status', 'type': 'string'},
    {'id': 'error_sequence_number', 'type': 'string'},
    {'id': 'use', 'type': 'string'},
    {'id': 'tech_type', 'type': 'string'},
    {'id': 'capacity', 'type': 'string'},
    {'id': 'enclosure_id', 'type': 'int'},
    {'id': 'slot_id', 'type': 'int'},
  )

  _relations = ManagedEntity._relations + (
    ('drive_device', ToOne(ToManyCont,
      'ZenPacks.community.IBMV7000.IBMV7000Device','drives',
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
    return self.drive_device()

  def getRRDTemplateName(self):
    return 'IBMV7000Drive'

