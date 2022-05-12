#!/usr/bin/env python
# coding: utf-8

# In[9]:


from opentrons import protocol_api

#metadata
metadata = {
    'protocolName': 'Easy Liquid Transfer',
    'author': 'Henrik S',
    'description': 'Simple protocol for liquid transfer using OT2',
    'apiLevel': '2.11'
    }

def run(protocol: protocol_api.ProtocolContext):
    
    # labware
    tiprack10 = protocol.load_labware('opentrons_96_tiprack_10ul', '3')
    tiprack300 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    
    test_tube = protocol.load_labware('opentrons_10_tuberack_nest_4x50ml_6x15ml_conical', '5')
    #snapcap = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '4')
    snapcap = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '4')

    # pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack300])
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack10])

    # commands
    p300.pick_up_tip()
    
    p300.flow_rate.aspirate = 20
    p300.flow_rate.dispense = 20
    p300.well_bottom_clearance.aspirate = 5
    p300.well_bottom_clearance.dispense = 5
    
    for well in snapcap.rows()[:2]:
        p300.aspirate(100, well)
        p300.air_gap(50)
    
    p300.dispense(300, test_tube['A3'])
    p300.return_tip()
    
    
    p20.pick_up_tip()
    p20.well_bottom_clearance.aspirate = 5
    p20.well_bottom_clearance.dispense = 5
    
    p20.aspirate(10, snapcap['B1'])
    p20.dispense(10, test_tube['A3'])
    p20.return_tip()


# In[ ]:




