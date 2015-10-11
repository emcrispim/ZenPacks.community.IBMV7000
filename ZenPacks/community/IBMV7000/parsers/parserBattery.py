##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 September, 2015
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################

from Products.ZenRRD.CommandParser import CommandParser
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
from ZenPacks.community.IBMV7000 import Utils
from transaction import commit

class parserBattery(CommandParser):

  def processResults(self, cmd, result):
    
      
    """
    Process the results for command "lsenclosurebattery -delim :".
    """
    datapointMap = dict([(dp.id, dp) for dp in cmd.points])
    devname = cmd.deviceConfig.device
    # returned from datasource component field with ${here/id}
    componentid = cmd.component

    rresult = Utils.cmdParser(cmd.result.output,'battery_id','BAT_ID')

    # specific component device
    rresult = rresult[componentid] 

    
    # recondition_needed raise event
    if rresult['recondition_needed']!='no': 
      result.events.append(Utils.getEvent(cmd,"Battery recondition needed",clear=False))

    #Battery end of life warning raise event
    if rresult['end_of_life_warning']!='no': 
      result.events.append(Utils.getEvent(cmd,"Battery end of life warning",clear=False))

    
    # update current component
    # zencommand does not have direct access to the model and components but
    # maybe theres another way to do this
    
    scriptbase = ZenScriptBase(noopts = 1, connect = True)
    device = scriptbase.findDevice(devname)
    component = device.batteries.findObjectsById(componentid)[0]
    component.battery_status=rresult['status']
    component.charging_status=rresult['charging_status']
    component.recondition_needed=rresult['recondition_needed']
    component.percent_charged=int(rresult['percent_charged'])
    component.end_of_life_warning=rresult['end_of_life_warning']
    commit()



