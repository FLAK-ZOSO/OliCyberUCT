# OliCyberUCT

**OliCyber User Comparison Tool** is a command line utility for `training.olicyber.it` users.

It allows you to compare two users and see which challenges they have solved that the other has not.

Other features may be added in the future.

## Installation

```bash
git clone https://github.com/FLAK-ZOSO/OliCyberUCT
```

Consider putting your user token in `token.txt` if you receive the following error.

```py
Traceback (most recent call last):
  File "/home/flak-zoso/Documents/GitHub/OliCyberUCT/playerdiff.py", line 12, in <module>
    user1.get_stats()
  File "/home/flak-zoso/Documents/GitHub/OliCyberUCT/olicybertools.py", line 13, in get_stats
    if self.stats["extended"]:
TypeError: 'NoneType' object is not subscriptable
```

You can find your user token by logging in to `training.olicyber.it` and looking at the localStorage in your browser's developer tools.

```js
console.log(localStorage.getItem("token"));
```

## Usage

```md
python3 playerdiff.py <user1> <user2> [--title|--id|--both] [--stats]
```

### Example command

```bash
python3 playerdiff.py 4244 6606 --both --stats
```

### Example output

```bash
815wena with 0 correct submissions has 0 points
mmm03 with 9 correct submissions has 1767 points

mmm03 has solved 9 challenges that 815wena has not solved

- (250, 'Misc 03 - Allegati')
- (252, 'Misc 05 - Servizio tcp')
- (251, 'Misc 04 - Sito web')
- (248, 'Misc 01 - Sanity Check')
- (80, 'Very strong Vigenere')
- (249, 'Misc 02 - Suggerimenti')
- (253, 'Misc 06 - Espressione regolare')
- (77, 'I like hashes')
- (73, 'Tutte le strade portano a Roma')

815wena has solved 0 challenges that mmm03 has not solved
```
