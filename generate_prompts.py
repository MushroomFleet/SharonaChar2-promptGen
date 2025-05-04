import datetime
import os

# Fixed components for all prompts
PROMPT_TYPE = "depiction of hunter-style cave woman character"
CHARACTER_DESCRIPTION = "sh4r0na woman with short white hair, vibrant orange fur skin blouse with black accents and exposed torso, including matching fur skin wrapped oversized boots and gloves"
PROMPT_STYLE = "Watercolor style graphic novel illustration, detailed ink linework"

# Current timestamp for filenames
TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d-%H%M")

# Theme 1: Ruins of the Ancients
RUINS_OF_ANCIENTS = [
    "she is exploring the remnants of a once-great city, where massive concrete and steel structures are now half-buried and overgrown, with primitive tribal markings painted over faded corporate logos",
    "she is standing amid the ruins of an ancient skyscraper, its broken glass and twisted metal frame now serving as the foundation for a primitive settlement, with campfires burning in what were once office spaces",
    "she is walking through corridors of a fallen metropolis, where sunlight filters through collapsed ceilings and vines snake around rusted elevator shafts",
    "she is climbing the crumbling staircase of a once-mighty structure, now half-reclaimed by nature, with birds nesting in the remnants of technological marvels",
    "she is navigating through the buried ruins of an ancient mall, where tribal markets now operate between collapsed storefronts and fountains have become sacred water sources",
    "she is standing atop a crumbling highway overpass, looking out over a vast landscape where ancient roads are now rivers cutting through new growth forest",
    "she is examining strange artifacts in what was once a museum, now a sacred tribal site where technological relics are worshipped as gifts from the gods",
    "she is moving cautiously through the sunken remains of an ancient subway system, now a network of tribal catacombs adorned with paintings depicting the fall of the old world",
    "she is sheltering in the hollowed-out shell of a toppled monolith, its corporate logo barely visible through layers of erosion and tribal markings",
    "she is trudging through the sand-filled lobby of a grand hotel, where dunes have formed around reception desks and primitive drawings adorn marble walls",
    "she is venturing through a field of rusted vehicles, now overgrown with strange vegetation and repurposed as dwellings by primitive tribes",
    "she is exploring the remnants of an airport, where tribal shamans conduct ceremonies on cracked runways and ancient aircraft serve as chieftain quarters",
    "she is standing in what was once a grand stadium, now a tribal gathering place where ancient sporting events are reenacted as religious ceremonies",
    "she is navigating through a maze of toppled office buildings, where paper and plastic have fossilized and primitive artwork depicts the ancient technological beings",
    "she is perched on the edge of a massive crater where a city once stood, looking down at the new ecosystem that has formed in the ruins",
    "she is moving through a forest of ancient power transmission towers, now wrapped in vines and serving as tribal boundary markers",
    "she is examining the faded remnants of a massive billboard, its advertisement now a mysterious tribal prophecy interpreted by shamans",
    "she is crossing a vast parking structure, now terraced into primitive agricultural plots where tribes grow strange hybrid crops",
    "she is standing before a massive dam, now a tribal temple where the occasional functioning turbine is worshipped as a living deity",
    "she is picking her way through the shattered remains of a once-gleaming corporate headquarters, where tribal councils now meet in boardrooms adorned with bones and pelts"
]

# Theme 2: New Ice Territories
NEW_ICE_TERRITORIES = [
    "she is traversing a vast ice plain where the twisted remains of ancient vehicles protrude from glaciers, while primitive ice-dwellers hunt mammoth-like creatures that have evolved in this new age",
    "she is standing at the edge of a massive glacier that has swallowed an entire city, with only the tallest spires still visible above the ice",
    "she is taking shelter in an ice cave formed within what was once a shopping mall, with frozen escalators and display cases creating strange crystalline formations",
    "she is following a path through snow-covered ruins, where primitive tribes have marked safe passages with totems made from scavenged technological parts",
    "she is crossing a frozen lake that was once a bustling metropolis, the ice clear enough to reveal the sunken buildings below",
    "she is climbing an ice-encrusted monument, its original purpose long forgotten but now serving as a sacred site for the ice tribes",
    "she is navigating through a blizzard across what was once a major highway, now elevated above the snowy landscape like a great white serpent",
    "she is breaking through the ice crust of a frozen building, revealing preserved ancient technology that still glows with mysterious power",
    "she is watching the northern lights dance above a field of frozen satellites, their dishes forever pointed at skies no one remembers how to listen to",
    "she is moving carefully across the frozen surface of what was once a reservoir, now a sacred hunting ground where tribes stalk massive evolved fish beneath the ice",
    "she is standing before a wall of ice that has preserved an ancient library, books and digital screens visible but untouchable within the frozen mass",
    "she is sheltering from the bitter cold in the remains of an ancient nuclear plant, where the snow glows faintly at night and strange creatures roam",
    "she is traversing a narrow path between towering ice formations that have engulfed a once-bustling airport, frozen planes jutting out at odd angles",
    "she is examining primitive ice sculptures crafted by local tribes to mimic the ancient technological wonders half-buried in the surrounding glacier",
    "she is following animal tracks across a vast snowy plain that was once farmland, dotted with the frozen remains of agricultural machinery",
    "she is looking out across a valley of ice spires formed around ancient radio towers, their metal frames creating strange geometric patterns in the frozen landscape",
    "she is cautiously approaching a tribal settlement built from scavenged materials and ice blocks, nestled in the frozen remains of a sports stadium",
    "she is moving between massive ice-covered cooling towers, now sacred sites where tribal elders go to commune with the spirits of the ancient ones",
    "she is navigating through a forest of frozen trees mixed with the preserved remains of power lines, creating an eerie metallic forest",
    "she is standing on the edge of a massive ice shelf that was once a coastal city, watching as primitive boats fish in the waters where skyscrapers are submerged"
]

# Theme 3: Great Desert Expansions
GREAT_DESERT_EXPANSIONS = [
    "she is crossing the vast desert that was once an ocean, where the skeletal remains of massive ships rise from the sand like strange monuments, and nomadic tribes worship at the foot of a crumbling hydroelectric dam",
    "she is navigating through a sea of sand dunes that have completely engulfed a coastal city, with only the tallest buildings peeking above the desert surface",
    "she is taking refuge from a sandstorm in the hollowed-out hull of an ancient container ship, now home to a thriving desert tribe and hundreds of miles from any water",
    "she is following a caravan of traders across what was once a seabed, using the protruding ruins of underwater pipelines as a navigation guide",
    "she is standing atop a massive sand dune, looking down at an ancient harbor now completely dry, where nomadic tribes hold markets amid the stranded vessels",
    "she is exploring the remains of a submarine partially buried in the sand, its mysterious technology now a sacred site for desert shamans",
    "she is trudging across the cracked earth of what was once a great lake, with the preserved wooden docks now serving as bridges between tribal territories",
    "she is sheltering from the scorching sun beneath the tilted deck of a luxury cruise liner, its faded opulence now home to a society of desert dwellers",
    "she is navigating through a forest of oil rigs, now standing like ancient monoliths in a sea of sand, connected by rope bridges built by the nomadic tribes",
    "she is examining strange calcified formations in the desert that were once vibrant coral reefs, now sacred sources of building materials and tools",
    "she is standing before an ancient lighthouse that now serves as a tribal watchtower, its beacon repurposed to signal safe paths through the treacherous desert",
    "she is crossing a vast salt flat that was once an inland sea, where tribal salt miners carefully extract the precious resource using tools fashioned from ancient debris",
    "she is navigating along the edge of a massive canyon carved by the last great waters to recede from this land, with cliff dwellings built into what were once underwater caves",
    "she is moving through a bizarre forest of petrified water towers, their tanks now repurposed as tribal living quarters high above the desert floor",
    "she is standing amid the ruins of a beach resort, with sand-filled swimming pools and lobby fountains now used as precious water cisterns",
    "she is climbing over massive sea walls that once protected coastal cities, now standing as mysterious monuments in the middle of an endless desert",
    "she is following a dry riverbed that cuts through the desert, lined with the remains of bridges that once spanned mighty waters but now connect nothing",
    "she is observing tribal craftspeople who harvest ancient plastic and metal from the desert to create tools and ornaments, unaware of their original purpose",
    "she is navigating through the remains of a marina, its dock structures creating eerie patterns in the desert landscape, with sand dunes forming between rotting hulls",
    "she is sheltering in the shadow of an enormous cargo vessel, now permanently anchored in the desert and serving as a fortress for a powerful nomadic chief"
]

# Theme 4: Reclaimed Forests
RECLAIMED_FORESTS = [
    "she is moving through a dense forest where massive trees have broken through the remains of an ancient highway, and primitive tribal dwellings hang from branches adorned with scavenged technological trinkets",
    "she is navigating a lush canopy that has completely engulfed what was once a suburban neighborhood, with houses barely visible beneath the thick vegetation",
    "she is climbing the moss-covered remains of a skyscraper, now serving as the central trunk for an entire ecosystem of plants and animals",
    "she is walking along the overgrown remains of train tracks, now a tribal pathway through a forest where mechanical parts are occasionally visible beneath the undergrowth",
    "she is standing in a clearing where a shopping mall once stood, its glass ceiling now supporting a canopy of vines and its floors a rich garden of plants",
    "she is moving cautiously through a forest where trees grow from abandoned vehicles, their roots cracking through windshields and their branches extending through roof openings",
    "she is climbing a grand staircase now covered in moss and fungus, leading up to a temple-like structure that was once a government building",
    "she is navigating through the remains of an amusement park, where roller coaster tracks snake through the forest canopy and tribal homes occupy the carousel",
    "she is examining strange hybrid plants that have evolved to incorporate ancient plastics and metals into their structure, creating metallic flowers and circuit-like root systems",
    "she is following a tribal hunting party through a forest that has reclaimed an airport, with planes serving as massive planters for trees that grow through their fuselages",
    "she is standing before an ancient monument now completely wrapped in vines and roots, with only the vague shape still visible beneath the vegetation",
    "she is crossing a natural bridge formed by the intertwined roots of massive trees that have grown up through a collapsed highway overpass",
    "she is moving through the shadowy interior of what was once a stadium, now a cathedral-like forest space where sunlight filters through the collapsed roof",
    "she is observing tribal rituals conducted around a tree that has grown through the center of an ancient technological device, fusing nature and machine",
    "she is navigating along the edge of a forest where the trees are strangely ordered, revealing the grid pattern of the ancient city streets they've replaced",
    "she is pushing through dense undergrowth that has consumed what was once a university campus, with tribal libraries established in the few buildings still accessible",
    "she is standing beneath a canopy of trees that have grown from the ruins of a collapsed bridge, their intertwined branches forming a new passage across the chasm",
    "she is examining tribal dwellings built into the massive trunks of trees that have grown through office buildings, with windows and doors cut into both wood and concrete",
    "she is making her way through a flooded forest where the ruins of a subway system create a maze of partially submerged tunnels filled with aquatic plants",
    "she is following a path through a forest of strange tree-building hybrids, where it's impossible to tell where architecture ends and nature begins"
]

# Theme 5: Volcanic Badlands
VOLCANIC_BADLANDS = [
    "she is standing at the edge of a volcanic fissure where the heat has exposed layers of ancient civilization, with tribal shamans harvesting strange metals from the molten earth to forge mysterious weapons",
    "she is navigating across a landscape of hardened lava flows that have consumed an entire city, with only the tallest structures still visible above the black rock",
    "she is climbing a hill of volcanic ash that has buried an ancient industrial complex, where steam still escapes through vents in the ground",
    "she is moving carefully across a field of bubbling mud pots that have formed in what was once a downtown area, the foundations of buildings creating patterns in the geothermal features",
    "she is sheltering from ash fall in the remains of a reinforced building, its walls now serving as protection for a tribe that harvests obsidian from the surrounding lava fields",
    "she is standing atop a ridge overlooking a valley where new volcanoes have burst through the remains of an ancient highway system, their lava flows creating rivers of fire",
    "she is examining tribal tools crafted from a strange alloy formed when volcanic heat melted together ancient technologies with natural minerals",
    "she is crossing a narrow stone bridge over a river of molten lava, the bridge formed from the remains of a fallen skyscraper that now connects two tribal territories",
    "she is observing a tribal ritual conducted around a mysterious technological artifact that was exposed when the earth split open during a volcanic eruption",
    "she is navigating through a forest of strange crystal formations that have grown where volcanic gases interact with the ruins of an ancient chemical plant",
    "she is standing before a massive wall of obsidian that has formed where lava engulfed an ancient dam, its black surface now carved with tribal histories",
    "she is moving through a labyrinth of steam vents and hot springs that have formed in the ruins of an ancient subway system, now used for tribal purification rituals",
    "she is climbing the side of a new mountain formed when volcanic activity lifted an entire section of ancient city upward, creating terraced ruins that spiral to the summit",
    "she is sheltering in a cave formed when lava flowed around a buried bunker, the ancient technological remnants inside now worshipped as tribal relics",
    "she is crossing a vast plain of cracked earth where geysers erupt unpredictably from what were once sewer systems, creating an ever-changing landscape of steam and water",
    "she is navigating around a massive crater lake formed in the impact zone of an ancient industrial disaster, its waters now strangely colored and home to unique lifeforms",
    "she is examining strange metallic flows where a volcanic eruption has melted an ancient weapons cache, creating rivers of steel and aluminum",
    "she is following a tribal hunting party across fields of black glass formed when volcanic heat fused the remains of an ancient city, creating a treacherous but beautiful landscape",
    "she is standing at the edge of a massive sinkhole where the ground has collapsed into ancient underground structures, revealing a complex network now filled with volcanic gases",
    "she is moving cautiously across a terrain of sharp volcanic rock that has formed around the twisted metal skeletons of ancient transportation networks"
]

# Theme 6: Neo-Primitive Coastlines
NEO_PRIMITIVE_COASTLINES = [
    "she is perched on a cliff overlooking a new coastline, where the sea has reclaimed the land and primitive fishing vessels made from ancient plastics and metals navigate between the coral-encrusted tops of submerged skyscrapers",
    "she is walking along a beach where the sand is mixed with pulverized concrete and glass from ancient buildings, now polished smooth by millennia of waves",
    "she is exploring a series of tribal dwellings built into the remains of a coastal highway, now perched on the edge of a cliff formed by rising sea levels",
    "she is navigating through a mangrove forest that has grown up through the ruins of a sunken city, with strange fruits growing from trees rooted in ancient apartments",
    "she is standing on the deck of an ancient aircraft carrier, now permanently grounded on a new beach and serving as the foundation for an entire fishing village",
    "she is examining tribal fishing nets made from scavenged cables and wires, used to harvest strange new sea creatures that swim among the sunken ruins",
    "she is climbing a lighthouse now located miles inland, serving as a tribal lookout tower for a society that still remembers when the waters came",
    "she is moving along a new coastline where massive sea walls once protected ancient cities, now forming artificial reefs visible at low tide",
    "she is observing a tribal ceremony conducted at the edge of the water, where offerings are made to the ancient structures visible beneath the waves",
    "she is navigating through a series of tidal pools formed in the remains of a coastal resort, each pool home to unique ecosystems and considered sacred by local tribes",
    "she is standing on a natural bridge formed when sea levels rose around a tall skyscraper, its upper floors now connecting two islands that were once hill tops",
    "she is sheltering from a storm in the remains of a coastal bunker, now half-submerged and home to a tribe that worships the ancient weather prediction machines still visible inside",
    "she is crossing between islands that were once mountaintops, using primitive boats to navigate the channels between what used to be valleys",
    "she is examining strange hybrid sea creatures caught in tribal fish traps, animals that have evolved to incorporate plastics and metals from the sunken civilization",
    "she is moving through a coastal cave system that was once a subway tunnel, now partially flooded and leading to hidden tribal settlements",
    "she is standing on the edge of a massive whirlpool formed where the sea has found its way into deep underground structures, creating a perpetual vortex feared by local tribes",
    "she is navigating along a beach of strange black sand, formed from the erosion of an ancient industrial site now being reclaimed by the relentless ocean",
    "she is watching tribal fishermen harvest kelp that grows from the ruins of a sunken oil rig, its massive structure now a thriving artificial reef",
    "she is exploring the upper floors of a partially submerged skyscraper, now home to nesting seabirds and tribal shamans who communicate with these winged messengers",
    "she is crossing a series of floating platforms made from ancient debris, connecting a community that lives entirely on the water above what was once a major port city"
]

# Theme 7: Tribal City-States
TRIBAL_CITY_STATES = [
    "she is standing in the central plaza of a neo-primitive city-state, where a tribal king sits upon a throne made from the remains of an ancient aircraft, and warriors with spears tipped with technological fragments guard ancient knowledge repositories",
    "she is moving through a bustling tribal market established in what was once a grand train station, with vendors selling goods crafted from scavenged materials",
    "she is navigating the hierarchical levels of a tribal city built within a skyscraper, where social status is determined by which floor one inhabits",
    "she is observing a council meeting of tribal elders in what was once a corporate boardroom, its technology long dead but its authority still respected",
    "she is climbing the ceremonial steps to a temple built atop an ancient power plant, where technological fragments are worshipped and a mysterious light still glows in the depths",
    "she is moving through narrow streets formed between repurposed shipping containers, now a warren of tribal dwellings in a thriving port city-state",
    "she is standing in an arena where tribal champions compete with weapons fashioned from ancient technology, cheered on by crowds seated in what was once a baseball stadium",
    "she is navigating through a tribal city where water is distributed through repurposed ancient plumbing, controlled by a priest class who guard the secrets of pressure and flow",
    "she is examining ancient texts in a tribal library established in what was once a university, where fragments of old knowledge are preserved but often misinterpreted",
    "she is passing through massive gates made from the remains of public transit vehicles, marking the boundary between rival city-states built in adjacent districts of an ancient metropolis",
    "she is observing a class of young tribal members being taught to decipher ancient writing systems, seated in the remains of what was once an elementary school",
    "she is moving carefully through a tribal palace built within a museum, where ancient artifacts are displayed as symbols of the chief's connection to the old gods",
    "she is standing in a vast ceremonial space that was once a shopping mall atrium, now draped with tribal banners and dominated by a massive totem pole made from technological debris",
    "she is navigating the political tensions between the tribe that controls the ancient water treatment facility and those who manage the surrounding agricultural terraces",
    "she is witnessing a ritual exchange of technological artifacts between representatives of tribal city-states, each item a symbol of power and ancient connection",
    "she is moving through a city built in the shell of an ancient sports dome, its tribal society structured around teams competing for resources and territory",
    "she is standing before the tribal justice council that meets in what was once a courthouse, its laws a mixture of ancient precedent and new tribal tradition",
    "she is examining the work of tribal artisans who craft beautiful objects from ancient electronic components, creating a new aesthetic from the remnants of the past",
    "she is observing the night watchmen of a tribal city as they patrol the walls made from stacked vehicles, keeping eye for rival tribes and strange beasts that roam the darkness",
    "she is participating in a harvest festival held in a tribal city-state built around an ancient agricultural research facility, where hybrid crops are grown using a mixture of old science and new ritual"
]

# Theme 8: Mutated Wetlands
MUTATED_WETLANDS = [
    "she is carefully traversing a vibrant, mutated swamp where strange luminescent plants grow from the ruins of an ancient industrial complex, and massive amphibious creatures with multiple limbs lurk beneath the iridescent waters",
    "she is moving along a network of elevated pathways built above a flooded urban area, where bizarre hybrid plant-buildings rise from the murky waters below",
    "she is navigating through a dense mangrove forest that has evolved to incorporate metallic elements into its structure, creating living bridges between half-submerged ruins",
    "she is examining strange flowering plants that grow from the remains of an ancient chemical plant, their blooms emitting a soft blue glow at night",
    "she is crossing a series of stepping stones that were once the tops of buried cars, now providing the only safe passage across a bog filled with carnivorous vegetation",
    "she is standing on the shore of a wetland where the water periodically changes color due to ancient industrial chemicals leaching from submerged ruins",
    "she is harvesting medicinal plants that grow only on the partially submerged remains of an ancient hospital, now a sacred site for tribal healers",
    "she is moving carefully through a foggy marsh where massive fungi sprout from the remains of ancient structures, their caps forming a bizarre secondary canopy",
    "she is navigating by the light of bioluminescent algae that covers the surface of a flooded city center, its patterns revealing the street grid below",
    "she is observing tribal fishermen who have adapted to catch the strange, multi-eyed fish that swim through the sunken remains of an ancient aquarium",
    "she is sheltering from acid rain beneath massive lily pads that have evolved to grow from the sunroofs of buried vehicles",
    "she is crossing a natural bridge formed by the tangled roots of mutated trees that have grown together around a collapsed highway overpass",
    "she is examining tribal totems made from the skulls of unknown creatures, displayed at the boundaries of territories within the dangerous wetlands",
    "she is navigating through a series of flooded subway tunnels, now home to bioluminescent eels that tribal hunters track for their valuable glowing organs",
    "she is standing at the edge of a whirlpool formed where floodwaters continuously drain into a subterranean shopping mall, creating a dangerous but resource-rich diving spot",
    "she is moving between islands of debris that float on the surface of a wetland, each one a micro-ecosystem supporting unique mutated life forms",
    "she is observing tribal wetland dwellers who have adapted physically to their environment, with webbed fingers and specialized lungs to filter the strange air",
    "she is navigating through a swamp where trees bear fruit containing preserved fragments of ancient technology, considered sacred by the tribes who harvest them",
    "she is crossing a marsh on a boat made from ancient synthetic materials, the only substances that resist the corrosive properties of the evolving waters",
    "she is exploring the partially submerged remains of a water treatment plant, now home to a colony of intelligent amphibious creatures that trade with local human tribes"
]

