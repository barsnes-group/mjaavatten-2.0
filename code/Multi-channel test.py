#!/usr/bin/env python
# coding: utf-8

# In[1]:


from opentrons import protocol_api


# In[2]:


#metadata
metadata = {
    'protocolName': 'Multi Channel Pipette test',
    'author': 'Henrik S',
    'description': 'MCP Test',
    'apiLevel': '2.11'
    }

def run(protocol: protocol_api.ProtocolContext):
    
    # labware, tipracks
    tiprack10 = protocol.load_labware('opentrons_96_tiprack_10ul', 11)
    tiprack300 = protocol.load_labware('opentrons_96_tiprack_300ul', 8)
    
    # modules
    mag_mod = protocol.load_module('magnetic module', 10)
    mag_plate = mag_mod.load_labware('eppendorf_96_deepwellplate_500ul')
    
    temp_mod = protocol.load_module('temperature module', 4)
    temp_plate = temp_mod.load_labware('eppendorf_96_deepwellplate_500ul')
    
    # pipettes
    p300 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack300])
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack10])

    # wells
    reservoir = protocol.load_labware('agilent_1_reservoir_290ml', 2)
    
    
    tuberack = protocol.load_labware('opentrons_10_tuberack_nest_4x50ml_6x15ml_conical', 3)
    snapcap = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 6)
    
    
    p300.transfer(
        100, 
        reservoir.wells(), #insert true source here
        temp_plate.wells(),
        mix_after = (2, 50),
        #touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
        )
  


# In[ ]:




