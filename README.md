# OliCyberUCT

**OliCyber User Comparison Tool** is a command line utility for `training.olicyber.it` users.

It allows you to compare two users and see which challenges they have solved that the other has not.

Other features may be added in the future.

## Installation

```bash
git clone https://github.com/FLAK-ZOSO/OliCyberUCT
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
