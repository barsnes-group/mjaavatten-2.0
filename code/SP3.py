#!/usr/bin/env python
# coding: utf-8

# In[2]:


from opentrons import protocol_api


# In[3]:


#metadata
metadata = {
    'protocolName': 'SP3',
    'author': 'Henrik S',
    'description': 'SP3 protocol for PROBE',
    'apiLevel': '2.11'
    }

def run(protocol: protocol_api.ProtocolContext):
    
    # labware, tipracks
    tiprack10 = protocol.load_labware('opentrons_96_tiprack_10ul', '11')
    tiprack300 = protocol.load_labware('opentrons_96_tiprack_300ul', '8')
    
    # modules and their plates
    mag_mod = protocol.load_module('magnetic module', '10')
    mag_plate = mag_mod.load_labware('eppendorf_96_deepwellplate_500ul')
    
    temp_mod = protocol.load_module('temperature module', '7')
    temp_plate = temp_mod.load_labware('eppendorf_96_deepwellplate_500ul')
    
    # pipettes
    p300 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack300])
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack10])

    # wells
    reservoir = protocol.load_labware('agilent_1_reservoir_290ml', 2)    
    
    tuberack = protocol.load_labware('opentrons_10_tuberack_nest_4x50ml_6x15ml_conical', '3')
    snapcap = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 6)
    
    
    
    #Reduction and alkylation
    
    # 1.
    #Add 2-3µl mM DTT
    p20.distribute(
        3, 
        tuberack['A3'], #insert true source here
        temp_plate.wells(),
        #touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
        )
    
    #Incubate
    
    temp_mod.set_temperature(60)
    protocol.delay(minutes = 20, msg = 'Incubating 20 minutes at 60°C for reduction')
    temp_mod.set_temperature(22)
    
    
    #2. 
    #Add 3-4µl 200 mM IAA
    p20.distribute(
        4, 
        tuberack['A3'], #insert true source here
        temp_plate.wells().bottom(5),
        #touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
        )
    
    #Incubate
    temp_mod.set_temperature(22)
    protocol.delay(minutes = 60, msg = 'Incubate at RT(22°C) for 1 hour for alkylation')
    
    
    
    #Protein binding, cleanup and digestion

    #1. 
    #Add SP3 solution
    p20.distribute(
        2, 
        tuberack['A3'], #insert true source here
        temp_plate.wells().bottom(5),
        #touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
        )
    
    
    #2. 
    #Add 100% Ethanol
    p20.distribute(
        10, 
        tuberack['A3'], #insert true source here
        mag_plate.wells().top(-2),
        #touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
        )
    
    #3. 
    #Move to ThermoMixer
    protocol.pause('Incubate in thermomixer at 24°C for 7 min at 1000 rpm')
    
    #4.
    #Incubate on magnet to migrate the beads
    mag_mod.engage(10)
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
        tuberack['A3'], #insert true source here
        mag_plate.wells().top(-2),
        #touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
        )
    
    #Incubate on magnet to migrate the beads
    mag_mod.engage(10)
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
        tuberack['A3'], #insert true source here
        mag_plate.wells().top(-2),
        #touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
        )
    
    #Incubate on magnet to migrate the beads
    mag_mod.engage(10)
    protocol.delay(minutes = 5, msg = 'Incubating on magnet for 5 minutes')
    mag_mod.disengage()
    
    #Remove contaminants 
    p300.transfer(
        180,
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3']],
        trashcontainer['A2'].top(),
        blow_out = False
        )
    
    
    #Third time
    #Add 180ul of 80% ethanol SP3 rinse solution
    p300.transfer(
        180, 
        tuberack['A3'], #insert true source here
        mag_plate.wells().top(-2),
        #touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
        )
    
    #Incubate on magnet to migrate the beads
    mag_mod.engage(10)
    protocol.delay(minutes = 5, msg = 'Incubating on magnet for 5 minutes')
    mag_mod.disengage()
    
    #Remove contaminants 
    p300.transfer(
        180,
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3']],
        trashcontainer['A2'].top(),
        blow_out = False
        )
    
    ####################################################################
    
    #11. 
    #Add 50ul of digestion solution
    p300.transfer(
        50, 
        tuberack['A3'], #insert true source here
        mag_plate.wells().top(-2),
        #touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
        )
    
    
    #12. and 13. 
    #Pause for pushing beads, and incubate overnight(37C and 1000 rpm)
    protocol.pause('Using a micropipette with a 200-μL tip, gently push the beads that '
                   'are not covered by liquid along the tube wall into the digestion solution. '
                   'Thereafter, sonicate in water bath and incubate for 12-18 hours in ThermoMixer')
    
    
    
    
    #Peptide extraction
    
    #14.
    #First, centrifuge at 13 000 rpm at 24°C for 3 minutes.
    
    
    #15. 
    #Engage magnet until beads have settled on tube wall
    mag_mod.engage(10)
    protocol.delay(minutes = 5, msg = 'Incubating on magnet for 5 minutes')
    mag_mod.disengage()
    
    #Remove contaminants 
    p300.transfer(
        180,
        [mag_plate.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3']],
        trashcontainer['A2'].top(),
        blow_out = False
        )
    
    
    #16. 
    #Add 50ul of 0.5M NaCL pipette-mix
    p300.transfer(
        50, 
        tuberack['A3'], #insert true source here
        mag_plate.wells().top(-2),
        #touch_tip = True,
        blow_out = True,
        blowout_location = 'source well',
        trash = False
        )
    
    
    #17. 
    #Sonicate in water bath
    protocol.pause('Sonicate for 30s in a water bath, and centrifuge the tube at 13 000 rpm at 24°C for 3 min')
    
    
    #18. 
    #Engage magnet until beads have settled on tube wall
    mag_mod.engage(10)
    protocol.delay(minutes = 5, msg = 'Incubating on magnet for 5 minutes')
    mag_mod.disengage()
    
    
    
    


# In[ ]:





# In[ ]:




