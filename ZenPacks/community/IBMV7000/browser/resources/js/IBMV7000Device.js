//#######################################################################
// Author:               Eduardo Crispim, emcrispim@gmail.com
// Date:                 September, 2015
// 
// This program is free software; you can redistribute it and/or modify it
// under the terms of the GNU General Public License version 2 or (at your
// option) any later version as published by the Free Software Foundation.
//
//#######################################################################



(function(){
  var ZC = Ext.ns('Zenoss.component');
  ZC.registerName(
    'IBMV7000Enclosure',
    _t('Enclosure'),
    _t('Enclosures')
  );

  ZC.registerName(
    'IBMV7000Battery',
    _t('Battery'),
    _t('Batteries')
  );

  ZC.registerName(
    'IBMV7000Drive',
    _t('Drive'),
    _t('Drives')
  );

  ZC.IBMV7000EnclosurePanel = Ext.extend(ZC.ComponentGridPanel,{
    constructor: function(config){
      config = Ext.applyIf(config||{}, {
        componentType: 'IBMV7000Enclosure',
        autoExpandColumn: 'name',
        sortInfo: {
          field: 'name',
          direction: 'DESC'
        },
        fields: [
          {name: 'uid'},
          {name: 'name'},
          {name: 'status'},
          {name: 'severity'},
          {name: 'usesMonitorAttribute'},
          {name: 'monitor'},
          {name: 'monitored'},
          {name: 'locking'},
          {name: 'enclosure_status'},
          {name: 'enclosure_type'},
          {name: 'product_MTM'},
          {name: 'serial_number'},
          {name: 'total_canisters',type:'int'},
          {name: 'online_canisters',type:'int'},
          {name: 'total_PSUs',type:'int'},
          {name: 'online_PSUs',type:'int'},
          {name: 'drive_slots',type:'int'},
          {name: 'total_fan_modules',type:'int'},
          {name: 'online_fan_modules',type:'int'}

        ],
        columns: [
          {
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
          },{
            id: 'name',
            dataIndex: 'name',
            header: _t('ID'),
            sortable: true
          },{
            id: 'enclosure_status',
            dataIndex: 'enclosure_status',
            header: _t('Status'),
            sortable: true,
            width:70
          },{  
            id: 'enclosure_type',
            dataIndex: 'enclosure_type',
            header: _t('Type'),
            sortable: true,
            width:70
          },{
            id: 'product_MTM',
            dataIndex: 'product_MTM',
            header: _t('Product MTM'),
            sortable: true,
            width:90
          },{
            id: 'serial_number',
            dataIndex: 'serial_number',
            header: _t('Serial Number'),
            sortable: true,
            width:90
          },{
            id: 'total_canisters',
            dataIndex: 'total_canisters',
            header: _t('#Canisters'),
            sortable: true,
            width:70
          },{
            id: 'online_canisters',
            dataIndex: 'online_canisters',
            header: _t('Online Canisters'),
            sortable: true,
            width:100
          },{
            id: 'total_PSUs',
            dataIndex: 'total_PSUs',
            header: _t('#PSUs'),
            sortable: true,
            width:80
          },{
            id: 'online_PSUs',
            dataIndex: 'online_PSUs',
            header: _t('#Online PSUs'),
            sortable: true,
            width:100
          },{
            id: 'total_fan_modules',
            dataIndex: 'total_fan_modules',
            header: _t('#Fan modules'),
            sortable: true,
            width:100
          },{
            id: 'online_fan_modules',
            dataIndex: 'online_fan_modules',
            header: _t('Online Fan modules'),
            sortable: true,
            width:100

          },{
            id: 'monitored',
            dataIndex: 'monitored',
            header: _t('Monitored'),
            renderer: Zenoss.render.checkbox,
            width:70,
            sortable: true
          },{
            id: 'locking',
            dataIndex: 'locking',
            header: _t('Locking'),
            renderer: Zenoss.render.locking_icons,
            width: 65
          }
        ]
      });

      ZC.IBMV7000EnclosurePanel.superclass.constructor.call(this,config);
    }
  });

  Ext.reg('IBMV7000EnclosurePanel',ZC.IBMV7000EnclosurePanel);




  ZC.IBMV7000BatteryPanel = Ext.extend(ZC.ComponentGridPanel,{
    constructor: function(config){
      config = Ext.applyIf(config||{}, {
        componentType: 'IBMV7000Battery',
        autoExpandColumn: 'name',
        sortInfo: {
          field: 'name',
          direction: 'DESC'
        },
        fields: [
          {name: 'uid'},
          {name: 'name'},
          {name: 'status'},
          {name: 'severity'},
          {name: 'usesMonitorAttribute'},
          {name: 'monitor'},
          {name: 'monitored'},
          {name: 'locking'},
          {name: 'enclosure_ID'},
          {name: 'battery_status'},
          {name: 'charging_status'},
          {name: 'recondition_needed'},
          {name: 'percent_charged',type:'int'},
          {name: 'end_of_life_warning'}
        ],
        columns: [
          {
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
          },{
            id: 'name',
            dataIndex: 'name',
            header: _t('ID'),
            sortable: true
          },{
            id: 'enclosure_ID',
            dataIndex: 'enclosure_ID',
            header: _t('enclosure ID'),
            sortable: true,
            width:80
          },{  
            id: 'battery_status',
            dataIndex: 'battery_status',
            header: _t('Status'),
            sortable: true,
            width:80
          },{
            id: 'charging_status',
            dataIndex: 'charging_status',
            header: _t('Charging'),
            sortable: true,
            width:90
          },{
            id: 'recondition_needed',
            dataIndex: 'recondition_needed',
            header: _t('Recondition needed'),
            sortable: true,
            width:120
          },{
            id: 'percent_charged',
            dataIndex: 'percent_charged',
            header: _t('Percent charged'),
            sortable: true,
            width:90
          },{
            id: 'end_of_life_warning',
            dataIndex: 'end_of_life_warning',
            header: _t('End of life Warning'),
            sortable: true,
            width:110
          },{
            id: 'monitored',
            dataIndex: 'monitored',
            header: _t('Monitored'),
            renderer: Zenoss.render.checkbox,
            width:70,
            sortable: true
          },{
            id: 'locking',
            dataIndex: 'locking',
            header: _t('Locking'),
            renderer: Zenoss.render.locking_icons,
            width: 65
          }
        ]
      });

      ZC.IBMV7000BatteryPanel.superclass.constructor.call(this,config);
    }
  });

  Ext.reg('IBMV7000BatteryPanel',ZC.IBMV7000BatteryPanel);



   ZC.IBMV7000DrivePanel = Ext.extend(ZC.ComponentGridPanel,{
    constructor: function(config){
      config = Ext.applyIf(config||{}, {
        componentType: 'IBMV7000Drive',
        autoExpandColumn: 'name',
        sortInfo: {
          field: 'name',
          direction: 'DESC'
        },
        fields: [
          {name: 'uid'},
          {name: 'name'},
          {name: 'status'},
          {name: 'severity'},
          {name: 'usesMonitorAttribute'},
          {name: 'monitor'},
          {name: 'monitored'},
          {name: 'locking'},
          {name: 'drive_status'},
          {name: 'error_sequence_number'},
          {name: 'use'},
          {name: 'tech_type'},
          {name: 'capacity'},
          {name: 'enclosure_id',type:'int'},
          {name: 'slot_id'}
        ],
        columns: [
          {
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
          },{
            id: 'name',
            dataIndex: 'name',
            header: _t('Drive ID'),
            sortable: true
          },{
            id: 'drive_status',
            dataIndex: 'drive_status',
            header: _t('Drive status'),
            sortable: true,
            width:80
          },{  
            id: 'error_sequence_number',
            dataIndex: 'error_sequence_number',
            header: _t('Error sequence number'),
            sortable: true,
            width:130
          },{  
            id: 'use',
            dataIndex: 'use',
            header: _t('Use'),
            sortable: true,
            width:80
          },{
            id: 'tech_type',
            dataIndex: 'tech_type',
            header: _t('Tech type'),
            sortable: true,
            width:90
          },{
            id: 'capacity',
            dataIndex: 'capacity',
            header: _t('Capacity'),
            sortable: true,
            width:120
          },{
            id: 'enclosure_id',
            dataIndex: 'enclosure_id',
            header: _t('Enclosure ID'),
            sortable: true,
            width:90
          },{
            id: 'slot_id',
            dataIndex: 'slot_id',
            header: _t('Slot ID'),
            sortable: true,
            width:110
          },{
            id: 'monitored',
            dataIndex: 'monitored',
            header: _t('Monitored'),
            renderer: Zenoss.render.checkbox,
            width:70,
            sortable: true
          },{
            id: 'locking',
            dataIndex: 'locking',
            header: _t('Locking'),
            renderer: Zenoss.render.locking_icons,
            width: 65
          }
        ]
      });

      ZC.IBMV7000DrivePanel.superclass.constructor.call(this,config);
    }
  });

  Ext.reg('IBMV7000DrivePanel',ZC.IBMV7000DrivePanel);



  Ext.onReady(function(){
    var DEVICE_OVERVIEW_ID = 'deviceoverviewpanel_summary';
    Ext.ComponentMgr.onAvailable(DEVICE_OVERVIEW_ID,function(){
      var overview = Ext.getCmp(DEVICE_OVERVIEW_ID);
      overview.removeField('memory');
      overview.addField({
        name:'storage_capacity',
        fieldLabel: _t('Capacity (Used/Total)')
      });
    });



  }); //Ext.onReady

})(); 