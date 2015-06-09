snnm
====

> There are only two hard things in Computer Science: cache invalidation and naming things.
>
> -- Phil Karlton


The first problem is for smart people only. The second one can be eased with the aid of snnm (SYNONYMS)


###How it works

The basics:

    $ snnm coffee
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

	    $ snnm coffee --camel-case
		...
		CafeAuLait
		...

2. Mixed case

    	$ snnm coffee --mixed-case
		...
		cafeAuLait
		...

3. Underscore

    	$ snnm coffee --underscore
		...
		cafe_au_lait
		...

4. Constant

		$ snnm coffee --constant
		...
		CAFE_AU_LAIT
		...



And that's it. That's all it does... =P

###Where does the data come from?

All data comes from http://www.thesaurus.com/


###Installation

	pip install snnm


**This package only works with Python 3.x**
