##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 September, 2015
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################


from Products.DataCollector.plugins.CollectorPlugin import CommandPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap, RelationshipMap
from ZenPacks.community.IBMV7000 import Utils

class IBMV7000(CommandPlugin):

  relname = 'drives'
  modname = 'ZenPacks.community.IBMV7000.Drive'

  # The command to run.
  command = (
    'lssystem;'
    'echo __COMMAND__;'
    'lsdrive -delim :;'
    'echo __COMMAND__;'
    'lsenclosure -delim :;'
    'echo __COMMAND__;'
    'lsenclosurebattery -delim :;'
    )
  

  def condition(self, device, log):
      return True

  def process(self, device, results, log):

    maps = []

    #striping the commands results
    data=results.split("__COMMAND__\n")


    # gathering info for lssystem command

    try:
      total_mdisk_capacity = data[0].split('total_mdisk_capacity')[1].split('\n')[0].strip()
    except:
      total_mdisk_capacity = "unknown"

    try:
      total_used_capacity = data[0].split('total_used_capacity')[1].split('\n')[0].strip()
    except:
      total_used_capacity = "unknown"

    maps.append(self.objectMap({
           'total_mdisk_capacity' : total_mdisk_capacity,
           'total_used_capacity'  : total_mdisk_capacity }))


    # parsing data for lsdrive command

    # results contents..
    #id:status:error_sequence_number:use:tech_type:capacity:mdisk_id:mdisk_name:member_id:enclosure_id:slot_id:node_id:node_name:auto_manage
    #0:online::member:sas_nearline_hdd:1.8TB:0:mdisk0:1:1:3:::inactive
    #1:online::spare:sas_nearline_hdd:1.8TB::::1:1:::inactive
    #2:online::member:sas_nearline_hdd:1.8TB:0:mdisk0:4:1:6:::inactive
    #3:online::member:sas_nearline_hdd:1.8TB:0:mdisk0:5:1:7:::inactive

    lsdrivedata = Utils.cmdParser(data[1],'id','DRIVE_ID')
    drives = []
    for key,item in lsdrivedata.iteritems():
      drives.append(ObjectMap(data={
        'id'                          : self.prepId(key),
        'title'                       : key,
        'drive_status'                : item['status'],
        'error_sequence_number'       : item['error_sequence_number'],
        'use'                         : item['use'],
        'tech_type'                   : item['tech_type'],
        'capacity'                    : item['capacity'],
        'enclosure_id'                : int(item['enclosure_id']),
        'slot_id'                     : int(item['slot_id']),
      }))

    maps.append(RelationshipMap(
      relname='drives',
      modname='ZenPacks.community.IBMV7000.Drive',
      objmaps=drives
    ))
    
    # parsing data for lsenclosure command
    # results contents..
    #enclosure_id:battery_id:status:charging_status:recondition_needed:percent_charged:end_of_life_warning
    #2:1:online:idle:no:100:no
    #2:2:online:idle:no:99:no

    lsenclosuredata = Utils.cmdParser(data[2],'id','ENC_ID')
    enclosures = []
    for key,item in lsenclosuredata.iteritems():
      enclosures.append(ObjectMap(data={
        'id'                          : self.prepId(key),
        'title'                       : key,
        'enclosure_status'            : item['status'],
        'enclosure_type'              : item['type'],
        'product_MTM'                 : item['product_MTM'],
        'serial_number'               : item['serial_number'],
        'total_canisters'             : int(item['total_canisters']),
        'online_canisters'            : int(item['online_canisters']),
        'total_PSUs'                  : int(item['total_PSUs']),
        'online_PSUs'                 : int(item['online_PSUs']),
        'drive_slots'                 : int(item['drive_slots']),
        'total_fan_modules'           : int(item['total_fan_modules']),
        'online_fan_modules'          : int(item['online_fan_modules']),
      }))

    maps.append(RelationshipMap(
      relname='enclosures',
      modname='ZenPacks.community.IBMV7000.Enclosure',
      objmaps=enclosures
    ))


     # parsing data for lsenclosurebattery command
     # results contents..
     #enclosure_id:battery_id:status:charging_status:recondition_needed:percent_charged:end_of_life_warning
     #2:1:online:idle:no:100:no
     #2:2:online:idle:no:99:no

    lsenclosurebattery = Utils.cmdParser(data[3],'battery_id','BAT_ID')
    batteries = []
    for key,item in lsenclosurebattery.iteritems():
      batteries.append(ObjectMap(data={
        'id'                          : self.prepId(key),
        'title'                       : key,
        'battery_status'              : item['status'],
        'charging_status'             : item['charging_status'],
        'recondition_needed'          : item['recondition_needed'],
        'percent_charged'             : int(item['percent_charged']),
        'end_of_life_warning'         : item['end_of_life_warning'],
       

      }))

    maps.append(RelationshipMap(
      relname='batteries',
      modname='ZenPacks.community.IBMV7000.Battery',
      objmaps=batteries
    ))

    
    return maps

  



