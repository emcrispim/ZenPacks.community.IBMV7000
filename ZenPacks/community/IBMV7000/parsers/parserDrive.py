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

class parserDrive(CommandParser):

  def processResults(self, cmd, result):
    """
    Process the results for command "lsdrive -delim :".
    """
    update = False
    datapointMap = dict([(dp.id, dp) for dp in cmd.points])
    devname = cmd.deviceConfig.device

    # returned from datasource component field with ${here/id}
    componentid = cmd.component

    rresult = Utils.cmdParser(cmd.result.output,'id','DRIVE_ID')
    # specific component device
    rresult = rresult[componentid] 


    # drive status raise event
    if rresult['status']!='online': 
      result.events.append(Utils.getEvent(cmd,"Drive status not online",clear=False))
      update = True

    # drive error sequence number
    if rresult['error_sequence_number']!='': 
      result.events.append(Utils.getEvent(cmd,"Drive error sequence number: "+rresult['error_sequence_number'],clear=False))
      update = True
  
    # update current component if needed
    if update:
      scriptbase = ZenScriptBase(noopts = 1, connect = True)
      device = scriptbase.findDevice(devname)
      component = device.drives.findObjectsById(componentid)[0]
      component.drive_status=rresult['status']
      component.error_sequence_number=rresult['error_sequence_number']
      commit()




 