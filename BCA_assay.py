#!/usr/bin/env python
# coding: utf-8

# In[4]:


from opentrons import protocol_api

#metadata
metadata = {
    'protocolName': 'BCA assay',
    'author': 'Henrik S',
    'description': 'BCA protein assay',
    'apiLevel': '2.11'
    }

def run(protocol: protocol_api.ProtocolContext):
    
    # labware, tipracks
    #tiprack10 = protocol.load_labware('opentrons_96_tiprack_10ul', '7')
    tiprack300 = protocol.load_labware('opentrons_96_tiprack_300ul', '8')
    
    # pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack300])
    #p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack10])

    
    # wells
    fischer_well = protocol.load_labware('fischer_96_wellplate_330ul', '4')
    
    
    tuberack = protocol.load_labware('opentrons_10_tuberack_nest_4x50ml_6x15ml_conical', '3')
    snapcap = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '6')


    # commands
    
    
    p300.flow_rate.blow_out = 100
    
    
    #Add water to well A1-A6 and B1-B6

    p300.distribute(
        [10, 8, 6, 4, 2, 0, 10, 8, 6, 4, 2, 0], 
        tuberack['A3'],   
        [fischer_well.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 
                                                                  'B1', 'B2', 'B3', 'B4', 'B5', 'B6']], 
        touch_tip = True,
        blow_out = True,   
        blowout_location= 'source well',
        trash = False      
    )
    
    
    #Add water to well B1-B6
    '''
    p300.distribute(
        [10, 8, 6, 4, 2, 0], 
        tuberack['A3'],
        [fischer_well.wells_by_name()[well_name] for well_name in ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']],
        touch_tip = True,
        blow_out = True,
        blowout_location= 'source well',
        trash = False
    )
    '''

    #Add Bovine IG/BSA to well A1-A6 and B1-B6

    p300.distribute(
        [0, 2, 4, 6, 8, 10, 0, 2, 4, 6, 8, 10],
        snapcap['D1'],
        [fischer_well.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 
                                                                   'B1', 'B2', 'B3', 'B4', 'B5', 'B6']],
        touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = True
    )
    
    
    #Add Bovine IG/BSA to well B1-B6
    '''
    p300.distribute(
        [0, 2, 4, 6, 8, 10],
        snapcap['D1'],
        [fischer_well.wells_by_name()[well_name] for well_name in ['B1, 'B2', 'B3', 'B4', 'B5', 'B6']],
        touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = True
    )'''
    
    '''
    #Add Lysis buffer to  well A1-A6
    
    p300.distribute(
        5,
        tuberack['A3'],
        [fischer_well.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']],
        touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
    )
    '''
    
    #Add Lysis buffer to well A1-A6 and B1-B6
    
    p300.distribute(
        5,
        tuberack['A3'],
        [fischer_well.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 
                                                                   'B1', 'B2', 'B3', 'B4', 'B5', 'B6']],
        touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
    )
    
           
    
    #Add BCA to standard curve wells
    
    p300.distribute(
        200, 
        tuberack['B3'],
        [fischer_well.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 
                                                                   'B1', 'B2', 'B3', 'B4', 'B5', 'B6']],
        touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = True
        )
    
    
    
    
    
    
    
    '''
    #Add water to every well
    
    p300.distribute(
        10, 
        tuberack['A3'],
        fischer_well.wells(),
        touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
        )
    
    
    
    
    #Add BCA to every well
    
    p300.distribute(
        200, 
        tuberack['A3'],
        fischer_well.wells(),
        touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
        )
    '''


# In[ ]:





# In[ ]:




