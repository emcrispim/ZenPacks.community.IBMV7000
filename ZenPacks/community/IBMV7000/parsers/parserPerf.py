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
from transaction import commit

class parserPerf(CommandParser):

  def processResults(self, cmd, result):
    
      
    """
     Process the results for command "lssystemstats".
      The lssystemstats command with -history option provides the last 300 values
      this will return the mean values to each datapoint 
    """

    datapointMap = dict([(dp.id, dp) for dp in cmd.points])
    

    # datapoint values
    dpv={}

    for lines in  cmd.result.output.splitlines()[1:]:
      values = lines.split(':')
      dp = values[1]
      v = int(values[2])

      """  
        if there are already  values in the dictionary then it will sum and count,
        later it will return the mean values 
      """
      if dpv.has_key(dp):
        dpv[dp]['value']+=v
        dpv[dp]['count']+=1
      else:
        dpv[dp]={'value':v,'count':1}
 
    for k in datapointMap.keys():
      result.values.append((datapointMap[k],int(dpv[k]['value']/dpv[k]['count'])))
    
    


   
        



  

