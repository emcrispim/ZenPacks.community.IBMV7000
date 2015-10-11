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


from Products.ZenUtils.ZenScriptBase import ZenScriptBase


class Battery(DeviceComponent,ManagedEntity):
  meta_type = portal_type = "IBMV7000Battery"

  enclosure_ID = None
  battery_status = None
  charging_status = None
  recondition_needed = None
  percent_charged = None
  end_of_life_warning = None
  

  _properties = ManagedEntity._properties + (
    {'id': 'enclosure_ID', 'type': 'string'},
    {'id': 'battery_status', 'type': 'string'},
    {'id': 'charging_status', 'type': 'string'},
    {'id': 'recondition_needed', 'type': 'string'},
    {'id': 'percent_charged', 'type': 'int'},
    {'id': 'end_of_life_warning', 'type': 'string'},
  )

  _relations = ManagedEntity._relations + (
    ('battery_device', ToOne(ToManyCont,
      'ZenPacks.community.IBMV7000.IBMV7000Device','batteries',
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
    return self.battery_device()

  def getRRDTemplateName(self):
    return 'IBMV7000Battery'

