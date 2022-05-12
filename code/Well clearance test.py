#!/usr/bin/env python
# coding: utf-8

# In[5]:


from opentrons import protocol_api

#metadata
metadata = {
    'protocolName': 'Clearance test',
    'author': 'Henrik S',
    'description': 'Well bottom clearance testing',
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
    
    
    test_tube = protocol.load_labware('opentrons_10_tuberack_nest_4x50ml_6x15ml_conical', '3')
    #snapcap = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '6')

    
    #p300.well_bottom_clearance.aspirate = 50
    p300.default_speed = 100
    
    '''
    p300.distribute(
        20, 
        test_tube['A1'],   
        [fischer_well.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3', 'A4', 'A5']], 
        touch_tip = True,
        blow_out = True,   
        blowout_location= 'source well',
        trash = False      
    )
    '''

    p300.distribute(
        20, 
        test_tube['B3'],   
        [fischer_well.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3', 'A4', 'A5']], 
        touch_tip = True,
        blow_out = True,   
        blowout_location= 'source well',
        trash = False      
    )


# In[ ]:




