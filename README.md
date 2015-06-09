snnm
====

> There are only two hard things in Computer Science: cache invalidation and naming things.
>
> -- Phil Karlton


The first problem is only for smart people. The second one can be eased with the aid of snnm (SYNONYMS)


###How it works

The basics:

    $ snnm car
	perk
	mud
	brew
	café
	cappuccino
	espresso
	caffeine
	java
	decaf
	decoction
	mocha
	demitasse
	ink
	battery acid
	café au lait
	café noir
	forty weight
	hot stuff
	jamocha
	joe
	varnish remover

Some variations:

1. CamelCase

    $ snnm car --camel-case
	(...)
	Ink
	BatteryAcid
	CafeAuLait
	CafeNoir
	FortyWeight

2. mixedCase

    $ snnm car --mixed-case
	(...)
	ink
	batteryAcid
	cafeAuLait
	cafeNoir
	fortyWeight

3. underscore

    $ snnm car --underscore
	(...)
	ink
	battery_acid
	cafe_au_lait
	cafe_noir
	forty_weight

4. CONSTANT

	$ snnm car --constant
	(...)
	INK
	BATTERY_ACID
	CAFE_AU_LAIT
	CAFE_NOIR
	FORTY_WEIGHT


And that's it. That's all it does... =)

###Where does the data come from?

All data comes from http://www.thesaurus.com/


###Documentation

TODO
