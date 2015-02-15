__author__ = 'Bob'
#comparethemurlco module to return petname
from Infograb import petid_get
def getpet(id):# gets around seeking from wow api by using saved dictionary..will move to module and self edit on none

        pet_dict =	{'MechanicalSquirrel': 'petSpeciesId:39',
        'BombayCat':'petSpeciesId:40',
        'CornishRexCat':'petSpeciesId:41',
        'BlackTabbyCat':'petSpeciesId:42',
        'OrangeTabbyCat':'petSpeciesId:43',
        'SiameseCat':'petSpeciesId:44',
        'SilverTabbyCat':'petSpeciesId:45',
        'WhiteKitten':'petSpeciesId:46',
        'Cockatiel':'petSpeciesId:47',
        'HyacinthMacaw':'petSpeciesId:49',
        'GreenWingMacaw':'petSpeciesId:50',
        'Senegal':'petSpeciesId:51',
        'AnconaChicken':'petSpeciesId:52',
        'UndercityCockroach':'petSpeciesId:55',
        'DarkWhelpling':'petSpeciesId:56',
        'AzureWhelpling':'petSpeciesId:57',
        'CrimsonWhelpling':'petSpeciesId:58',
        'EmeraldWhelpling':'petSpeciesId:59',
        'WoodFrog':'petSpeciesId:64',
        'TreeFrog':'petSpeciesId:65',
        'HawkOwl':'petSpeciesId:67',
        'GreatHornedOwl':'petSpeciesId:68',
        'SnowyOwl':'petSpeciesId:69',
        'BrownPrairieDog':'petSpeciesId:70',
        'SnowshoeRabbit':'petSpeciesId:72',
        'AlbinoSnake':'petSpeciesId:74',
        'BlackKingsnake':'petSpeciesId:75',
        'BrownSnake':'petSpeciesId:77',
        'CrimsonSnake':'petSpeciesId:78',
        'MechanicalChicken':'petSpeciesId:83',
        'WestfallChicken':'petSpeciesId:84',
        'PetBombling':'petSpeciesId:85',
        'LilSmoky':'petSpeciesId:86',
        'SpriteDarterHatchling':'petSpeciesId:87',
        'WorgPup':'petSpeciesId:89',
        'SmolderwebHatchling':'petSpeciesId:90',
        'PandaCub':'petSpeciesId:92',
        'MiniDiablo':'petSpeciesId:93',
        'Zergling':'petSpeciesId:94',
        'LifelikeToad':'petSpeciesId:95',
        'Jubling':'petSpeciesId:106',
        'Murky':'petSpeciesId:107',
        'Lurky':'petSpeciesId:111',
        'DisgustingOozeling':'petSpeciesId:114',
        'TranquilMechanicalYeti':'petSpeciesId:116',
        'TinySnowman':'petSpeciesId:117',
        'WinterReindeer':'petSpeciesId:118',
        'FatherWintersHelper:':'petSpeciesId:119',
        'WintersLittleHelper':'petSpeciesId:120',
        'Gurky':'petSpeciesId:121',
        'Peddlefeet':'petSpeciesId:122',
        'Poley':'petSpeciesId:124',
        'Speedy':'petSpeciesId:125',
        'Mr.Wiggles':'petSpeciesId:126',
        'WhiskerstheRat':'petSpeciesId:127',
        'SpiritofSummer':'petSpeciesId:128',
        'HippogryphHatchling':'petSpeciesId:130',
        'Netherwhelp':'petSpeciesId:131',
        'MagicalCrawdad':'petSpeciesId:132',
        'ManaWyrmling':'petSpeciesId:136',
        'BrownRabbit':'petSpeciesId:137',
        'BlueMoth':'petSpeciesId:138',
        'RedMoth':'petSpeciesId:139',
        'YellowMoth':'petSpeciesId:140',
        'WhiteMoth':'petSpeciesId:141',
        'GoldenDragonhawkHatchling':'petSpeciesId:142',
        'RedDragonhawkHatchling':'petSpeciesId:143',
        'SilverDragonhawkHatchling':'petSpeciesId:144',
        'BlueDragonhawkHatchling':'petSpeciesId:145',
        'Firefly':'petSpeciesId:146',
        'Error_pet_not_found' : 'petSpeciesID:6',
        'Miniwing':'petSpeciesId:149',
        'Wolpertinger':'petSpeciesId:153',
        'Lucky':'petSpeciesId:155',
        'Bananas':'petSpeciesId:156',
        'Willy':'petSpeciesId:157',
        'Egbert':'petSpeciesId:158',
        'Peanut':'petSpeciesId:159',
        'Stinker':'petSpeciesId:160',
        'SinisterSquashling':'petSpeciesId:162',
        'Toothy':'petSpeciesId:163',
        'Muckbreath':'petSpeciesId:164',
        'Mojo':'petSpeciesId:165',
        'Pint-SizedPinkPachyderm':'petSpeciesId:166',
        'TinySporebat':'petSpeciesId:167',
        'RocketChicken':'petSpeciesId:168',
        'DragonKite':'petSpeciesId:169',
        'GoldenPig':'petSpeciesId:170',
        'SilverPig':'petSpeciesId:171',
        'SearingScorchling':'petSpeciesId:172',
        'Snarly':'petSpeciesId:173',
        'Chuck':'petSpeciesId:174',
        'PhoenixHatchling':'petSpeciesId:175',
        'SpiritofCompetition':'petSpeciesId:179',
        'EssenceofCompetition':'petSpeciesId:180',
        'EtherealSoul-Trader':'petSpeciesId:183',
        'NetherRayFry':'petSpeciesId:186',
        'VampiricBatling':'petSpeciesId:187',
        'Frosty':'petSpeciesId:188',
        'MiniTyrael':'petSpeciesId:189',
        'GhostlySkull':'petSpeciesId:190',
        'ClockworkRocketBot':'petSpeciesId:191',
        'Mr.Chilly':'petSpeciesId:192',
        'GiantSewerRat':'petSpeciesId:193',
        'TickbirdHatchling':'petSpeciesId:194',
        'WhiteTickbirdHatchling':'petSpeciesId:195',
        'Proto-DrakeWhelp':'petSpeciesId:196',
        'CobraHatchling':'petSpeciesId:197',
        'Pengu':'petSpeciesId:198',
        'KirinTorFamiliar':'petSpeciesId:199',
        'SpringRabbit':'petSpeciesId:200',
        'PlumpTurkey':'petSpeciesId:201',
        'BabyBlizzardBear':'petSpeciesId:202',
        'LittleFawn':'petSpeciesId:203',
        'TeldrassilSproutling':'petSpeciesId:204',
        'DunMoroghCub':'petSpeciesId:205',
        'TirisfalBatling':'petSpeciesId:206',
        'DurotarScorpion':'petSpeciesId:207',
        'ElwynnLamb':'petSpeciesId:209',
        'MulgoreHatchling':'petSpeciesId:210',
        'StrandCrawler':'petSpeciesId:211',
        'AmmenValeLashling':'petSpeciesId:212',
        'EnchantedBroom':'petSpeciesId:213',
        'ArgentSquire':'petSpeciesId:214',
        'Mechanopeep':'petSpeciesId:215',
        'ArgentGruntling':'petSpeciesId:216',
        'MurkimustheGladiator':'petSpeciesId:217',
        'SenjinFetish':'petSpeciesId:218',
        'Withers':'petSpeciesId:220',
        'CalicoCat':'petSpeciesId:224',
        'CuriousOracleHatchling':'petSpeciesId:225',
        'CuriousWolvarPup':'petSpeciesId:226',
        'Warbot':'petSpeciesId:227',
        'Grunty':'petSpeciesId:228',
        'ShimmeringWyrmling':'petSpeciesId:229',
        'JadeTiger':'petSpeciesId:231',
        'DartingHatchling':'petSpeciesId:232',
        'DeviateHatchling':'petSpeciesId:233',
        'GundrakHatchling':'petSpeciesId:234',
        'LeapingHatchling':'petSpeciesId:235',
        'ObsidianHatchling':'petSpeciesId:236',
        'RavasaurHatchling':'petSpeciesId:237',
        'RazormawHatchling':'petSpeciesId:238',
        'RazzashiHatchling':'petSpeciesId:239',
        'OnyxPanther':'petSpeciesId:240',
        'TuskarrKite':'petSpeciesId:241',
        'SpectralTigerCub':'petSpeciesId:242',
        'OnyxianWhelpling':'petSpeciesId:243',
        'CoreHoundPup':'petSpeciesId:244',
        'GryphonHatchling':'petSpeciesId:245',
        'WindRiderCub':'petSpeciesId:246',
        'ZipaoTiger':'petSpeciesId:247',
        'PandarenMonk':'petSpeciesId:248',
        'LilKT':'petSpeciesId:249',
        'PerkyPug':'petSpeciesId:250',
        'ToxicWasteling':'petSpeciesId:251',
        'FrigidFrostling':'petSpeciesId:253',
        'BlueClockworkRocketBot':'petSpeciesId:254',
        'CelestialDragon':'petSpeciesId:255',
        'LilXT':'petSpeciesId:256',
        'MiniThor':'petSpeciesId:258',
        'BlueMiniJouster':'petSpeciesId:259',
        'GoldMiniJouster':'petSpeciesId:260',
        'PersonalWorldDestroyer':'petSpeciesId:261',
        'De-WeaponizedMechanicalCompanion':'petSpeciesId:262',
        'CrawlingClaw':'petSpeciesId:264',
        'Pebble':'petSpeciesId:265',
        'FossilizedHatchling':'petSpeciesId:266',
        'EnchantedLantern':'petSpeciesId:267',
        'LilDeathwing':'petSpeciesId:268',
        'DarkPhoenixHatchling':'petSpeciesId:270',
        'RustbergGull':'petSpeciesId:271',
        'ArmadilloPup':'petSpeciesId:272',
        'ClockworkGnome':'petSpeciesId:277',
        'FoxKit':'petSpeciesId:278',
        'TinyShaleSpider':'petSpeciesId:279',
        'GuildPage':'petSpeciesId:281',
        'GuildHerald':'petSpeciesId:283',
        'LandrosLilXT':'petSpeciesId:285',
        'Mr.Grubbs':'petSpeciesId:286',
        'TinyFlamefly':'petSpeciesId:287',
        'ScootertheSnail':'petSpeciesId:289',
        'SingingSunflower':'petSpeciesId:291',
        'MagicLamp':'petSpeciesId:292',
        'ElementiumGeode':'petSpeciesId:293',
        'Deathy':'petSpeciesId:294',
        'LilRagnaros':'petSpeciesId:297',
        'MoonkinHatchling':'petSpeciesId:298',
        'PantherCub':'petSpeciesId:301',
        'LandrosLichling':'petSpeciesId:302',
        'NightsaberCub':'petSpeciesId:303',
        'WinterspringCub':'petSpeciesId:306',
        'LashtailHatchling':'petSpeciesId:307',
        'Legs':'petSpeciesId:308',
        'PterrordaxHatchling':'petSpeciesId:309',
        'VoodooFigurine':'petSpeciesId:310',
        'GuardianCub':'petSpeciesId:311',
        'CenarionHatchling':'petSpeciesId:316',
        'HyjalBearCub':'petSpeciesId:317',
        'CrimsonLasher':'petSpeciesId:318',
        'FelineFamiliar':'petSpeciesId:319',
        'LilTarecgosa':'petSpeciesId:320',
        'CreepyCrate':'petSpeciesId:321',
        'Nuts':'petSpeciesId:323',
        'BrilliantKaliri':'petSpeciesId:325',
        'PurplePuffer':'petSpeciesId:328',
        'Murkablo':'petSpeciesId:329',
        'DarkmoonMonkey':'petSpeciesId:330',
        'AllianceBalloon':'petSpeciesId:331',
        'HordeBalloon':'petSpeciesId:332',
        'GregariousGrell':'petSpeciesId:333',
        'DarkmoonTurtle':'petSpeciesId:335',
        'DarkmoonBalloon':'petSpeciesId:336',
        'Lumpy':'petSpeciesId:337',
        'DarkmoonTonk':'petSpeciesId:338',
        'DarkmoonZeppelin':'petSpeciesId:339',
        'SeaPony':'petSpeciesId:340',
        'LunarLantern':'petSpeciesId:341',
        'FestivalLantern':'petSpeciesId:342',
        'DarkmoonCub':'petSpeciesId:343',
        'GreenBalloon':'petSpeciesId:344',
        'YellowBalloon':'petSpeciesId:345',
        'FetishShaman':'petSpeciesId:346',
        'SouloftheAspects':'petSpeciesId:347',
        'EyeoftheLegion':'petSpeciesId:348',
        'BlackLamb':'petSpeciesId:374',
        'Rabbit':'petSpeciesId:378',
        'Squirrel':'petSpeciesId:379',
        'BucktoothFlapper':'petSpeciesId:380',
        'Porcupette':'petSpeciesId:381',
        'EternalStrider':'petSpeciesId:383',
        'Mouse':'petSpeciesId:385',
        'PrairieDog':'petSpeciesId:386',
        'Snake':'petSpeciesId:387',
        'ShoreCrab':'petSpeciesId:388',
        'TinyHarvester':'petSpeciesId:389',
        'MountainCottontail':'petSpeciesId:391',
        'RedridgeRat':'petSpeciesId:392',
        'Cockroach':'petSpeciesId:393',
        'FledglingBuzzard':'petSpeciesId:395',
        'DuskSpiderling':'petSpeciesId:396',
        'Skunk':'petSpeciesId:397',
        'BlackRat':'petSpeciesId:398',
        'RatSnake':'petSpeciesId:399',
        'WidowSpiderling':'petSpeciesId:400',
        'StrandCrab':'petSpeciesId:401',
        'SwampMoth':'petSpeciesId:402',
        'Parrot':'petSpeciesId:403',
        'Long-tailedMole':'petSpeciesId:404',
        'TreePython':'petSpeciesId:405',
        'Beetle':'petSpeciesId:406',
        'ForestSpiderling':'petSpeciesId:407',
        'LizardHatchling':'petSpeciesId:408',
        'Polly':'petSpeciesId:409',
        'WharfRat':'petSpeciesId:410',
        'BabyApe':'petSpeciesId:411',
        'Spider':'petSpeciesId:412',
        'Scorpid':'petSpeciesId:414',
        'FireBeetle':'petSpeciesId:415',
        'Scorpling':'petSpeciesId:416',
        'Rat':'petSpeciesId:417',
        'WaterSnake':'petSpeciesId:418',
        'SmallFrog':'petSpeciesId:419',
        'Toad':'petSpeciesId:420',
        'CrimsonMoth':'petSpeciesId:421',
        'Moccasin':'petSpeciesId:422',
        'LavaCrab':'petSpeciesId:423',
        'Roach':'petSpeciesId:424',
        'AshViper':'petSpeciesId:425',
        'AshSpiderling':'petSpeciesId:427',
        'MoltenHatchling':'petSpeciesId:428',
        'LavaBeetle':'petSpeciesId:429',
        'GoldBeetle':'petSpeciesId:430',
        'Rattlesnake':'petSpeciesId:431',
        'Stripe-TailedScorpid':'petSpeciesId:432',
        'SpikyLizard':'petSpeciesId:433',
        'LittleBlackRam':'petSpeciesId:437',
        'KingSnake':'petSpeciesId:438',
        'RestlessShadeling':'petSpeciesId:439',
        'SnowCub':'petSpeciesId:440',
        'AlpineHare':'petSpeciesId:441',
        'IrradiatedRoach':'petSpeciesId:442',
        'GrasslandsCottontail':'petSpeciesId:443',
        'TinyTwister':'petSpeciesId:445',
        'JadeOozeling':'petSpeciesId:446',
        'Fawn':'petSpeciesId:447',
        'Hare':'petSpeciesId:448',
        'BrownMarmot':'petSpeciesId:449',
        'Maggot':'petSpeciesId:450',
        'Red-TailedChipmunk':'petSpeciesId:452',
        'InfestedBearCub':'petSpeciesId:453',
        'UndercityRat':'petSpeciesId:454',
        'BlightedSquirrel':'petSpeciesId:455',
        'Blighthawk':'petSpeciesId:456',
        'FesteringMaggot':'petSpeciesId:457',
        'LostofLordaeron':'petSpeciesId:458',
        'Cat':'petSpeciesId:459',
        'RubySapling':'petSpeciesId:460',
        'Larva':'petSpeciesId:461',
        'SpiritCrab':'petSpeciesId:463',
        'GreyMoth':'petSpeciesId:464',
        'RavagerHatchling':'petSpeciesId:465',
        'SpinyLizard':'petSpeciesId:466',
        'DungBeetle':'petSpeciesId:467',
        'CreepyCrawly':'petSpeciesId:468',
        'TwilightBeetle':'petSpeciesId:469',
        'TwilightSpider':'petSpeciesId:470',
        'Robo-Chick':'petSpeciesId:471',
        'RabidNutVarmint5000':'petSpeciesId:472',
        'TurquoiseTurtle':'petSpeciesId:473',
        'CheetahCub':'petSpeciesId:474',
        'GiraffeCalf':'petSpeciesId:475',
        'GazelleFawn':'petSpeciesId:477',
        'ForestMoth':'petSpeciesId:478',
        'ElfinRabbit':'petSpeciesId:479',
        'TopazShaleHatchling':'petSpeciesId:480',
        'RockViper':'petSpeciesId:482',
        'HornyToad':'petSpeciesId:483',
        'DesertSpider':'petSpeciesId:484',
        'StoneArmadillo':'petSpeciesId:485',
        'AlpineChipmunk':'petSpeciesId:487',
        'CoralSnake':'petSpeciesId:488',
        'SpawnofOnyxia':'petSpeciesId:489',
        'SandKitten':'petSpeciesId:491',
        'Stinkbug':'petSpeciesId:492',
        'ShimmershellSnail':'petSpeciesId:493',
        'SilithidHatchling':'petSpeciesId:494',
        'Frog':'petSpeciesId:495',
        'RustySnail':'petSpeciesId:496',
        'TaintedCockroach':'petSpeciesId:497',
        'TaintedMoth':'petSpeciesId:498',
        'TaintedRat':'petSpeciesId:499',
        'Minfernal':'petSpeciesId:500',
        'SpottedBellFrog':'petSpeciesId:502',
        'SilkyMoth':'petSpeciesId:503',
        'DiemetradonHatchling':'petSpeciesId:504',
        'TwilightIguana':'petSpeciesId:505',
        'VenomspitterHatchling':'petSpeciesId:506',
        'CrestedOwl':'petSpeciesId:507',
        'DarkshoreCub':'petSpeciesId:508',
        'TinyBogBeast':'petSpeciesId:509',
        'Rabbot':'petSpeciesId:510',
        'Sidewinder':'petSpeciesId:511',
        'ScarabHatchling':'petSpeciesId:512',
        'QirajiGuardling':'petSpeciesId:513',
        'FlayerYoungling':'petSpeciesId:514',
        'SporelingSprout':'petSpeciesId:515',
        'WarpstalkerHatchling':'petSpeciesId:517',
        'ClefthoofRunt':'petSpeciesId:518',
        'FelFlame':'petSpeciesId:519',
        'FledglingNetherRay':'petSpeciesId:521',
        'DevouringMaggot':'petSpeciesId:523',
        'Turkey':'petSpeciesId:525',
        'ScaldedBasiliskHatchling':'petSpeciesId:528',
        'FjordWorgPup':'petSpeciesId:529',
        'OilySlimeling':'petSpeciesId:530',
        'StuntedShardhorn':'petSpeciesId:532',
        'ImperialEagleChick':'petSpeciesId:534',
        'WaterWaveling':'petSpeciesId:535',
        'TundraPenguin':'petSpeciesId:536',
        'DragonboneHatchling':'petSpeciesId:537',
        'ScourgedWhelpling':'petSpeciesId:538',
        'GrottoVole':'petSpeciesId:539',
        'CarrionRat':'petSpeciesId:540',
        'Fire-ProofRoach':'petSpeciesId:541',
        'MacFrog':'petSpeciesId:542',
        'Locust':'petSpeciesId:543',
        'OasisMoth':'petSpeciesId:544',
        'LeopardScorpid':'petSpeciesId:545',
        'TolvirScarab':'petSpeciesId:546',
        'NordrassilWisp':'petSpeciesId:547',
        'WildhammerGryphonHatchling':'petSpeciesId:548',
        'Yellow-BelliedMarmot':'petSpeciesId:549',
        'HighlandsMouse':'petSpeciesId:550',
        'TwilightFiendling':'petSpeciesId:552',
        'StowawayRat':'petSpeciesId:553',
        'CrimsonShaleHatchling':'petSpeciesId:554',
        'DeepholmCockroach':'petSpeciesId:555',
        'CrystalBeetle':'petSpeciesId:556',
        'NetherFaerieDragon':'petSpeciesId:557',
        'ArcticFoxKit':'petSpeciesId:558',
        'CrimsonGeode':'petSpeciesId:559',
        'SeaGull':'petSpeciesId:560',
        'CoralAdder':'petSpeciesId:562',
        'EmeraldTurtle':'petSpeciesId:564',
        'JungleDarter':'petSpeciesId:565',
        'MirrorStrider':'petSpeciesId:566',
        'TempleSnake':'petSpeciesId:567',
        'SilkbeadSnail':'petSpeciesId:568',
        'GardenFrog':'petSpeciesId:569',
        'MaskedTanuki':'petSpeciesId:570',
        'GroveViper':'petSpeciesId:571',
        'SpireboundCrab':'petSpeciesId:572',
        'SandyPetrel':'petSpeciesId:573',
        'Bat':'petSpeciesId:626',
        'InfectedSquirrel':'petSpeciesId:627',
        'InfectedFawn':'petSpeciesId:628',
        'ShoreCrawler':'petSpeciesId:629',
        'GilneanRaven':'petSpeciesId:630',
        'EmeraldBoa':'petSpeciesId:631',
        'AshLizard':'petSpeciesId:632',
        'MountainSkunk':'petSpeciesId:633',
        'CrystalSpider':'petSpeciesId:634',
        'Adder':'petSpeciesId:635',
        'SkitteringCavernCrawler':'petSpeciesId:637',
        'NetherRoach':'petSpeciesId:638',
        'BoreanMarmot':'petSpeciesId:639',
        'SnowshoeHare':'petSpeciesId:640',
        'ArcticHare':'petSpeciesId:641',
        'FjordRat':'petSpeciesId:644',
        'HighlandsTurkey':'petSpeciesId:645',
        'Chicken':'petSpeciesId:646',
        'GrizzlySquirrel':'petSpeciesId:647',
        'HugeToad':'petSpeciesId:648',
        'Biletoad':'petSpeciesId:649',
        'TerribleTurnip':'petSpeciesId:650',
        'TinyGoldfish':'petSpeciesId:652',
        'SandScarab':'petSpeciesId:665',
        'LuckyQuilenCub':'petSpeciesId:671',
        'StormwindRat':'petSpeciesId:675',
        'ShyBandicoon':'petSpeciesId:677',
        'JungleGrub':'petSpeciesId:678',
        'SummitKid':'petSpeciesId:679',
        'KuitanMongoose':'petSpeciesId:680',
        'JumpingSpider':'petSpeciesId:699',
        'LeopardTreeFrog':'petSpeciesId:702',
        'MaskedTanukiPup':'petSpeciesId:703',
        'AmorousRooster':'petSpeciesId:705',
        'Bandicoon':'petSpeciesId:706',
        'BandicoonKit':'petSpeciesId:707',
        'MalayanQuillrat':'petSpeciesId:708',
        'MalayanQuillratPup':'petSpeciesId:709',
        'MarshFiddler':'petSpeciesId:710',
        'SifangOtter':'petSpeciesId:711',
        'SifangOtterPup':'petSpeciesId:712',
        'SoftshellSnapling':'petSpeciesId:713',
        'FeverbiteHatchling':'petSpeciesId:714',
        'WildSilkworm':'petSpeciesId:715',
        'AmethystSpiderling':'petSpeciesId:716',
        'SavoryBeetle':'petSpeciesId:717',
        'LuyuMoth':'petSpeciesId:718',
        'MeiLiSparkler':'petSpeciesId:722',
        'SpinyTerrapin':'petSpeciesId:723',
        'AlpineFoxling':'petSpeciesId:724',
        'AlpineFoxlingKit':'petSpeciesId:725',
        'PlainsMonitor':'petSpeciesId:726',
        'PrairieMouse':'petSpeciesId:727',
        'SzechuanChicken':'petSpeciesId:728',
        'TolaiHare':'petSpeciesId:729',
        'TolaiHarePup':'petSpeciesId:730',
        'ZooeySnake':'petSpeciesId:731',
        'AmberMoth':'petSpeciesId:732',
        'GrasslandHopper':'petSpeciesId:733',
        'Mongoose':'petSpeciesId:737',
        'MongoosePup':'petSpeciesId:739',
        'Yakrat':'petSpeciesId:740',
        'SilentHedgehog':'petSpeciesId:741',
        'CloudedHedgehog':'petSpeciesId:742',
        'RapanaWhelk':'petSpeciesId:743',
        'ResilientRoach':'petSpeciesId:744',
        'CrunchyScorpion':'petSpeciesId:745',
        'EmperorCrab':'petSpeciesId:746',
        'EffervescentGlowfly':'petSpeciesId:747',
        'GildedMoth':'petSpeciesId:748',
        'GoldenCivet':'petSpeciesId:749',
        'GoldenCivetKitten':'petSpeciesId:750',
        'DancingWaterSkimmer':'petSpeciesId:751',
        'Yellow-BelliedBullfrog':'petSpeciesId:752',
        'GardenMoth':'petSpeciesId:753',
        'ShrineFly':'petSpeciesId:754',
        'DeathsHeadCockroach':'petSpeciesId:755',
        'FungalMoth':'petSpeciesId:756',
        'TinyGreenDragon':'petSpeciesId:757',
        'TinyRedDragon':'petSpeciesId:758',
        'JadeCraneChick':'petSpeciesId:792',
        'ThunderingSerpentHatchling':'petSpeciesId:802',
        'WildJadeHatchling':'petSpeciesId:817',
        'WildGoldenHatchling':'petSpeciesId:818',
        'WildCrimsonHatchling':'petSpeciesId:819',
        'SingingCricket':'petSpeciesId:820',
        'FeralVermling':'petSpeciesId:821',
        'HighlandsSkunk':'petSpeciesId:823',
        'Grinder':'petSpeciesId:834',
        'Hopling':'petSpeciesId:835',
        'AquaStrider':'petSpeciesId:836',
        'EmeraldShaleHatchling':'petSpeciesId:837',
        'AmethystShaleHatchling':'petSpeciesId:838',
        'MechanicalPandarenDragonling':'petSpeciesId:844',
        'JadeOwl':'petSpeciesId:845',
        'SapphireCub':'petSpeciesId:846',
        'Fishy':'petSpeciesId:847',
        'DarkmoonRabbit':'petSpeciesId:848',
        'Chi-jiKite':'petSpeciesId:849',
        'YulonKite':'petSpeciesId:850',
        'HornedLizard':'petSpeciesId:851',
        'Venus':'petSpeciesId:855',
        'JadeTentacle':'petSpeciesId:856',
        'Baneling':'petSpeciesId:903',
        'WanderersFestivalHatchling':'petSpeciesId:1013',}
        found=False
        for name in pet_dict.keys():

                if pet_dict[name] == id:
                    found=True
                    pet= str(name)
                else:
                    if found==False:
                        pet=str(id)
        if found==False:
            check= id.partition(':')[2]
            #if ':' in check:
            #    check=pet[13:1]
            x=petid_get(check)
            return x
        else:
            return id




if __name__ == '__main__':
    getpet(id)