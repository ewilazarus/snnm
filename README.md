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

... and some variations:

1. CamelCase


    $ snnm car -c
	...
	CafeAuLait
	...


2. mixedCase:


    $ snnm car -m
	...
	cafeAuLait
	...

3. underscore:


    $ snnm car -u
	...
	cafe_au_lait
	...


4. CONSTANT:


	$ snnm car -o
	...
	CAFE_AU_LAIT
	...



And that's it. That's all it does... =)

###Where does the data come from?

All data comes from http://www.thesaurus.com/


###Documentation

TODO