# Theme 9: Highland Strongholds
HIGHLAND_STRONGHOLDS = [
    "she is approaching a stronghold built into a mountainside, where primitive tribespeople have built dwellings around a still-functioning ancient weather station, worshipping the occasional lights and sounds it produces as messages from the gods",
    "she is climbing a narrow path cut into the face of a cliff, passing tribal dwellings built into and around the remains of a luxury mountainside hotel",
    "she is navigating the terraced agricultural plots built on the ruins of a mountain military base, where strange plants grow from soil mixed with technological debris",
    "she is standing at the entrance to a tribal citadel built around a massive satellite dish, now decorated with tribal symbols and serving as the focus of religious ceremonies",
    "she is moving through the fortified gates of a highland community that has repurposed an ancient ski resort, its chair lifts now serving as a primitive transport system",
    "she is observing tribal sentries who keep watch from towers built atop the remains of high-voltage transmission pylons, using mirrors to signal between mountain peaks",
    "she is examining the ingenious water collection system built by highland tribes, incorporating ancient gutters and pipes from the ruins they've built upon",
    "she is navigating through a network of caves that were once part of a mountain research facility, now home to tribal elders who guard ancient technological artifacts",
    "she is standing on a platform overlooking a vast valley, built upon the remains of a mountain observatory where tribal astronomers still track the stars",
    "she is moving carefully through a highland marketplace established in what was once a mountain tunnel system, its walls now covered with tribal artwork depicting the history of their sky-dwelling gods",
    "she is sheltering from a storm in a tribal longhouse built from the remains of a crashed aircraft, its metal skin repurposed to create a dwelling that clings to the mountainside",
    "she is climbing the ceremonial steps to a tribal temple built around a massive antenna array, where shamans interpret the static from ancient receivers as the voices of ancestors",
    "she is crossing a rope bridge that connects twin tribal fortresses built on adjacent peaks, the bridge made from cables salvaged from an ancient ski lift",
    "she is examining tribal hunting weapons crafted from a strange lightweight metal found only in the ruins of a highland research station",
    "she is navigating through the levels of a tribal stronghold built inside a mountain that was once hollowed out for a luxury bunker, its security doors now serving as sacred boundaries",
    "she is standing before a tribal council that meets in what was once a mountain command center, seated in a circle around a dead but still revered control panel",
    "she is observing the careful work of tribal builders who incorporate pieces of ancient solar panels into their roof designs, believing they capture not just light but spiritual energy",
    "she is moving through a highland village built along the edge of a crater formed by some ancient catastrophe, now considered the sacred birthplace of their tribe",
    "she is navigating the complex social hierarchy of a mountain community divided between those who live in the repurposed luxury penthouses at the peak and those dwelling in the lower service levels",
    "she is examining strange wind instruments played by tribal musicians, crafted from the ventilation systems of the ancient mountain facility their community now inhabits"
]

# Theme 10: Ancient Power Sites
ANCIENT_POWER_SITES = [
    "she is walking through an ancient power facility where primitive tribes have built a whole religion around the occasional bursts of electricity that still surge through the partially functioning systems, with shamans interpreting the flickering lights as omens",
    "she is moving cautiously around a massive nuclear cooling tower, now a tribal temple where rituals are performed around a central altar made from control panels",
    "she is navigating through a forest of solar panels, some still functioning sporadically, venerated by the tribal community that harvests the mysterious energy they produce",
    "she is standing before a tribal shrine built around a still-humming transformer box, offerings of technological artifacts arranged around its base",
    "she is observing a coming-of-age ritual where young tribal members must spend a night alone in the control room of an ancient hydroelectric dam, listening for the voices of the ancestors in the creaking machinery",
    "she is examining tribal markings that warn of invisible dangers in areas where ancient radiation still lingers, their symbols a mixture of hazard warnings and spiritual prohibition",
    "she is moving through a series of chambers in what was once a geothermal plant, now a tribal bathhouse where the naturally heated waters are believed to have healing properties",
    "she is navigating the dangerous territory around an ancient power line corridor, where towers have fallen to create a maze of metal, still occasionally conducting electricity after rainstorms",
    "she is standing on a platform overlooking a valley filled with wind turbines, some still spinning and considered by local tribes to be ancestors frozen in an eternal dance",
    "she is sheltering from a storm in a tribal dwelling built inside a massive generator housing, its walls lined with copper wire believed to ward off evil spirits",
    "she is examining strange mutations in plants that grow around the base of an ancient power station, harvested by tribal healers for their unique medicinal properties",
    "she is moving carefully through a tribal marketplace established in a tangle of electrical infrastructure, where vendors sell amulets made from circuit boards and copper wire",
    "she is observing a tribal shaman who communicates with the spirits by touching different parts of an ancient control panel, interpreting the occasional lights and sounds as responses",
    "she is navigating through a series of chambers beneath an ancient solar farm, where mirrors still occasionally focus light into blinding beams considered manifestations of deity",
    "she is standing at the center of a tribal ritual circle built around a still-functioning backup generator, which roars to life during electrical storms and is worshipped as a thunder god",
    "she is crossing a valley where ancient power lines have fallen to create a web-like pattern on the ground, now a sacred labyrinth that tribal members must navigate during initiation rites",
    "she is examining tribal artwork that depicts the mythological history of their people, showing ancient beings commanding the power of lightning and fire from control panels",
    "she is moving through a settlement built in the shadow of massive power plant cooling stacks, where the occasional steam release is treated as a blessing from the ancestors",
    "she is observing tribal craftspeople who work with salvaged copper and aluminum from power infrastructure, believing these metals connect them to the energy of the ancient ones",
    "she is navigating through a forest where trees have grown around fallen power lines, creating strange metal-wood hybrid structures worshipped as nature spirits merged with ancient technology"
]

# Dictionary to hold all themes
themes = {
    "ruinsofancients": RUINS_OF_ANCIENTS,
    "newiceterritories": NEW_ICE_TERRITORIES,
    "greatdesertexpansions": GREAT_DESERT_EXPANSIONS,
    "reclaimedforests": RECLAIMED_FORESTS,
    "volcanicbadlands": VOLCANIC_BADLANDS,
    "neoprimitivecoastlines": NEO_PRIMITIVE_COASTLINES,
    "tribalcitystates": TRIBAL_CITY_STATES,
    "mutatedwetlands": MUTATED_WETLANDS,
    "highlandstrongholds": HIGHLAND_STRONGHOLDS,
    "ancientpowersites": ANCIENT_POWER_SITES
}

# Create prompt files for each theme
for theme_name, captions in themes.items():
    filename = f"sharona-prompts-{theme_name}-{TIMESTAMP}.txt"
    with open(filename, "w") as f:
        for caption in captions:
            prompt = f"{PROMPT_TYPE}, {CHARACTER_DESCRIPTION}, {caption}, {PROMPT_STYLE}."
            f.write(prompt + "\n")
    print(f"Created {filename} with {len(captions)} prompts")

print("All prompt files have been generated successfully!")
