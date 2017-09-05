# `snnm`

> There are only two hard things in Computer Science: cache invalidation and naming things.
>
> -- Phil Karlton


The first problem is for smart people only. The second one can be eased with the
aid of `snnm` (SYNONYMS)


## How it works

```
$ snnm coffee
Synonyms for coffee:
battery acid
brew
caffeine
café
café au lait
café noir
cappuccino
decaf
decoction
demitasse
espresso
forty weight
hot stuff
ink
jamocha
java
joe
mocha
mud
perk
varnish remover

```

Furthermore, it will try to paginate your results according to your terminal
height.

There's also a `-u | --ugly-output` flag that can be used in case you want to
pipe your output into some other program.


## Where does the data come from?

All data comes from http://www.thesaurus.com/


## Installation

```
$ pip install snnm

```

**Note:** This is a Python 3 only package.
