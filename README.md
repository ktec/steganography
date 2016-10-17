# Southampton CodeDojo October 2016

Tonight for codedojo the challenge was to create something related to steganography. Not stenography, btw, thats something entirely different.

Stegnography is the art of hiding something in plain sight. We chose to hide an image containing a message within another message.

"A Brazilian drug trafficker had messages hidden with steganographic algorithms hidden on his computer inside images of a cartoon character" [1]

We chose to implement using python because neither of us knew it well so it was a good chance to learn two things at once!

There are two main scripts, `encode.py` and `decode.py`. It should be blindingly obvious what they do.


So to get started, lets open our host or carrier image.

```
$ open ./image.png
```


## Encode

Ok, now let's encode our "secret" image:

```
$ ./encode.py image.png ./secret/secret.png encoded.png
Encoded file encoded.png written
```

Now you can open `encoded.png` and inspect it closely. Can you see any difference?
No, exactly!! But hidden in there is our secret...

```
$ open ./encoded.png
```

![Encoded](./encoded.png?raw=true "Can you see a hidden message?")


## Decode

Ok let's put you out of your misery and decode it:

```
$ ./decode.py encoded.png secret.png
Decoded file secret.png written
```

And finally let's open the file to reveal the secret image:

```
$ open ./secret.png
```


Credits: I must thank [David Banks](https://github.com/davidbanks17), for most of the heavy lifting here, I just pointed and asked questions mostly.


Further reading: 

[1] Aaron Miller - http://www.aaronmiller.in/thesis/
