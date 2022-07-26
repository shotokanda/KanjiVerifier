# KanjiVerifier
This script verifies how many kanji of a text you will understand according to your JLPT level. 

## Motivation

TokuyuuTV explained in a video (https://www.youtube.com/watch?v=4CvoPRZsejc&list=LL&index=3&t=235s) that you will understand the following percentages of kanji from e.g. a newspaper article according to your JLPT level:


| level | number of characters |  known/unknown ratio  |
| ----- | -------------------- | ------------- |
| N5    |  ~80 chars           | 36%           |
| N4    |  ~246 chars          | 62%           |
| N3    |  ~616 chars          | 86%           |
| N2    |  ~986 chars          | 94%           |
| N1    |  ~2226 chars         | 100%*         | 

\* except for special kanji, normally explained with furigana 

You can use this script with text files where you saved the text from e.g. a news article into and verify this statistics on your own.


## Usage

[^1]: Insert your e.g. article's text into a file. (test.txt includes an example)
[^2]: Run the script by executing:
```
python3 kanjiverifier.py <NAME OF YOUR FILE>.txt
```
