#!/usr/bin/env python
# coding: utf-8

# In[7]:


from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'My Protocol',
    'author': 'Henrik S',
    'description': 'Simple protocol to get started using OT2',
    'apiLevel': '2.11'
    }

def run(protocol: protocol_api.ProtocolContext):
    
    # labware
    tiprack10 = protocol.load_labware('opentrons_96_tiprack_10ul', '3')
    tiprack300 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    #test_tube = protocol.load_labware('opentrons_10_tuberack_nest_4x50ml_6x15ml_conical', '5')
    snapcap = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '4')
    

    # pipettes
    left_pipette = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack300])
    right_pipette = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack10, snapcap])

    # commands
    left_pipette.pick_up_tip()
    left_pipette.drop_tip()
    right_pipette.pick_up_tip()
    right_pipette.drop_tip()
    right_pipette.pick_up_tip()
    right_pipette.drop_tip()


# In[ ]:




