"""List of all Dungeon and Monster Sets with their bonus effects"""

from .dungeon_set import MonsterSet, DungeonSet

MONSTER_SETS = {}
DUNGEON_SETS = {}

MONSTER_SETS["balorgh"] = MonsterSet(
    "Balorgh", "Adds 129 Weapon Damage, Adds 129 Spell Damage",
    "When you use an Ultimate ability, you gain Weapon Damage and Spell Damage for 10 seconds equal to twice the amount of total Ultimate consumed."
)
MONSTER_SETS["bloodspawn"] = MonsterSet(
    "Bloodspawn", "Adds 129 Stamina Recovery",
    "When you take damage, you have a 6%% chance to generate 14 Ultimate and increase your Physical Resistance and Spell Resistance by 6450 for 6 seconds. This effect can occur once every 6 seconds."
)
MONSTER_SETS["chokethorn"] = MonsterSet(
    "Chokethorn", "Adds 129 Magicka Recovery",
    "When you use a heal ability, you have a 15%% chance to summon a strangler sapling that heals you or an ally for 19565 Health over 4 seconds. This effect can occur once every 10 seconds."
)
MONSTER_SETS["domihaus"] = MonsterSet(
    "Domihaus", "Adds 1096 Maximum Stamina, Adds 1096 Maximum Magicka",
    "When you deal damage, you have a 15%% chance to create either a ring of fire or ring of molten earth around you for 10 seconds, which deals 1000 Flame Damage or 1000 Physical Damage every 1 second. Standing within the ring grants you 200 Spell Damage or 200 Weapon Damage. This effect can occur once every 15 seconds."
)
MONSTER_SETS["earthgore"] = MonsterSet(
    "Earthgore", "Adds 4%% Healing Done",
    "When you heal yourself or an ally that is under 50%% Health, you conjure a pool of quenching blood underneath them, immediately removing all previous enemy placed effects, and healing the lowest Health friendly target in the area for 30000 Health over 6 seconds. This effect can occur once every 35 seconds."
)
MONSTER_SETS["engine guardian"] = MonsterSet(
    "Engine Guardian", "Adds 129 Health Recovery",
    "When you use an ability, you have a 10%% chance to summon a dwemer automation to restore 1204 Health, Stamina, or Magicka to you every 0.5 seconds for 6 seconds. This effect can occur once every 8 seconds."
)
MONSTER_SETS["Grothdarr"] = MonsterSet(
    "Grothdarr", "Adds 1096 Maximum Magicka",
    "When you deal damage, you have a 10%% chance to create lava pools that swirl around you, dealing 1800 Flame Damage to all enemies within 8 meters of you every 1 second for 5 seconds. This effect can occur once every 10 seconds."
)
MONSTER_SETS["grundwulf"] = MonsterSet(
    "Grundwulf", "Adds 833 Weapon Critical, Adds 833 Spell Critical",
    "Whenever you deal critical damage, restore 1000 Magicka or Stamina, whichever maximum is higher. You also gain 500 of the other resource. This effect can occur once every 5 seconds."
)
MONSTER_SETS["iceheart"] = MonsterSet(
    "Iceheart", "Adds 833 Spell Critical",
    "When you deal Critical Damage, you have a 20%% chance to gain a damage shield that absorbs 5000 damage for 6 seconds. While the damage shield holds, you deal 500 Frost Damage to all enemies within 5 meters of you every 1 second. This effect can occur once every 6 seconds."
)
MONSTER_SETS["ilambris"] = MonsterSet(
    "Ilambris", "Adds 1096 Maximum Magicka",
    "When you deal Flame or Shock Damage, you have a 10%% chance to summon a meteor shower of that damage type that deals 1170 Damage to all enemies within 4 meters every 1 second for 5 seconds. Each effect can occur once every 8 seconds."
)
MONSTER_SETS["infernal guardian"] = MonsterSet(
    "Infernal Guardian", "Adds 1096 Maximum Magicka",
    "When you apply a damage shield to yourself or an ally, you have a 50%% chance to lob 3 mortars over 2 seconds at the furthest enemy from you that each deal 5500 Flame Damage to all enemies within 5 meters of the blast area. This effect can occur once every 6 seconds."
)
MONSTER_SETS["kjalnar's nightmare"] = MonsterSet(
    "Kjalnar's Nightmare", "Adds 129 Spell Damage",
    "Dealing damage with a Light Attack puts a stack of Bone on your enemy for 5 seconds. You can only apply 1 stack every 1 second. At 5 stacks, an undodgeable skeletal hand attacks your enemy after 1 second, knocking them into the air and stunning them for 3 seconds, or dealing 14500 Magic Damage if they cannot be stunned. An enemy that has reached 5 stacks cannot gain Bone stacks for 3 seconds."
)
MONSTER_SETS["kra'gh"] = MonsterSet(
    "Kra'gh", "Adds 1487 Physical Penetration",
    "When you deal damage, you have a 10%% chance to spawn dreugh limbs that create shockwaves in front of you dealing 1300 Physical Damage every 0.4 seconds for 1.2 seconds. This effect can occur once every 3 seconds."
)
MONSTER_SETS["lord warden"] = MonsterSet(
    "Lord Warden", "Adds 2975 Armor",
    "When you take damage, you have a 50%% chance to summon a shadow orb for 10 seconds that increases the Physical Resistance and Spell Resistance of you and your allies within 8 meters by 3870. This effect can occur once every 10 seconds."
)
MONSTER_SETS["maarselok"] = MonsterSet(
    "Maarselok", "Adds 1096 Maximum Stamina",
    "When you bash an enemy, you spew a cone of corruption, dealing 8000 Disease Damage to enemies over 4 seconds. This damage is increased by 5%% for each negative effect the enemies have, up to 150%% additional damage. This effect can occur once every 7 seconds."
)
MONSTER_SETS["maw of the infernal"] = MonsterSet(
    "Maw of the Infernal", "Adds 1206 Maximum Health",
    "When you deal damage with a Light or Heavy Attack, you have a 10%% chance to summon a fire breathing Daedroth for 15 seconds. The Daedroth's basic attacks deal 4257 Flame Damage. This effect can occur once every 15 seconds."
)
MONSTER_SETS["mighty chudan"] = MonsterSet(
    "Mighty Chudan", "Adds 2975 Armor",
    "Adds 1206 Maximum Health, Gain Major Resolve at all times, increasing your Physical Resistance and Spell Resistance by 5280."
)
MONSTER_SETS["molag kena"] = MonsterSet(
    "Molag Kena", "Adds 129 Weapon Damage, Adds 129 Spell Damage",
    "When you deal damage with 2 consecutive Light Attacks you trigger Overkill for 6 seconds, which increases your Weapon Damage and Spell Damage by 516 but also increases the cost of your abilities by 8%."
)
MONSTER_SETS["mother ciannait"] = MonsterSet(
    "Mother Ciannait", "Adds 1096 Maximum Magicka",
    "While in combat, casting an ability with a cast time or channeling an ability grants you a damage shield that absorbs 5000 damage for 6 seconds. If the damage shield is broken, you restore 600 Magicka. This effect can occur once every 6 seconds."
)
MONSTER_SETS["nerien'eth"] = MonsterSet(
    "Nerien'eth", "Adds 1206 Maximum Health",
    "When you deal direct damage, you have a 10%% chance to summon a Lich crystal that explodes after 2 seconds, dealing 8800 Magic Damage to all enemies within 4 meters. This effect can occur once every 3 seconds."
)
MONSTER_SETS["nightflame"] = MonsterSet(
    "Nightflame", "Adds 1096 Maximum Magicka",
    "When you heal yourself or an ally, you have a 10%% chance to summon a totem for 6 seconds that heals you and your allies within 5 meters for 2525 Health every 1 second. This effect can occur once every 10 seconds."
)
MONSTER_SETS["pirate skeleton"] = MonsterSet(
    "Pirate Skeleton", "Adds 2975 Armor",
    "When you take damage to your Health, you have a 8%% chance to transform into a skeleton and gain Major Protection and Major Defile for 10 seconds, reducing your damage taken by 30%% but reducing your healing received and Health Recovery by 30%. This effect can occur once every 20 seconds."
)
MONSTER_SETS["scourge harvester"] = MonsterSet(
    "Scourge Harvester", "Adds 1206 Maximum Health",
    "When you take damage, you have a 6%% chance to create a beam that steals 5805 Health over 4 seconds from the attacker. While the beam holds you gain Major Vitality, increasing your healing received by 30%. The beam breaks if the enemy moves further than 8 meters away. This effect can occur once every 6 seconds."
)
MONSTER_SETS["selene"] = MonsterSet(
    "Selene", "Adds 1096 Maximum Stamina",
    "When you deal melee damage, you have a 15%% chance to call on a primal spirit that mauls the closest enemy in front of you after 1.3 seconds for 12000 Physical Damage. This effect can occur once every 4 seconds."
)
MONSTER_SETS["sellistrix"] = MonsterSet(
    "Sellistrix", "Adds 1096 Maximum Stamina",
    "When you deal damage, you have a 10%% chance to create an earthquake under the enemy that erupts after 1.5 seconds, dealing 5030 Physical Damage to all enemies within 4 meters and stunning them for 3 seconds. This effect can occur once every 5.5 seconds."
)
MONSTER_SETS["sentinel of rkugamz"] = MonsterSet(
    "Sentinel of Rkugamz", "Adds 4%% Healing Done",
    "When you heal yourself or an ally, you have a 10%% chance to summon a dwemer spider that heals for 1000 Health and restores 115 Magicka and Stamina to you and your allies within 5 meters every 1 second for 8 seconds. This effect can occur once every 15 seconds."
)
MONSTER_SETS["shadowrend"] = MonsterSet(
    "Shadowrend", "Adds 129 Magicka Recovery",
    "When you take damage, you have a 15%% chance to summon a shadowy Clannfear for 15 seconds. The Clannfear's basic attacks deal 3440 Magic Damage and apply Minor Maim to any enemy hit for 3 seconds, reducing their damage done by 15%. This effect can occur once every 15 seconds."
)
MONSTER_SETS["slimecraw"] = MonsterSet(
    "Slimecraw", "Adds 833 Spell Critical, Adds 833 Weapon Critical",
    "Gain Minor Berserk at all times, increasing your damage done by 8%.")
MONSTER_SETS["spawn of mephala"] = MonsterSet(
    "Spawn of Mephala", "Adds 1096 Maximum Stamina",
    " When you deal damage with a fully-charged Heavy Attack, you create a web for 10 seconds that deals 1100 Poison Damage every 1 second to all enemies within 4 meters and reduces their Movement Speed by 50%. This effect can occur once every 10 seconds."
)
MONSTER_SETS["stonekeeper"] = MonsterSet(
    "Stonekeeper",
    "Adds 548 Maximum Stamina, Adds 548 Maximum Magicka, Adds 603 Maximum Health",
    "When you block an attack, you gain an energy Charge stack, up to one stack per second. When you gain 6 Charges, you release the energy, restoring 5350 Stamina and Magicka, and healing for 5350. After releasing the Charges, you cannot regain new Charges for 14 seconds."
)
MONSTER_SETS["stormfist"] = MonsterSet(
    "Stormfist", "Adds 129 Stamina Recovery",
    "When you deal damage, you have a 10%% chance to create a thunderfist to crush the enemy, dealing 1650 Shock Damage every 1 second for 3 seconds to all enemies within 4 meters and a final 8000 Physical Damage when the fist closes. This effect can occur once every 8 seconds."
)
MONSTER_SETS["swarm mother"] = MonsterSet(
    "Swarm Mother", "Adds 129 Stamina Recovery",
    "When you block an attack from an enemy that is further than 8 meters from you, you spin strands of spider silk to pull the enemy to you. This effect can occur once every 1 second."
)
MONSTER_SETS["symphony of blades"] = MonsterSet(
    "Symphony of Blades", "Adds 4%% Healing Done",
    "When you heal an ally who is under 50%% of their primary resource, grant them Meridia's Favor, which restores 2325 Magicka or Stamina every 1 second for 6 seconds. This effect can occur every 18 seconds. The resource returned is based off the target's highest maximum resource."
)
MONSTER_SETS["troll king"] = MonsterSet(
    "Troll King", "Adds 4%% Healing Done",
    "When you heal yourself or an ally, if they are still below 50%% Health, their Health Recovery is increased by 1548 for 10 seconds."
)
MONSTER_SETS["thurvokun"] = MonsterSet(
    "Thurvokun", "Adds 1206 Maximum Health",
    "When you take damage from a nearby enemy, you summon a growing pool of desecrated bile for 8 seconds. Enemies in the bile take 430 Disease Damage every 1 second and are afflicted with Minor Maim and Minor Defile for 4 seconds, reducing their damage done by 15%% and healing received and Health Recovery by 15%. This effect can occur every 8 seconds."
)
MONSTER_SETS["tremorscale"] = MonsterSet(
    "Tremorscale", "Adds 1096 Maximum Stamina",
    "When you taunt an enemy, you have a 50%% chance to cause a duneripper to burst from the ground beneath them after 1 second, dealing 5850 Physical Damage to all enemies within 4 meters and reducing their Movement Speed by 70%% for 3 seconds. This effect can occur once every 4 seconds."
)
MONSTER_SETS["valkyn skoria"] = MonsterSet(
    "Valkyn Skoria", "Adds 1206 Maximum Health",
    "When you deal damage with a damage over time effect, you have a 8%% chance to summon a meteor that deals 9000 Flame Damage to the target and 4000 Flame Damage to all other enemies within 5 meters. This effect can occur once every 5 seconds."
)
MONSTER_SETS["velidreth"] = MonsterSet(
    "Velidreth", "Adds 129 Weapon Damage",
    "When you deal damage, you have a 20%% chance to spawn 3 disease spores in front of you after 1 second that deal 10320 Disease Damage to the first enemy they hit. This effect can occur once every 9 seconds."
)
MONSTER_SETS["vykosa"] = MonsterSet(
    "Vykosa", "Adds 4%% Healing Taken",
    "When you Bash an enemy you've taunted, you frighten them with a deafening howl, lowering their Weapon Damage and Spell Damage by 20%% for 5 seconds. This effect can occur once every 15 seconds."
)
MONSTER_SETS["zaan"] = MonsterSet(
    "Zaan", "Adds 833 Spell Critical",
    "When you damage a nearby enemy with a Light or Heavy Attack, you have a 20%% chance to create a beam of fire that will connect you to your enemy. The beam deals 3440 Flame Damage every 1 second to your enemy for 5 seconds. Every second, this damage increases by 50%. The beam is broken if the enemy moves 8 meters away from you. This effect can occur every 18 seconds."
)
DUNGEON_SETS["aegis caller"] = DungeonSet("Aegis Caller", "", "", "", "", "")
DUNGEON_SETS["amber plasm"] = DungeonSet("Amber Plasm", "", "", "", "", "")
DUNGEON_SETS["armor of truth"] = DungeonSet("Armor of Truth", "", "", "", "",
                                            "")
DUNGEON_SETS["auroran's thunder"] = DungeonSet("Auroran's Thunder", "", "", "",
                                               "", "")
DUNGEON_SETS["azureblight reaper"] = DungeonSet("Azureblight Reaper", "", "",
                                                "", "", "")
DUNGEON_SETS["bani's torment"] = DungeonSet("Bani's Torment", "", "", "", "",
                                            "")
DUNGEON_SETS["barkskin"] = DungeonSet("Barkskin", "", "", "", "", "")
DUNGEON_SETS["blood moon"] = DungeonSet("Blood Moon", "", "", "", "", "")
DUNGEON_SETS["blooddrinker"] = DungeonSet("Blooddrinker", "", "", "", "", "")
DUNGEON_SETS["bone pirate's tatters"] = DungeonSet("Bone Pirate's Tatters", "",
                                                   "", "", "", "")
DUNGEON_SETS["brands of imperium"] = DungeonSet("Brands of Imperium", "", "",
                                                "", "", "")
DUNGEON_SETS["burning spellweave"] = DungeonSet("Burning Spellweave", "", "",
                                                "", "", "")
DUNGEON_SETS["caluurion's legacy"] = DungeonSet("Caluurion's Legacy", "", "",
                                                "", "", "")
DUNGEON_SETS["combat physician"] = DungeonSet("Combat Physician", "", "", "",
                                              "", "")
DUNGEON_SETS["crusader"] = DungeonSet("Crusader", "", "", "", "", "")
DUNGEON_SETS["curse of doylemish"] = DungeonSet("Curse of Doylemish", "", "",
                                                "", "", "")
DUNGEON_SETS["dragon's defilement"] = DungeonSet("Dragon's Defilement", "", "",
                                                 "", "", "")
DUNGEON_SETS["draugr hulk"] = DungeonSet("Draugr Hulk", "", "", "", "", "")
DUNGEON_SETS["draugr's rest"] = DungeonSet("Draugr's Rest", "", "", "", "", "")
DUNGEON_SETS["draugrkin's grip"] = DungeonSet("Draugrkin's Grip", "", "", "",
                                              "", "")
DUNGEON_SETS["dreugh king slayer"] = DungeonSet("Dreugh King Slayer", "", "",
                                                "", "", "")
DUNGEON_SETS["dro'zakar's claw"] = DungeonSet("Dro'Zakar's Claws", "", "", "",
                                              "", "")
DUNGEON_SETS["dunerippper's scales"] = DungeonSet("Duneripper's Scales", "",
                                                  "", "", "", "")
DUNGEON_SETS["durok's bane"] = DungeonSet("Durok's Bane", "", "", "", "", "")
DUNGEON_SETS["ebon armory"] = DungeonSet("Ebon Armory", "", "", "", "", "")
DUNGEON_SETS["embershield"] = DungeonSet("Embershield", "", "", "", "", "")
DUNGEON_SETS["essence thief"] = DungeonSet("Essence Thief", "", "", "", "", "")
DUNGEON_SETS["flame blossom"] = DungeonSet("Flame Blossom", "", "", "", "", "")
DUNGEON_SETS["frozen watcher"] = DungeonSet("Frozen Watcher", "", "", "", "",
                                            "")
DUNGEON_SETS["gossamer"] = DungeonSet("Gossamer", "", "", "", "", "")
DUNGEON_SETS["grave guardian"] = DungeonSet("Grave Guardian", "", "", "", "",
                                            "")
DUNGEON_SETS["hagraven's garden"] = DungeonSet("Hagraven's Garden", "", "", "",
                                               "", "")
DUNGEON_SETS["hand of mephala"] = DungeonSet("Hand of Mephala", "", "", "", "",
                                             "")
DUNGEON_SETS["hanu's compassion"] = DungeonSet("Hanu's Compassion", "", "", "",
                                               "", "")
DUNGEON_SETS["haven of ursus"] = DungeonSet("Haven of Ursus", "", "", "", "",
                                            "")
DUNGEON_SETS["heem-jas' retribution"] = DungeonSet("Heem-Jas' Retribution", "",
                                                   "", "", "", "")
DUNGEON_SETS["hircine's veneer"] = DungeonSet("Hircine's Veneer", "", "", "",
                                              "", "")
DUNGEON_SETS["hiti's hearth"] = DungeonSet("Hiti's Hearth", "", "", "", "", "")
DUNGEON_SETS["hollowfang thirst"] = DungeonSet("Hollowfang Thirst", "", "", "",
                                               "", "")
DUNGEON_SETS["icy conjuror"] = DungeonSet("Icy Conjuror", "", "", "", "", "")
DUNGEON_SETS["ironblood"] = DungeonSet("Ironblood", "", "", "", "", "")
DUNGEON_SETS["jailbreaker"] = DungeonSet("Jailbreaker", "", "", "", "", "")
DUNGEON_SETS["jailer's tenacity"] = DungeonSet("Jailer's Tenacity", "", "", "",
                                               "", "")
DUNGEON_SETS["jolting arms"] = DungeonSet("Jolting Arms", "", "", "", "", "")
DUNGEON_SETS["jorvuld's guidance"] = DungeonSet("Jorvuld's Guidance", "", "",
                                                "", "", "")
DUNGEON_SETS["knight-errant's mail"] = DungeonSet("Knight-Errant's Mail", "",
                                                  "", "", "", "")
DUNGEON_SETS["knightmare"] = DungeonSet("Knightmare", "", "", "", "", "")
DUNGEON_SETS["lamia's song"] = DungeonSet("Lamia's Song", "", "", "", "", "")
DUNGEON_SETS["leeching plate"] = DungeonSet("Leeching Plate", "", "", "", "",
                                            "")
DUNGEON_SETS["leviathan"] = DungeonSet("Leviathan", "", "", "", "", "")
DUNGEON_SETS["light speaker"] = DungeonSet("Light Speaker", "", "", "", "", "")
DUNGEON_SETS["magicka furnace"] = DungeonSet("Magicka Furnace", "", "", "", "",
                                             "")
DUNGEON_SETS["medusa"] = DungeonSet("Medusa", "", "", "", "", "")
DUNGEON_SETS["mighty glacier"] = DungeonSet("Mighty Glacier", "", "", "", "",
                                            "")
DUNGEON_SETS["moon hunter"] = DungeonSet("Moon Hunter", "", "", "", "", "")
DUNGEON_SETS["netch's touch"] = DungeonSet("Netch's Touch", "", "", "", "", "")
DUNGEON_SETS["nikulas' heavy armor"] = DungeonSet("Nikulas' Heavy Armor", "",
                                                  "", "", "", "")
DUNGEON_SETS["noble duelist's silks"] = DungeonSet("Noble Duelist's Silks", "",
                                                   "", "", "", "")
DUNGEON_SETS["oblivion's edge"] = DungeonSet("Oblivion's Edge", "", "", "", "",
                                             "")
DUNGEON_SETS["overwhelming surge"] = DungeonSet("Overwhelming Surge", "", "",
                                                "", "", "")
DUNGEON_SETS["pillar of nirn"] = DungeonSet("Pillar of Nirn", "", "", "", "",
                                            "")
DUNGEON_SETS["plague slinger"] = DungeonSet("Plague Slinger", "", "", "", "",
                                            "")
DUNGEON_SETS["prayer shawl"] = DungeonSet("Prayer Shawl", "", "", "", "", "")
DUNGEON_SETS["rattlecage"] = DungeonSet("Rattlecage", "", "", "", "", "")
DUNGEON_SETS["renald's resolve"] = DungeonSet("Renald's Resolve", "", "", "",
                                              "", "")
DUNGEON_SETS["sanctuary"] = DungeonSet("Sanctuary", "", "", "", "", "")
DUNGEON_SETS["savage werewolf"] = DungeonSet("Savage Werewolf", "", "", "", "",
                                             "")
DUNGEON_SETS["scathing mage"] = DungeonSet("Scathing Mage", "", "", "", "", "")
DUNGEON_SETS["scavenging demise"] = DungeonSet("Scavenging Demise", "", "", "",
                                               "", "")
DUNGEON_SETS["sergeant's mail"] = DungeonSet("Sergeant's Mail", "", "", "", "",
                                             "")
DUNGEON_SETS["sheer venom"] = DungeonSet("Sheer Venom", "", "", "", "", "")
DUNGEON_SETS["shroud of the lich"] = DungeonSet("Shroud of the Lich", "", "",
                                                "", "", "")
DUNGEON_SETS["spell power cure"] = DungeonSet("Spell Power Cure", "", "", "",
                                              "", "")
DUNGEON_SETS["spelunker"] = DungeonSet("Spelunker", "", "", "", "", "")
DUNGEON_SETS["spider cultist cowl"] = DungeonSet("Spider Cultist Cowl", "", "",
                                                 "", "", "")
DUNGEON_SETS["storm master"] = DungeonSet("Storm Master", "", "", "", "", "")
DUNGEON_SETS["strength of the automation"] = DungeonSet(
    "Strength of the Automaton", "", "", "", "", "")
DUNGEON_SETS["sunderflame"] = DungeonSet("Sunderflame", "", "", "", "", "")
DUNGEON_SETS["sword dancer"] = DungeonSet("Sword Dancer", "", "", "", "", "")
DUNGEON_SETS["the ice furnace"] = DungeonSet("The Ice Furnace", "", "", "", "",
                                             "")
DUNGEON_SETS["the worm's raiment"] = DungeonSet("The Worm's Raiment", "", "",
                                                "", "", "")
DUNGEON_SETS["titanborn strength"] = DungeonSet("Titanborn Strength", "", "",
                                                "", "", "")
DUNGEON_SETS["toothrow"] = DungeonSet("Toothrow", "", "", "", "", "")
DUNGEON_SETS["tormentor"] = DungeonSet("Tormentor", "", "", "", "", "")
DUNGEON_SETS["trappings of invigoration"] = DungeonSet(
    "Trappings of Invigoration", "", "", "", "", "")
DUNGEON_SETS["treasure hunter"] = DungeonSet("Treasure Hunter", "", "", "", "",
                                             "")
DUNGEON_SETS["tsogvin's warband"] = DungeonSet("Tzogvin's Warband", "", "", "",
                                               "", "")
DUNGEON_SETS["ulfnor's favor"] = DungeonSet("Ulfnor's Favor", "", "", "", "",
                                            "")
DUNGEON_SETS["undaunted bastion"] = DungeonSet("Undaunted Bastion", "", "", "",
                                               "", "")
DUNGEON_SETS["undaunted infiltrator"] = DungeonSet("Undaunted Infiltrator", "",
                                                   "", "", "", "")
DUNGEON_SETS["undaunted unweaver"] = DungeonSet("Undaunted Unweaver", "", "",
                                                "", "", "")
DUNGEON_SETS["vestments of the warlock"] = DungeonSet(
    "Vestments of the Warlock", "", "", "", "", "")
DUNGEON_SETS["viper's sting"] = DungeonSet("Viper's Sting", "", "", "", "", "")
DUNGEON_SETS["widowmaker"] = DungeonSet("Widowmaker", "", "", "", "", "")
DUNGEON_SETS["z'en's redress"] = DungeonSet("Z'en's Redress", "", "", "", "",
                                            "")
