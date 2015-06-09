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

1. Camel case

	    $ snnm car --camel-case
		...
		CafeAuLait
		...

2. Mixed case

    	$ snnm car --mixed-case
		...
		cafeAuLait
		...

3. Underscore

    	$ snnm car --underscore
		...
		cafe_au_lait
		...

4. Constant

		$ snnm car --constant
		...
		CAFE_AU_LAIT
		...



And that's it. That's all it does... =P

###Where does the data come from?

All data comes from http://www.thesaurus.com/


###Documentation

TODO
