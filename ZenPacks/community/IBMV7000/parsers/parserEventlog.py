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
from ZenPacks.community.IBMV7000 import Utils

class parserEventlog(CommandParser):

  def processResults(self, cmd, result):
    """
    Process the results for command "lseventlog -message no -fixed no -delim :".
    """
    
    devname = cmd.deviceConfig.device

    rresult = Utils.cmdParser(cmd.result.output,'event_id','EVT_ID')
  
    for key,evt in rresult.iteritems():
      result.events.append(Utils.getEvent(cmd,key+':'+evt['description'],clear=False))


  

