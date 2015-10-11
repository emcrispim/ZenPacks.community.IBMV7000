
##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 September, 2015
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################


# Utils functions



# This function provides utils for parsing data in the form
# <field1>:<field2>: ... :<fieldn>\n
# <value11>:<value12>: ... :<field1X>\n
# <value21>:<value22>: ... :<fieldYX>\n
# 
# to a dictionary
# {"fieldId":{"fieldId":"valueId","field1":"value1"},...
# {"fieldId":{"fieldId":"valueId","field2":"value2"},...
# }



def cmdParser(data,fieldId,idPrefix='',separator=':'):
  result = {}

  fields=data.split('\n')[0].split(':')
  fieldIdx=fields.index(fieldId)

  for line in data.split('\n')[1:]:
    if len(line)>1:
      inline={}
      lline = line.split(separator)
      for i in range(len(lline)):
        inline[fields[i]] = lline[i]
      result[idPrefix+lline[fieldIdx]]=inline

  return result


# Return a dictionary structure for events
def getEvent(cmd,summary,message=None,clear=False):
    event = dict(
      summary=summary,
      component=cmd.component,
    )

    if message:
      event['message'] = message

    if clear:
      event['severity'] = 0
    else:
      event['severity'] = cmd.severity

    return event











