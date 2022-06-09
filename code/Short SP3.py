#!/usr/bin/env python
# coding: utf-8

# In[1]:


from opentrons import protocol_api


# In[2]:


#metadata
metadata = {
    'protocolName': 'SP3',
    'author': 'Henrik S',
    'description': 'Short SP3 test protocol for PROBE',
    'apiLevel': '2.11'
    }

def run(protocol: protocol_api.ProtocolContext):
    
    # labware, tipracks
    tiprack10 = protocol.load_labware('opentrons_96_tiprack_10ul', '9')
    tiprack300 = protocol.load_labware('opentrons_96_tiprack_300ul', '8')
    tiprack2 = protocol.load_labware('opentrons_96_tiprack_300ul', '11')
    
    trashcontainer = protocol.load_labware('eppendorf_96_deepwellplate_500ul', 1)
    
    # modules
    mag_mod = protocol.load_module('magnetic module', '10')
    mag_plate = mag_mod.load_labware('eppendorf_96_deepwellplate_500ul')
    
    temp_mod = protocol.load_module('temperature module', '7')
    temp_plate = temp_mod.load_labware('eppendorf_96_deepwellplate_500ul')
    
    # pipettes
    p300 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack300, tiprack2])
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack10])

    # wells
    eppendorf_deepwell = protocol.load_labware('eppendorf_96_deepwellplate_500ul', 4)
    reservoir2 = protocol.load_labware('agilent_1_reservoir_290ml', 2)
    reservoir3 = protocol.load_labware('agilent_1_reservoir_290ml', 3)
    
    
    #tuberack = protocol.load_labware('opentrons_10_tuberack_nest_4x50ml_6x15ml_conical', '3')
    #snapcap = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 6)
    
    
    
    #Protein binding, cleanup and digestion
    '''
    #1. 
    #Add SP3(100% ethanol) solution
    p20.transfer(
        2, 
        tuberack['A3'], #insert true source here
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3']],
        #mag_plate.wells().bottom(5),
        mix_after = (5, 15),
        #touch_tip = True,
        blow_out = False,
        blowout_location = 'source well'
        )
    '''
    
    #2. 
    #Add 100% Ethanol
    p300.transfer(
        130, 
        reservoir3.wells(), #insert true source here
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3']],
        #mag_plate.wells().top(-2),
        mix_after = (5, 100),
        new_tip = 'always',
        blow_out = False,
        blowout_location = 'source well'
        )
    
    #3. 
    #Move to ThermoMixer
    protocol.pause('Incubate in thermomixer at 24°C for 7 min at 1000 rpm, then move to magnet')
    
    
    #4.
    #Incubate on magnet to migrate the beads
    mag_mod.engage(20)
    protocol.delay(minutes = 5, msg = 'Incubating on magnet for 5 minutes')
    mag_mod.disengage()
    
    
    #5
    #Remove contaminants
    p300.transfer(
        180,
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3'].bottom()],
        trashcontainer['A1'].top(),
        blow_out = False
        )
    
    
    ################################## Steps 6-10 ##################################
    
    #First time
    #Add 180ul of 80% ethanol SP3 rinse solution
    p300.transfer(
        180, 
        reservoir2.wells(), #insert true source here
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3']],
        #mag_plate.wells().top(-2),
        mix_after = (5, 100),
        new_tip = 'always',
        blow_out = False,
        blowout_location = 'source well'
        )
    
    #Incubate on magnet to migrate the beads
    mag_mod.engage(20)
    protocol.delay(minutes = 5, msg = 'Incubating on magnet for 5 minutes')
    mag_mod.disengage()
    
    #Remove contaminants 
    p300.transfer(
        180,
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3']],
        trashcontainer['A2'].top(),
        blow_out = False
        )
    
    #Second time
    #Add 180ul of 80% ethanol SP3 rinse solution
    p300.transfer(
        180, 
        reservoir2.wells(), #insert true source here
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3']],
        #mag_plate.wells().top(-2),
        mix_after = (5, 100),
        new_tip = 'always',
        blow_out = False,
        blowout_location = 'source well'
        )
    
    
    #Incubate on magnet to migrate the beads
    mag_mod.engage(20)
    protocol.delay(minutes = 5, msg = 'Incubating on magnet for 5 minutes')
    mag_mod.disengage()
    
    #Remove contaminants
    p300.transfer(
        180,
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3'].bottom()],
        trashcontainer['A3'].top(),
        blow_out = False
        )
    
    
    #Add 180ul of 80% ethanol SP3 rinse solution
    p300.transfer(
        180, 
        reservoir2.wells(), #insert true source here
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3']],
        #mag_plate.wells().top(-2),
        mix_after = (5, 100),
        new_tip = 'always',
        blow_out = False,
        blowout_location = 'source well'
        )
    
    #Incubate on magnet to migrate the beads
    mag_mod.engage(20)
    protocol.delay(minutes = 5, msg = 'Incubating on magnet for 5 minutes')
    mag_mod.disengage()
    
    #Remove contaminants 
    p300.transfer(
        180,
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3'].bottom()],
        trashcontainer['A4'].top(),
        blow_out = False
        )
    
    ####################################################################
    '''
    #11. 
    #Add 50ul of digestion solution
    p300.transfer(
        50, 
        tuberack['A3'], #insert true source here
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3']],
        #mag_plate.wells().top(-2),
        blow_out = False,
        blowout_location = 'source well'
        )
    '''
    
    #12. and 13. 
    #Pause for pushing beads, and incubate overnight(37C and 1000 rpm)
    protocol.pause('Using a micropipette with a 200-μL tip, gently push the beads that '
                   'are not covered by liquid along the tube wall into the digestion solution. '
                   'Thereafter, sonicate in water bath and incubate for 12-18 hours in ThermoMixer')


# In[ ]:




