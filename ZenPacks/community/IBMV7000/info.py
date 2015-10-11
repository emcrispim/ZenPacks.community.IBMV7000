##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 September, 2015
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################


from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo

from ZenPacks.community.IBMV7000.interfaces import (
    IIBM7000DeviceInfo,
    IEnclosureInfo,
    IBatteryInfo,
    IDriveInfo,
)


class IBM7000DeviceInfo (DeviceInfo):
    implements(IIBM7000DeviceInfo) 

    @property
    def storage_capacity(self):
        r ='Unknown / Unknown'
        try:
            r = self._object.total_used_capacity+' / '+self._object.total_mdisk_capacity
        except:
            # cannot perfom operation if no values available
            pass
        return r
    

class EnclosureInfo(ComponentInfo):
    implements(IEnclosureInfo)

    id = ProxyProperty('id')
    enclosure_status = ProxyProperty('enclosure_status')
    enclosure_type = ProxyProperty('enclosure_type')
    product_MTM = ProxyProperty('product_MTM')
    serial_number = ProxyProperty('serial_number')
    total_canisters = ProxyProperty('total_canisters')
    online_canisters = ProxyProperty('online_canisters')
    total_PSUs = ProxyProperty('total_PSUs')
    online_PSUs = ProxyProperty('online_PSUs')
    drive_slots = ProxyProperty('drive_slots')
    total_fan_modules = ProxyProperty('total_fan_modules')
    online_fan_modules = ProxyProperty('online_fan_modules')


class BatteryInfo(ComponentInfo):
    implements(IBatteryInfo)

    id = ProxyProperty('id')
    enclosure_ID = ProxyProperty('enclosure_ID')
    battery_status = ProxyProperty('battery_status')
    charging_status = ProxyProperty('charging_status')
    recondition_needed = ProxyProperty('recondition_needed')
    percent_charged = ProxyProperty('percent_charged')
    end_of_life_warning = ProxyProperty('end_of_life_warning')


class DriveInfo(ComponentInfo):
    implements(IDriveInfo)

    id = ProxyProperty('id')
    drive_status = ProxyProperty('drive_status')
    error_sequence_number = ProxyProperty('error_sequence_number')
    use = ProxyProperty('use')
    tech_type = ProxyProperty('tech_type')
    capacity = ProxyProperty('capacity')
    enclosure_id = ProxyProperty('enclosure_id')
    slot_id = ProxyProperty('slot_id')



