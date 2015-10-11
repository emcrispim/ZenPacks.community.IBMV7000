##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 September, 2015
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################


from Products.Zuul.form import schema
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

class IIBM7000DeviceInfo(IDeviceInfo):
  total_mdisk_capacity = schema.TextLine(title=_t('Total Capacity size'))
  total_used_capacity = schema.TextLine(title=_t('Used Capacity size'))


class IEnclosureInfo(IComponentInfo):
  id = schema.TextLine(title=_t('Enclosure ID'))
  enclosure_status = schema.TextLine(title=_t('Status'))
  enclosure_type = schema.TextLine(title=_t('Type'))
  product_MTM = schema.TextLine(title=_t('Product MTM'))
  serial_number = schema.TextLine(title=_t('Serial Number'))
  total_canisters = schema.Int(title=_t('# Canisters'))
  online_canisters = schema.Int(title=_t('Online Canisters'))
  total_PSUs = schema.Int(title=_t('# PSUs'))
  online_PSUs = schema.Int(title=_t('Online PSUs'))
  drive_slots = schema.Int(title=_t('Drive Slots'))
  total_fan_modules = schema.Int(title=_t('# Fan modules'))
  online_fan_modules = schema.Int(title=_t('Online Fan Modules'))

      
class IBatteryInfo(IComponentInfo):
   id = schema.TextLine(title=_t('Battery ID'))
   enclosure_ID = schema.TextLine(title=_t('enclosure_ID'))
   battery_status = schema.TextLine(title=_t('Status'))
   charging_status = schema.TextLine(title=_t('Charging'))
   recondition_needed = schema.TextLine(title=_t('Recondition needed'))
   percent_charged = schema.Int(title=_t('Percent charged'))
   end_of_life_warning = schema.TextLine(title=_t('End of life Warning'))


class IDriveInfo(IComponentInfo):
   id = schema.TextLine(title=_t('Drive ID'))
   drive_status = schema.TextLine(title=_t('Drive Status'))
   error_sequence_number = schema.TextLine(title=_t('Error sequence number'))
   use = schema.TextLine(title=_t('Use'))
   tech_type = schema.TextLine(title=_t('Tech type'))
   capacity = schema.TextLine(title=_t('Capacity'))
   enclosure_id = schema.Int(title=_t('Enclosure ID'))
   slot_id = schema.Int(title=_t('Slot ID'))

