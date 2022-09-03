class pokemon():

	def __init__(self):

		self.special_types = [ 'Alolan', 'Galarian', 'Snowy', 'Rainy', 'Sunny', 'Normal', 'Baile', 'Pom-pom', "Pa'u", 'Sensu', 'Hisuian', 'Origin' ]

		self.pokemon_in_game = {

			#Kanto Pokemon

			'Bulbasaur': ('Kanto', 'Common'),
			'Ivysaur': ('Kanto', 'Common'),
			'Venusaur': ('Kanto', 'Common'),
			'Charmander': ('Kanto', 'Common'),
			'Charmeleon': ('Kanto', 'Common'),
			'Charizard': ('Kanto', 'Common'),
			'Squirtle': ('Kanto', 'Common'),
			'Wartortle': ('Kanto', 'Common'),
			'Blastoise': ('Kanto', 'Common'),
			'Caterpie': ('Kanto', 'Common'),
			'Metapod': ('Kanto', 'Common'),
			'Butterfree': ('Kanto', 'Common'),
			'Weedle': ('Kanto', 'Common'),
			'Kakuna': ('Kanto', 'Common'),
			'Beedrill': ('Kanto', 'Common'),
			'Pidgey': ('Kanto', 'Common'),
			'Pidgeotto': ('Kanto', 'Common'),
			'Pidgeot': ('Kanto', 'Common'),
			'Rattata': ('Kanto', 'Common'),
			'Raticate': ('Kanto', 'Common'),
			'Spearow': ('Kanto', 'Common'),
			'Fearow': ('Kanto', 'Common'),
			'Ekans': ('Kanto', 'Common'),
			'Arbok': ('Kanto', 'Common'),
			'Pikachu': ('Kanto', 'Common'),
			'Raichu': ('Kanto', 'Common'),
			'Sandshrew': ('Kanto', 'Common'),
			'Sandslash': ('Kanto', 'Common'),
			'Nidoran♀️': ('Kanto', 'Common'),
			'Nidorina': ('Kanto', 'Common'),
			'Nidoqueen': ('Kanto', 'Common'),
			'Nidoran♂️': ('Kanto', 'Common'),
			'Nidorino': ('Kanto', 'Common'),
			'Nidoking': ('Kanto', 'Common'),
			'Clefairy': ('Kanto', 'Common'),
			'Clefable': ('Kanto', 'Common'),
			'Vulpix': ('Kanto', 'Common'),
			'Ninetales': ('Kanto', 'Common'),
			'Jigglypuff': ('Kanto', 'Common'),
			'Wigglytuff': ('Kanto', 'Common'),
			'Zubat': ('Kanto', 'Common'),
			'Golbat': ('Kanto', 'Common'),
			'Oddish': ('Kanto', 'Common'),
			'Gloom': ('Kanto', 'Common'),
			'Vileplume': ('Kanto', 'Common'),
			'Paras': ('Kanto', 'Common'),
			'Parasect': ('Kanto', 'Common'),
			'Venonat': ('Kanto', 'Common'),
			'Venomoth': ('Kanto', 'Common'),
			'Diglett': ('Kanto', 'Common'),
			'Dugtrio': ('Kanto', 'Common'),
			'Meowth': ('Kanto', 'Common'),
			'Persian': ('Kanto', 'Common'),
			'Psyduck': ('Kanto', 'Common'),
			'Golduck': ('Kanto', 'Common'),
			'Mankey': ('Kanto', 'Common'),
			'Primeape': ('Kanto', 'Common'),
			'Growlithe': ('Kanto', 'Common'),
			'Arcanine': ('Kanto', 'Common'),
			'Poliwag': ('Kanto', 'Common'),
			'Poliwhirl': ('Kanto', 'Common'),
			'Poliwrath': ('Kanto', 'Common'),
			'Abra': ('Kanto', 'Common'),
			'Kadabra': ('Kanto', 'Common'),
			'Alakazam': ('Kanto', 'Common'),
			'Machop': ('Kanto', 'Common'),
			'Machoke': ('Kanto', 'Common'),
			'Machamp': ('Kanto', 'Common'),
			'Bellsprout': ('Kanto', 'Common'),
			'Weepinbell': ('Kanto', 'Common'),
			'Victreebel': ('Kanto', 'Common'),
			'Tentacool': ('Kanto', 'Common'),
			'Tentacruel': ('Kanto', 'Common'),
			'Geodude': ('Kanto', 'Common'),
			'Graveler': ('Kanto', 'Common'),
			'Golem': ('Kanto', 'Common'),
			'Ponyta': ('Kanto', 'Common'),
			'Rapidash': ('Kanto', 'Common'),
			'Slowpoke': ('Kanto', 'Common'),
			'Slowbro': ('Kanto', 'Common'),
			'Magnemite': ('Kanto', 'Common'),
			'Magneton': ('Kanto', 'Common'),
			"Farfetch'd": ('Kanto', 'Common'),
			'Doduo': ('Kanto', 'Common'),
			'Dodrio': ('Kanto', 'Common'),
			'Seel': ('Kanto', 'Common'),
			'Dewgong': ('Kanto', 'Common'),
			'Grimer': ('Kanto', 'Common'),
			'Muk': ('Kanto', 'Common'),
			'Shellder': ('Kanto', 'Common'),
			'Cloyster': ('Kanto', 'Common'),
			'Gastly': ('Kanto', 'Common'),
			'Haunter': ('Kanto', 'Common'),
			'Gengar': ('Kanto', 'Common'),
			'Onix': ('Kanto', 'Common'),
			'Drowzee': ('Kanto', 'Common'),
			'Hypno': ('Kanto', 'Common'),
			'Krabby': ('Kanto', 'Common'),
			'Kingler': ('Kanto', 'Common'),
			'Voltorb': ('Kanto', 'Common'),
			'Electrode': ('Kanto', 'Common'),
			'Exeggcute': ('Kanto', 'Common'),
			'Exeggutor': ('Kanto', 'Common'),
			'Cubone': ('Kanto', 'Common'),
			'Marowak': ('Kanto', 'Common'),
			'Hitmonlee': ('Kanto', 'Common'),
			'Hitmonchan': ('Kanto', 'Common'),
			'Lickitung': ('Kanto', 'Common'),
			'Koffing': ('Kanto', 'Common'),
			'Weezing': ('Kanto', 'Common'),
			'Rhyhorn': ('Kanto', 'Common'),
			'Rhydon': ('Kanto', 'Common'),
			'Chansey': ('Kanto', 'Common'),
			'Tangela': ('Kanto', 'Common'),
			'Kangaskhan': ('Kanto', 'Common'),
			'Horsea': ('Kanto', 'Common'),
			'Seadra': ('Kanto', 'Common'),
			'Goldeen': ('Kanto', 'Common'),
			'Seaking': ('Kanto', 'Common'),
			'Staryu': ('Kanto', 'Common'),
			'Starmie': ('Kanto', 'Common'),
			'Mr. Mime': ('Kanto', 'Common'),
			'Scyther': ('Kanto', 'Common'),
			'Jynx': ('Kanto', 'Common'),
			'Electabuzz': ('Kanto', 'Common'),
			'Magmar': ('Kanto', 'Common'),
			'Pinsir': ('Kanto', 'Common'),
			'Tauros': ('Kanto', 'Common'),
			'Magikarp': ('Kanto', 'Common'),
			'Gyarados': ('Kanto', 'Common'),
			'Lapras': ('Kanto', 'Common'),
			'Ditto': ('Kanto', 'Common'),
			'Eevee': ('Kanto', 'Common'),
			'Vaporeon': ('Kanto', 'Common'),
			'Jolteon': ('Kanto', 'Common'),
			'Flareon': ('Kanto', 'Common'),
			'Porygon': ('Kanto', 'Common'),
			'Omanyte': ('Kanto', 'Common'),
			'Omastar': ('Kanto', 'Common'),
			'Kabuto': ('Kanto', 'Common'),
			'Kabutops': ('Kanto', 'Common'),
			'Aerodactyl': ('Kanto', 'Common'),
			'Snorlax': ('Kanto', 'Common'),
			'Articuno': ('Kanto', 'Legendary'),
			'Zapdos': ('Kanto', 'Legendary'),
			'Moltres': ('Kanto', 'Legendary'),
			'Dratini': ('Kanto', 'Common'),
			'Dragonair': ('Kanto', 'Common'),
			'Dragonite': ('Kanto', 'Common'),
			'Mewtwo': ('Kanto', 'Legendary'),
			'Mew': ('Kanto', 'Mythical'),

			#Johto Pokemon
			'Chikorita': ('Johto', 'Common'),
			'Bayleef': ('Johto', 'Common'),
			'Meganium': ('Johto', 'Common'),
			'Cyndaquil': ('Johto', 'Common'),
			'Quilava': ('Johto', 'Common'),
			'Typhlosion': ('Johto', 'Common'),
			'Totodile': ('Johto', 'Common'),
			'Croconaw': ('Johto', 'Common'),
			'Feraligatr': ('Johto', 'Common'),
			'Sentret': ('Johto', 'Common'),
			'Furret': ('Johto', 'Common'),
			'Hoothoot': ('Johto', 'Common'),
			'Noctowl': ('Johto', 'Common'),
			'Ledyba': ('Johto', 'Common'),
			'Ledian': ('Johto', 'Common'),
			'Spinarak': ('Johto', 'Common'),
			'Ariados': ('Johto', 'Common'),
			'Crobat': ('Johto', 'Common'),
			'Chinchou': ('Johto', 'Common'),
			'Lanturn': ('Johto', 'Common'),
			'Pichu': ('Johto', 'Common'),
			'Cleffa': ('Johto', 'Common'),
			'Igglybuff': ('Johto', 'Common'),
			'Togepi': ('Johto', 'Common'),
			'Togetic': ('Johto', 'Common'),
			'Natu': ('Johto', 'Common'),
			'Xatu': ('Johto', 'Common'),
			'Mareep': ('Johto', 'Common'),
			'Flaaffy': ('Johto', 'Common'),
			'Ampharos': ('Johto', 'Common'),
			'Bellossom': ('Johto', 'Common'),
			'Marill': ('Johto', 'Common'),
			'Azumarill': ('Johto', 'Common'),
			'Sudowoodo': ('Johto', 'Common'),
			'Politoed': ('Johto', 'Common'),
			'Hoppip': ('Johto', 'Common'),
			'Skiploom': ('Johto', 'Common'),
			'Jumpluff': ('Johto', 'Common'),
			'Aipom': ('Johto', 'Common'),
			'Sunkern': ('Johto', 'Common'),
			'Sunflora': ('Johto', 'Common'),
			'Yanma': ('Johto', 'Common'),
			'Wooper': ('Johto', 'Common'),
			'Quagsire': ('Johto', 'Common'),
			'Espeon': ('Johto', 'Common'),
			'Umbreon': ('Johto', 'Common'),
			'Murkrow': ('Johto', 'Common'),
			'Slowking': ('Johto', 'Common'),
			'Misdreavus': ('Johto', 'Common'),
			'Unown': ('Johto', 'Common'),
			'Wobbuffet': ('Johto', 'Common'),
			'Girafarig': ('Johto', 'Common'),
			'Pineco': ('Johto', 'Common'),
			'Forretress': ('Johto', 'Common'),
			'Dunsparce': ('Johto', 'Common'),
			'Gligar': ('Johto', 'Common'),
			'Steelix': ('Johto', 'Common'),
			'Snubbull': ('Johto', 'Common'),
			'Granbull': ('Johto', 'Common'),
			'Qwilfish': ('Johto', 'Common'),
			'Scizor': ('Johto', 'Common'),
			'Shuckle': ('Johto', 'Common'),
			'Heracross': ('Johto', 'Common'),
			'Sneasel': ('Johto', 'Common'),
			'Teddiursa': ('Johto', 'Common'),
			'Ursaring': ('Johto', 'Common'),
			'Slugma': ('Johto', 'Common'),
			'Magcargo': ('Johto', 'Common'),
			'Swinub': ('Johto', 'Common'),
			'Piloswine': ('Johto', 'Common'),
			'Corsola': ('Johto', 'Common'),
			'Remoraid': ('Johto', 'Common'),
			'Octillery': ('Johto', 'Common'),
			'Delibird': ('Johto', 'Common'),
			'Mantine': ('Johto', 'Common'),
			'Skarmory': ('Johto', 'Common'),
			'Houndour': ('Johto', 'Common'),
			'Houndoom': ('Johto', 'Common'),
			'Kingdra': ('Johto', 'Common'),
			'Phanpy': ('Johto', 'Common'),
			'Donphan': ('Johto', 'Common'),
			'Porygon2': ('Johto', 'Common'),
			'Stantler': ('Johto', 'Common'),
			'Smeargle': ('Johto', 'Common'),
			'Tyrogue': ('Johto', 'Common'),
			'Hitmontop': ('Johto', 'Common'),
			'Smoochum': ('Johto', 'Common'),
			'Elekid': ('Johto', 'Common'),
			'Magby': ('Johto', 'Common'),
			'Miltank': ('Johto', 'Common'),
			'Blissey': ('Johto', 'Common'),
			'Raikou': ('Johto', 'Legendary'),
			'Entei': ('Johto', 'Legendary'),
			'Suicune': ('Johto', 'Legendary'),
			'Larvitar': ('Johto', 'Common'),
			'Pupitar': ('Johto', 'Common'),
			'Tyranitar': ('Johto', 'Common'),
			'Lugia': ('Johto', 'Legendary'),
			'Ho-Oh': ('Johto', 'Legendary'),
			'Celebi': ('Johto', 'Mythical'),

			#Hoenn Pokemon
			'Treecko': ('Hoenn', 'Common'),
			'Grovyle': ('Hoenn', 'Common'),
			'Sceptile': ('Hoenn', 'Common'),
			'Torchic': ('Hoenn', 'Common'),
			'Combusken': ('Hoenn', 'Common'),
			'Blaziken': ('Hoenn', 'Common'),
			'Mudkip': ('Hoenn', 'Common'),
			'Marshtomp': ('Hoenn', 'Common'),
			'Swampert': ('Hoenn', 'Common'),
			'Poochyena': ('Hoenn', 'Common'),
			'Mightyena': ('Hoenn', 'Common'),
			'Zigzagoon': ('Hoenn', 'Common'),
			'Linoone': ('Hoenn', 'Common'),
			'Wurmple': ('Hoenn', 'Common'),
			'Silcoon': ('Hoenn', 'Common'),
			'Beautifly': ('Hoenn', 'Common'),
			'Cascoon': ('Hoenn', 'Common'),
			'Dustox': ('Hoenn', 'Common'),
			'Lotad': ('Hoenn', 'Common'),
			'Lombre': ('Hoenn', 'Common'),
			'Ludicolo': ('Hoenn', 'Common'),
			'Seedot': ('Hoenn', 'Common'),
			'Nuzleaf': ('Hoenn', 'Common'),
			'Shiftry': ('Hoenn', 'Common'),
			'Taillow': ('Hoenn', 'Common'),
			'Swellow': ('Hoenn', 'Common'),
			'Wingull': ('Hoenn', 'Common'),
			'Pelipper': ('Hoenn', 'Common'),
			'Ralts': ('Hoenn', 'Common'),
			'Kirlia': ('Hoenn', 'Common'),
			'Gardevoir': ('Hoenn', 'Common'),
			'Surskit': ('Hoenn', 'Common'),
			'Masquerain': ('Hoenn', 'Common'),
			'Shroomish': ('Hoenn', 'Common'),
			'Breloom': ('Hoenn', 'Common'),
			'Slakoth': ('Hoenn', 'Common'),
			'Vigoroth': ('Hoenn', 'Common'),
			'Slaking': ('Hoenn', 'Common'),
			'Nincada': ('Hoenn', 'Common'),
			'Ninjask': ('Hoenn', 'Common'),
			'Shedinja': ('Hoenn', 'Common'),
			'Whismur': ('Hoenn', 'Common'),
			'Loudred': ('Hoenn', 'Common'),
			'Exploud': ('Hoenn', 'Common'),
			'Makuhita': ('Hoenn', 'Common'),
			'Hariyama': ('Hoenn', 'Common'),
			'Azurill': ('Hoenn', 'Common'),
			'Nosepass': ('Hoenn', 'Common'),
			'Skitty': ('Hoenn', 'Common'),
			'Delcatty': ('Hoenn', 'Common'),
			'Sableye': ('Hoenn', 'Common'),
			'Mawile': ('Hoenn', 'Common'),
			'Aron': ('Hoenn', 'Common'),
			'Lairon': ('Hoenn', 'Common'),
			'Aggron': ('Hoenn', 'Common'),
			'Meditite': ('Hoenn', 'Common'),
			'Medicham': ('Hoenn', 'Common'),
			'Electrike': ('Hoenn', 'Common'),
			'Manectric': ('Hoenn', 'Common'),
			'Plusle': ('Hoenn', 'Common'),
			'Minun': ('Hoenn', 'Common'),
			'Volbeat': ('Hoenn', 'Common'),
			'Illumise': ('Hoenn', 'Common'),
			'Roselia': ('Hoenn', 'Common'),
			'Gulpin': ('Hoenn', 'Common'),
			'Swalot': ('Hoenn', 'Common'),
			'Carvanha': ('Hoenn', 'Common'),
			'Sharpedo': ('Hoenn', 'Common'),
			'Wailmer': ('Hoenn', 'Common'),
			'Wailord': ('Hoenn', 'Common'),
			'Numel': ('Hoenn', 'Common'),
			'Camerupt': ('Hoenn', 'Common'),
			'Torkoal': ('Hoenn', 'Common'),
			'Spoink': ('Hoenn', 'Common'),
			'Grumpig': ('Hoenn', 'Common'),
			'Spinda': ('Hoenn', 'Common'),
			'Trapinch': ('Hoenn', 'Common'),
			'Vibrava': ('Hoenn', 'Common'),
			'Flygon': ('Hoenn', 'Common'),
			'Cacnea': ('Hoenn', 'Common'),
			'Cacturne': ('Hoenn', 'Common'),
			'Swablu': ('Hoenn', 'Common'),
			'Altaria': ('Hoenn', 'Common'),
			'Zangoose': ('Hoenn', 'Common'),
			'Seviper': ('Hoenn', 'Common'),
			'Lunatone': ('Hoenn', 'Common'),
			'Solrock': ('Hoenn', 'Common'),
			'Barboach': ('Hoenn', 'Common'),
			'Whiscash': ('Hoenn', 'Common'),
			'Corphish': ('Hoenn', 'Common'),
			'Crawdaunt': ('Hoenn', 'Common'),
			'Baltoy': ('Hoenn', 'Common'),
			'Claydol': ('Hoenn', 'Common'),
			'Lileep': ('Hoenn', 'Common'),
			'Cradily': ('Hoenn', 'Common'),
			'Anorith': ('Hoenn', 'Common'),
			'Armaldo': ('Hoenn', 'Common'),
			'Feebas': ('Hoenn', 'Common'),
			'Milotic': ('Hoenn', 'Common'),
			'Castform': ('Hoenn', 'Common'),
			'Kecleon': ('Hoenn', 'Common'),
			'Shuppet': ('Hoenn', 'Common'),
			'Banette': ('Hoenn', 'Common'),
			'Duskull': ('Hoenn', 'Common'),
			'Dusclops': ('Hoenn', 'Common'),
			'Tropius': ('Hoenn', 'Common'),
			'Chimecho': ('Hoenn', 'Common'),
			'Absol': ('Hoenn', 'Common'),
			'Wynaut': ('Hoenn', 'Common'),
			'Snorunt': ('Hoenn', 'Common'),
			'Glalie': ('Hoenn', 'Common'),
			'Spheal': ('Hoenn', 'Common'),
			'Sealeo': ('Hoenn', 'Common'),
			'Walrein': ('Hoenn', 'Common'),
			'Clamperl': ('Hoenn', 'Common'),
			'Huntail': ('Hoenn', 'Common'),
			'Gorebyss': ('Hoenn', 'Common'),
			'Relicanth': ('Hoenn', 'Common'),
			'Luvdisc': ('Hoenn', 'Common'),
			'Bagon': ('Hoenn', 'Common'),
			'Shelgon': ('Hoenn', 'Common'),
			'Salamence': ('Hoenn', 'Common'),
			'Beldum': ('Hoenn', 'Common'),
			'Metang': ('Hoenn', 'Common'),
			'Metagross': ('Hoenn', 'Common'),
			'Regirock': ('Hoenn', 'Legendary'),
			'Regice': ('Hoenn', 'Legendary'),
			'Registeel': ('Hoenn', 'Legendary'),
			'Latias': ('Hoenn', 'Legendary'),
			'Latios': ('Hoenn', 'Legendary'),
			'Kyogre': ('Hoenn', 'Legendary'),
			'Groudon': ('Hoenn', 'Legendary'),
			'Rayquaza': ('Hoenn', 'Legendary'),
			'Jirachi': ('Hoenn', 'Mythical'),
			'Deoxys': ('Hoenn', 'Mythical'),

			#Sinnoh Pokemon
			'Turtwig': ('Sinnoh', 'Common'),
			'Grotle': ('Sinnoh', 'Common'),
			'Torterra': ('Sinnoh', 'Common'),
			'Chimchar': ('Sinnoh', 'Common'),
			'Monferno': ('Sinnoh', 'Common'),
			'Infernape': ('Sinnoh', 'Common'),
			'Piplup': ('Sinnoh', 'Common'),
			'Prinplup': ('Sinnoh', 'Common'),
			'Empoleon': ('Sinnoh', 'Common'),
			'Starly': ('Sinnoh', 'Common'),
			'Staravia': ('Sinnoh', 'Common'),
			'Staraptor': ('Sinnoh', 'Common'),
			'Bidoof': ('Sinnoh', 'Common'),
			'Bibarel': ('Sinnoh', 'Common'),
			'Kricketot': ('Sinnoh', 'Common'),
			'Kricketune': ('Sinnoh', 'Common'),
			'Shinx': ('Sinnoh', 'Common'),
			'Luxio': ('Sinnoh', 'Common'),
			'Luxray': ('Sinnoh', 'Common'),
			'Budew': ('Sinnoh', 'Common'),
			'Roserade': ('Sinnoh', 'Common'),
			'Cranidos': ('Sinnoh', 'Common'),
			'Rampardos': ('Sinnoh', 'Common'),
			'Shieldon': ('Sinnoh', 'Common'),
			'Bastiodon': ('Sinnoh', 'Common'),
			'Burmy': ('Sinnoh', 'Common'),
			'Wormadam': ('Sinnoh', 'Common'),
			'Mothim': ('Sinnoh', 'Common'),
			'Combee': ('Sinnoh', 'Common'),
			'Vespiquen': ('Sinnoh', 'Common'),
			'Pachirisu': ('Sinnoh', 'Common'),
			'Buizel': ('Sinnoh', 'Common'),
			'Floatzel': ('Sinnoh', 'Common'),
			'Cherubi': ('Sinnoh', 'Common'),
			'Cherrim': ('Sinnoh', 'Common'),
			'Shellos': ('Sinnoh', 'Common'),
			'Gastrodon': ('Sinnoh', 'Common'),
			'Ambipom': ('Sinnoh', 'Common'),
			'Drifloon': ('Sinnoh', 'Common'),
			'Drifblim': ('Sinnoh', 'Common'),
			'Buneary': ('Sinnoh', 'Common'),
			'Lopunny': ('Sinnoh', 'Common'),
			'Mismagius': ('Sinnoh', 'Common'),
			'Honchkrow': ('Sinnoh', 'Common'),
			'Glameow': ('Sinnoh', 'Common'),
			'Purugly': ('Sinnoh', 'Common'),
			'Chingling': ('Sinnoh', 'Common'),
			'Stunky': ('Sinnoh', 'Common'),
			'Skuntank': ('Sinnoh', 'Common'),
			'Bronzor': ('Sinnoh', 'Common'),
			'Bronzong': ('Sinnoh', 'Common'),
			'Bonsly': ('Sinnoh', 'Common'),
			'Mime Jr.': ('Sinnoh', 'Common'),
			'Happiny': ('Sinnoh', 'Common'),
			'Chatot': ('Sinnoh', 'Common'),
			'Spiritomb': ('Sinnoh', 'Common'),
			'Gible': ('Sinnoh', 'Common'),
			'Gabite': ('Sinnoh', 'Common'),
			'Garchomp': ('Sinnoh', 'Common'),
			'Munchlax': ('Sinnoh', 'Common'),
			'Riolu': ('Sinnoh', 'Common'),
			'Lucario': ('Sinnoh', 'Common'),
			'Hippopotas': ('Sinnoh', 'Common'),
			'Hippowdon': ('Sinnoh', 'Common'),
			'Skorupi': ('Sinnoh', 'Common'),
			'Drapion': ('Sinnoh', 'Common'),
			'Croagunk': ('Sinnoh', 'Common'),
			'Toxicroak': ('Sinnoh', 'Common'),
			'Carnivine': ('Sinnoh', 'Common'),
			'Finneon': ('Sinnoh', 'Common'),
			'Lumineon': ('Sinnoh', 'Common'),
			'Mantyke': ('Sinnoh', 'Common'),
			'Snover': ('Sinnoh', 'Common'),
			'Abomasnow': ('Sinnoh', 'Common'),
			'Weavile': ('Sinnoh', 'Common'),
			'Magnezone': ('Sinnoh', 'Common'),
			'Lickilicky': ('Sinnoh', 'Common'),
			'Rhyperior': ('Sinnoh', 'Common'),
			'Tangrowth': ('Sinnoh', 'Common'),
			'Electivire': ('Sinnoh', 'Common'),
			'Magmortar': ('Sinnoh', 'Common'),
			'Togekiss': ('Sinnoh', 'Common'),
			'Yanmega': ('Sinnoh', 'Common'),
			'Leafeon': ('Sinnoh', 'Common'),
			'Glaceon': ('Sinnoh', 'Common'),
			'Gliscor': ('Sinnoh', 'Common'),
			'Mamoswine': ('Sinnoh', 'Common'),
			'Porygon-Z': ('Sinnoh', 'Common'),
			'Gallade': ('Sinnoh', 'Common'),
			'Probopass': ('Sinnoh', 'Common'),
			'Dusknoir': ('Sinnoh', 'Common'),
			'Froslass': ('Sinnoh', 'Common'),
			'Rotom': ('Sinnoh', 'Common'),
			'Uxie': ('Sinnoh', 'Legendary'),
			'Mesprit': ('Sinnoh', 'Legendary'),
			'Azelf': ('Sinnoh', 'Legendary'),
			'Dialga': ('Sinnoh', 'Legendary'),
			'Palkia': ('Sinnoh', 'Legendary'),
			'Heatran': ('Sinnoh', 'Legendary'),
			'Regigigas': ('Sinnoh', 'Legendary'),
			'Giratina': ('Sinnoh', 'Legendary'),
			'Cresselia': ('Sinnoh', 'Legendary'),
			'Phione': ('Sinnoh', 'Mythical'),
			'Manaphy': ('Sinnoh', 'Mythical'),
			'Darkrai': ('Sinnoh', 'Mythical'),
			'Shaymin': ('Sinnoh', 'Mythical'),
			'Arceus': ('Sinnoh', 'Mythical'),

			#Unova Pokemon
			'Victini': ('Unova', 'Mythical'),
			'Snivy': ('Unova', 'Common'),
			'Servine': ('Unova', 'Common'),
			'Serperior': ('Unova', 'Common'),
			'Tepig': ('Unova', 'Common'),
			'Pignite': ('Unova', 'Common'),
			'Emboar': ('Unova', 'Common'),
			'Oshawott': ('Unova', 'Common'),
			'Dewott': ('Unova', 'Common'),
			'Samurott': ('Unova', 'Common'),
			'Patrat': ('Unova', 'Common'),
			'Watchog': ('Unova', 'Common'),
			'Lillipup': ('Unova', 'Common'),
			'Herdier': ('Unova', 'Common'),
			'Stoutland': ('Unova', 'Common'),
			'Purrloin': ('Unova', 'Common'),
			'Liepard': ('Unova', 'Common'),
			'Pansage': ('Unova', 'Common'),
			'Simisage': ('Unova', 'Common'),
			'Pansear': ('Unova', 'Common'),
			'Simisear': ('Unova', 'Common'),
			'Panpour': ('Unova', 'Common'),
			'Simipour': ('Unova', 'Common'),
			'Munna': ('Unova', 'Common'),
			'Musharna': ('Unova', 'Common'),
			'Pidove': ('Unova', 'Common'),
			'Tranquill': ('Unova', 'Common'),
			'Unfezant': ('Unova', 'Common'),
			'Blitzle': ('Unova', 'Common'),
			'Zebstrika': ('Unova', 'Common'),
			'Roggenrola': ('Unova', 'Common'),
			'Boldore': ('Unova', 'Common'),
			'Gigalith': ('Unova', 'Common'),
			'Woobat': ('Unova', 'Common'),
			'Swoobat': ('Unova', 'Common'),
			'Drilbur': ('Unova', 'Common'),
			'Excadrill': ('Unova', 'Common'),
			'Audino': ('Unova', 'Common'),
			'Timburr': ('Unova', 'Common'),
			'Gurdurr': ('Unova', 'Common'),
			'Conkeldurr': ('Unova', 'Common'),
			'Tympole': ('Unova', 'Common'),
			'Palpitoad': ('Unova', 'Common'),
			'Seismitoad': ('Unova', 'Common'),
			'Throh': ('Unova', 'Common'),
			'Sawk': ('Unova', 'Common'),
			'Sewaddle': ('Unova', 'Common'),
			'Swadloon': ('Unova', 'Common'),
			'Leavanny': ('Unova', 'Common'),
			'Venipede': ('Unova', 'Common'),
			'Whirlipede': ('Unova', 'Common'),
			'Scolipede': ('Unova', 'Common'),
			'Cottonee': ('Unova', 'Common'),
			'Whimsicott': ('Unova', 'Common'),
			'Petilil': ('Unova', 'Common'),
			'Lilligant': ('Unova', 'Common'),
			'Basculin': ('Unova', 'Common'),
			'Sandile': ('Unova', 'Common'),
			'Krokorok': ('Unova', 'Common'),
			'Krookodile': ('Unova', 'Common'),
			'Darumaka': ('Unova', 'Common'),
			'Darmanitan': ('Unova', 'Common'),
			'Maractus': ('Unova', 'Common'),
			'Dwebble': ('Unova', 'Common'),
			'Crustle': ('Unova', 'Common'),
			'Scraggy': ('Unova', 'Common'),
			'Scrafty': ('Unova', 'Common'),
			'Sigilyph': ('Unova', 'Common'),
			'Yamask': ('Unova', 'Common'),
			'Cofagrigus': ('Unova', 'Common'),
			'Tirtouga': ('Unova', 'Common'),
			'Carracosta': ('Unova', 'Common'),
			'Archen': ('Unova', 'Common'),
			'Archeops': ('Unova', 'Common'),
			'Trubbish': ('Unova', 'Common'),
			'Garbodor': ('Unova', 'Common'),
			'Zorua': ('Unova', 'Common'),
			'Zoroark': ('Unova', 'Common'),
			'Minccino': ('Unova', 'Common'),
			'Cinccino': ('Unova', 'Common'),
			'Gothita': ('Unova', 'Common'),
			'Gothorita': ('Unova', 'Common'),
			'Gothitelle': ('Unova', 'Common'),
			'Solosis': ('Unova', 'Common'),
			'Duosion': ('Unova', 'Common'),
			'Reuniclus': ('Unova', 'Common'),
			'Ducklett': ('Unova', 'Common'),
			'Swanna': ('Unova', 'Common'),
			'Vanillite': ('Unova', 'Common'),
			'Vanillish': ('Unova', 'Common'),
			'Vanilluxe': ('Unova', 'Common'),
			'Deerling': ('Unova', 'Common'),
			'Sawsbuck': ('Unova', 'Common'),
			'Emolga': ('Unova', 'Common'),
			'Karrablast': ('Unova', 'Common'),
			'Escavalier': ('Unova', 'Common'),
			'Foongus': ('Unova', 'Common'),
			'Amoonguss': ('Unova', 'Common'),
			'Frillish': ('Unova', 'Common'),
			'Jellicent': ('Unova', 'Common'),
			'Alomomola': ('Unova', 'Common'),
			'Joltik': ('Unova', 'Common'),
			'Galvantula': ('Unova', 'Common'),
			'Ferroseed': ('Unova', 'Common'),
			'Ferrothorn': ('Unova', 'Common'),
			'Klink': ('Unova', 'Common'),
			'Klang': ('Unova', 'Common'),
			'Klinklang': ('Unova', 'Common'),
			'Tynamo': ('Unova', 'Common'),
			'Eelektrik': ('Unova', 'Common'),
			'Eelektross': ('Unova', 'Common'),
			'Elgyem': ('Unova', 'Common'),
			'Beheeyem': ('Unova', 'Common'),
			'Litwick': ('Unova', 'Common'),
			'Lampent': ('Unova', 'Common'),
			'Chandelure': ('Unova', 'Common'),
			'Axew': ('Unova', 'Common'),
			'Fraxure': ('Unova', 'Common'),
			'Haxorus': ('Unova', 'Common'),
			'Cubchoo': ('Unova', 'Common'),
			'Beartic': ('Unova', 'Common'),
			'Cryogonal': ('Unova', 'Common'),
			'Shelmet': ('Unova', 'Common'),
			'Accelgor': ('Unova', 'Common'),
			'Stunfisk': ('Unova', 'Common'),
			'Mienfoo': ('Unova', 'Common'),
			'Mienshao': ('Unova', 'Common'),
			'Druddigon': ('Unova', 'Common'),
			'Golett': ('Unova', 'Common'),
			'Golurk': ('Unova', 'Common'),
			'Pawniard': ('Unova', 'Common'),
			'Bisharp': ('Unova', 'Common'),
			'Bouffalant': ('Unova', 'Common'),
			'Rufflet': ('Unova', 'Common'),
			'Braviary': ('Unova', 'Common'),
			'Vullaby': ('Unova', 'Common'),
			'Mandibuzz': ('Unova', 'Common'),
			'Heatmor': ('Unova', 'Common'),
			'Durant': ('Unova', 'Common'),
			'Deino': ('Unova', 'Common'),
			'Zweilous': ('Unova', 'Common'),
			'Hydreigon': ('Unova', 'Common'),
			'Larvesta': ('Unova', 'Common'),
			'Volcarona': ('Unova', 'Common'),
			'Cobalion': ('Unova', 'Legendary'),
			'Terrakion': ('Unova', 'Legendary'),
			'Virizion': ('Unova', 'Legendary'),
			'Tornadus': ('Unova', 'Legendary'),
			'Thundurus': ('Unova', 'Legendary'),
			'Reshiram': ('Unova', 'Legendary'),
			'Zekrom': ('Unova', 'Legendary'),
			'Landorus': ('Unova', 'Legendary'),
			'Kyurem': ('Unova', 'Legendary'),
			'Keldeo': ('Unova', 'Mythical'),
			'Meloetta': ('Unova', 'Mythical'),
			'Genesect': ('Unova', 'Mythical'),

			#Kalos Pokemon
			'Chespin': ('Kalos', 'Common'),
			'Quilladin': ('Kalos', 'Common'),
			'Chesnaught': ('Kalos', 'Common'),
			'Fennekin': ('Kalos', 'Common'),
			'Braixen': ('Kalos', 'Common'),
			'Delphox': ('Kalos', 'Common'),
			'Froakie': ('Kalos', 'Common'),
			'Frogadier': ('Kalos', 'Common'),
			'Greninja': ('Kalos', 'Common'),
			'Bunnelby': ('Kalos', 'Common'),
			'Diggersby': ('Kalos', 'Common'),
			'Fletchling': ('Kalos', 'Common'),
			'Fletchinder': ('Kalos', 'Common'),
			'Talonflame': ('Kalos', 'Common'),
			'Scatterbug': ('Kalos', 'Common'),
			'Spewpa': ('Kalos', 'Common'),
			'Vivillon': ('Kalos', 'Common'),
			'Litleo': ('Kalos', 'Common'),
			'Pyroar': ('Kalos', 'Common'),
			'Flabébé': ('Kalos', 'Common'),
			'Floette': ('Kalos', 'Common'),
			'Florges': ('Kalos', 'Common'),
			'Skiddo': ('Kalos', 'Common'),
			'Gogoat': ('Kalos', 'Common'),
			'Pancham': ('Kalos', 'Common'),
			'Pangoro': ('Kalos', 'Common'),
			'Furfrou': ('Kalos', 'Common'),
			'Espurr': ('Kalos', 'Common'),
			'Meowstic': ('Kalos', 'Common'),
			'Honedge': ('Kalos', 'Common'),
			'Doublade': ('Kalos', 'Common'),
			'Aegislash': ('Kalos', 'Common'),
			'Spritzee': ('Kalos', 'Common'),
			'Aromatisse': ('Kalos', 'Common'),
			'Swirlix': ('Kalos', 'Common'),
			'Slurpuff': ('Kalos', 'Common'),
			'Inkay': ('Kalos', 'Common'),
			'Malamar': ('Kalos', 'Common'),
			'Binacle': ('Kalos', 'Common'),
			'Barbaracle': ('Kalos', 'Common'),
			'Skrelp': ('Kalos', 'Common'),
			'Dragalge': ('Kalos', 'Common'),
			'Clauncher': ('Kalos', 'Common'),
			'Clawitzer': ('Kalos', 'Common'),
			'Helioptile': ('Kalos', 'Common'),
			'Heliolisk': ('Kalos', 'Common'),
			'Tyrunt': ('Kalos', 'Common'),
			'Tyrantrum': ('Kalos', 'Common'),
			'Amaura': ('Kalos', 'Common'),
			'Aurorus': ('Kalos', 'Common'),
			'Sylveon': ('Kalos', 'Common'),
			'Hawlucha': ('Kalos', 'Common'),
			'Dedenne': ('Kalos', 'Common'),
			'Carbink': ('Kalos', 'Common'),
			'Goomy': ('Kalos', 'Common'),
			'Sliggoo': ('Kalos', 'Common'),
			'Goodra': ('Kalos', 'Common'),
			'Klefki': ('Kalos', 'Common'),
			'Phantump': ('Kalos', 'Common'),
			'Trevenant': ('Kalos', 'Common'),
			'Pumpkaboo': ('Kalos', 'Common'),
			'Gourgeist': ('Kalos', 'Common'),
			'Bergmite': ('Kalos', 'Common'),
			'Avalugg': ('Kalos', 'Common'),
			'Noibat': ('Kalos', 'Common'),
			'Noivern': ('Kalos', 'Common'),
			'Xerneas': ('Kalos', 'Legendary'),
			'Yveltal': ('Kalos', 'Legendary'),
			'Zygarde': ('Kalos', 'Legendary'),
			'Diancie': ('Kalos', 'Mythical'),
			'Hoopa': ('Kalos', 'Mythical'),
			'Volcanion': ('Kalos', 'Mythical'),

			#Alola Pokemon
			'Rowlet': ('Alola', 'Common'),
			'Dartrix': ('Alola', 'Common'),
			'Decidueye': ('Alola', 'Common'),
			'Litten': ('Alola', 'Common'),
			'Torracat': ('Alola', 'Common'),
			'Incineroar': ('Alola', 'Common'),
			'Popplio': ('Alola', 'Common'),
			'Brionne': ('Alola', 'Common'),
			'Primarina': ('Alola', 'Common'),
			'Pikipek': ('Alola', 'Common'),
			'Trumbeak': ('Alola', 'Common'),
			'Toucannon': ('Alola', 'Common'),
			'Yungoos': ('Alola', 'Common'),
			'Gumshoos': ('Alola', 'Common'),
			'Grubbin': ('Alola', 'Common'),
			'Charjabug': ('Alola', 'Common'),
			'Vikavolt': ('Alola', 'Common'),
			'Crabrawler': ('Alola', 'Common'),
			'Crabominable': ('Alola', 'Common'),
			'Oricorio': ('Alola', 'Common'),
			'Cutiefly': ('Alola', 'Common'),
			'Ribombee': ('Alola', 'Common'),
			'Rockruff': ('Alola', 'Common'),
			'Lycanroc': ('Alola', 'Common'),
			'Wishiwashi': ('Alola', 'Common'),
			'Mareanie': ('Alola', 'Common'),
			'Toxapex': ('Alola', 'Common'),
			'Mudbray': ('Alola', 'Common'),
			'Mudsdale': ('Alola', 'Common'),
			'Dewpider': ('Alola', 'Common'),
			'Araquanid': ('Alola', 'Common'),
			'Fomantis': ('Alola', 'Common'),
			'Lurantis': ('Alola', 'Common'),
			'Morelull': ('Alola', 'Common'),
			'Shiinotic': ('Alola', 'Common'),
			'Salandit': ('Alola', 'Common'),
			'Salazzle': ('Alola', 'Common'),
			'Stufful': ('Alola', 'Common'),
			'Bewear': ('Alola', 'Common'),
			'Bounsweet': ('Alola', 'Common'),
			'Steenee': ('Alola', 'Common'),
			'Tsareena': ('Alola', 'Common'),
			'Comfey': ('Alola', 'Common'),
			'Oranguru': ('Alola', 'Common'),
			'Passimian': ('Alola', 'Common'),
			'Wimpod': ('Alola', 'Common'),
			'Golisopod': ('Alola', 'Common'),
			'Sandygast': ('Alola', 'Common'),
			'Palossand': ('Alola', 'Common'),
			'Pyukumuku': ('Alola', 'Common'),
			'Type: Null': ('Alola', 'Legendary'),
			'Silvally': ('Alola', 'Legendary'),
			'Minior': ('Alola', 'Common'),
			'Komala': ('Alola', 'Common'),
			'Turtonator': ('Alola', 'Common'),
			'Togedemaru': ('Alola', 'Common'),
			'Mimikyu': ('Alola', 'Common'),
			'Bruxish': ('Alola', 'Common'),
			'Drampa': ('Alola', 'Common'),
			'Dhelmise': ('Alola', 'Common'),
			'Jangmo-o': ('Alola', 'Common'),
			'Hakamo-o': ('Alola', 'Common'),
			'Kommo-o': ('Alola', 'Common'),
			'Tapu Koko': ('Alola', 'Legendary'),
			'Tapu Lele': ('Alola', 'Legendary'),
			'Tapu Bulu': ('Alola', 'Legendary'),
			'Tapu Fini': ('Alola', 'Legendary'),
			'Cosmog': ('Alola', 'Legendary'),
			'Cosmoem': ('Alola', 'Legendary'),
			'Solgaleo': ('Alola', 'Legendary'),
			'Lunala': ('Alola', 'Legendary'),
			'Nihilego': ('Alola', 'Ultra Beast'),
			'Buzzwole': ('Alola', 'Ultra Beast'),
			'Pheromosa': ('Alola', 'Ultra Beast'),
			'Xurkitree': ('Alola', 'Ultra Beast'),
			'Celesteela': ('Alola', 'Ultra Beast'),
			'Kartana': ('Alola', 'Ultra Beast'),
			'Guzzlord': ('Alola', 'Ultra Beast'),
			'Necrozma': ('Alola', 'Legendary'),
			'Magearna': ('Alola', 'Mythical'),
			'Marshadow': ('Alola', 'Mythical'),
			'Poipole': ('Alola', 'Ultra Beast'),
			'Naganadel': ('Alola', 'Ultra Beast'),
			'Stakataka': ('Alola', 'Ultra Beast'),
			'Blacephalon': ('Alola', 'Ultra Beast'),
			'Zeraora': ('Alola', 'Mythical'),
			'Meltan': ('Alola', 'Mythical'),
			'Melmetal': ('Alola', 'Mythical'),

			#Galar Pokemon
			'Grookey': ('Galar', 'Common'),
			'Thwackey': ('Galar', 'Common'),
			'Rillaboom': ('Galar', 'Common'),
			'Scorbunny': ('Galar', 'Common'),
			'Raboot': ('Galar', 'Common'),
			'Cinderace': ('Galar', 'Common'),
			'Sobble': ('Galar', 'Common'),
			'Drizzile': ('Galar', 'Common'),
			'Inteleon': ('Galar', 'Common'),
			'Skwovet': ('Galar', 'Common'),
			'Greedent': ('Galar', 'Common'),
			'Rookidee': ('Galar', 'Common'),
			'Corvisquire': ('Galar', 'Common'),
			'Corviknight': ('Galar', 'Common'),
			'Blipbug': ('Galar', 'Common'),
			'Dottler': ('Galar', 'Common'),
			'Orbeetle': ('Galar', 'Common'),
			'Nickit': ('Galar', 'Common'),
			'Thievul': ('Galar', 'Common'),
			'Gossifleur': ('Galar', 'Common'),
			'Eldegoss': ('Galar', 'Common'),
			'Wooloo': ('Galar', 'Common'),
			'Dubwool': ('Galar', 'Common'),
			'Chewtle': ('Galar', 'Common'),
			'Drednaw': ('Galar', 'Common'),
			'Yamper': ('Galar', 'Common'),
			'Boltund': ('Galar', 'Common'),
			'Rolycoly': ('Galar', 'Common'),
			'Carkol': ('Galar', 'Common'),
			'Coalossal': ('Galar', 'Common'),
			'Applin': ('Galar', 'Common'),
			'Flapple': ('Galar', 'Common'),
			'Appletun': ('Galar', 'Common'),
			'Silicobra': ('Galar', 'Common'),
			'Sandaconda': ('Galar', 'Common'),
			'Cramorant': ('Galar', 'Common'),
			'Arrokuda': ('Galar', 'Common'),
			'Barraskewda': ('Galar', 'Common'),
			'Toxel': ('Galar', 'Common'),
			'Toxtricity': ('Galar', 'Common'),
			'Sizzlipede': ('Galar', 'Common'),
			'Centiskorch': ('Galar', 'Common'),
			'Clobbopus': ('Galar', 'Common'),
			'Grapploct': ('Galar', 'Common'),
			'Sinistea': ('Galar', 'Common'),
			'Polteageist': ('Galar', 'Common'),
			'Hatenna': ('Galar', 'Common'),
			'Hattrem': ('Galar', 'Common'),
			'Hatterene': ('Galar', 'Common'),
			'Impidimp': ('Galar', 'Common'),
			'Morgrem': ('Galar', 'Common'),
			'Grimmsnarl': ('Galar', 'Common'),
			'Obstagoon': ('Galar', 'Common'),
			'Perrserker': ('Galar', 'Common'),
			'Cursola': ('Galar', 'Common'),
			"Sirfetch'd": ('Galar', 'Common'),
			'Mr. Rime': ('Galar', 'Common'),
			'Runerigus': ('Galar', 'Common'),
			'Milcery': ('Galar', 'Common'),
			'Alcremie': ('Galar', 'Common'),
			'Falinks': ('Galar', 'Common'),
			'Pincurchin': ('Galar', 'Common'),
			'Snom': ('Galar', 'Common'),
			'Frosmoth': ('Galar', 'Common'),
			'Stonjourner': ('Galar', 'Common'),
			'Eiscue': ('Galar', 'Common'),
			'Indeedee': ('Galar', 'Common'),
			'Morpeko': ('Galar', 'Common'),
			'Cufant': ('Galar', 'Common'),
			'Copperajah': ('Galar', 'Common'),
			'Dracozolt': ('Galar', 'Common'),
			'Arctozolt': ('Galar', 'Common'),
			'Dracovish': ('Galar', 'Common'),
			'Arctovish': ('Galar', 'Common'),
			'Duraludon': ('Galar', 'Common'),
			'Dreepy': ('Galar', 'Common'),
			'Drakloak': ('Galar', 'Common'),
			'Dragapult': ('Galar', 'Common'),
			'Zacian': ('Galar', 'Legendary'),
			'Zamazenta': ('Galar', 'Legendary'),
			'Eternatus': ('Galar', 'Legendary'),
			'Kubfu': ('Galar', 'Legendary'),
			'Urshifu': ('Galar', 'Legendary'),
			'Zarude': ('Galar', 'Mythical'),
			'Regieleki': ('Galar', 'Legendary'),
			'Regidrago': ('Galar', 'Legendary'),
			'Glastrier': ('Galar', 'Legendary'),
			'Spectrier': ('Galar', 'Legendary'),
			'Calyrex': ('Galar', 'Legendary'),

			#Hisui Pokemon
			'Wyrdeer': ('Hisui', 'Common'),
			'Kleavor': ('Hisui', 'Common'),
			'Ursaluna': ('Hisui', 'Common'),
			'Basculegion': ('Hisui', 'Common'),
			'Sneasler': ('Hisui', 'Common'),
			'Overqwil': ('Hisui', 'Common'),
			'Enamorus': ('Hisui', 'Legendary')
		}