#!/usr/bin/python
# -*- coding: utf-8 -*-

from doctest import SKIP
import sys

argument = str(sys.argv[1])

def calculate(japtext):
  text = japtext
  uniqs = []
  skip = "\n A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z ぁ あ ぃ い ぅ う ぇ え ぉ お か が き ぎ く ぐ け げ こ ご さ ざ し じ す ず せ ぜ そ ぞ た だ ち ぢ っ つ づ て で と ど な に ぬ ね の は ば ぱ ひ び ぴ ふ ぶ ぷ へ べ ぺ ほ ぼ ぽ ま み む め も ゃ や ゅ ゆ ょ よ ら り る れ ろ ゎ わ ゐ ゑ を ん ゔ ゕ ゖ ァ ア ィ イ ゥ ウ ェ エ ォ オ カ ガ キ ギ ク グ ケ ゲ コ ゴ サ ザ シ ジ ス ズ セ ゼ ソ ゾ タ ダ チ ヂ ッ ツ ヅ テ デ ト ド ナ ニ ヌ ネ ノ ハ バ パ ヒ ビ ピ フ ブ プ ヘ ベ ペ ホ ボ ポ マ ミ ム メ モ ャ ヤ ュ ユ ョ ヨ ラ リ ル レ ロ ヮ ワ ヰ ヱ ヲ ン ヴ ヵ ヶ ヷ ヸ ヹ ヺ ・ ー ヽ ヾ 「 」、。1 2 3 4 5 6 7 8 9 0 "
  fn5 = open("JLTPn5.txt", encoding="utf8")
  fn4 = open("JLTPn4.txt", encoding="utf8")
  fn3 = open("JLTPn3.txt", encoding="utf8")
  fn2 = open("JLTPn2.txt", encoding="utf8")
  fn1 = open("JLTPn1.txt", encoding="utf8")

  n5 = fn5.read()
  n4 = fn4.read()
  n3 = fn3.read()
  n2 = fn2.read()
  n1 = fn1.read()

  def printAll():
    print(n5)
    print(n4)
    print(n3)
    print(n2)
    print(n1)

  for c in text:
    if c in uniqs or c in skip:
      continue
    else:
      uniqs.append(c)

  #print(uniqs)
  show = ""
  for i in uniqs:
    show += i
  print(show)
  print()

  n5counter = 0
  for letter in uniqs:
    if letter in n5:
      n5counter +=1
  print("JLPT N5")
  print(str(n5counter) + " out of " + str(len(uniqs)))
  print(str("{:.2%}".format(n5counter / len(uniqs))))
  print("\n")

  n4counter = 0
  for letter in uniqs:
    if letter in n4 or letter in n5:
      n4counter +=1
  print("JLPT N4")
  print(str(n4counter) + " out of " + str(len(uniqs)))
  print(str("{:.2%}".format(n4counter / len(uniqs))))
  print("\n")

  n3counter = 0
  for letter in uniqs:
    if letter in n3 or letter in n4 or letter in n5:
      n3counter +=1
  print("JLPT N3")
  print(str(n3counter) + " out of " + str(len(uniqs)))
  print(str("{:.2%}".format(n3counter / len(uniqs))))
  print("\n")

  n2counter = 0
  for letter in uniqs:
    if letter in n2 or letter in n3 or letter in letter in n4 or letter in n5:
      n2counter +=1
  print("JLPT N2")
  print(str(n2counter) + " out of " + str(len(uniqs)))
  print(str("{:.2%}".format(n2counter / len(uniqs))))
  print("\n")

  n1counter = 0
  for letter in uniqs:
    if letter in n1 or letter in n2 or letter in n3 or letter in letter in n4 or letter in n5:
      n1counter +=1
  print("JLPT N1")
  print(str(n1counter) + " out of " + str(len(uniqs)))
  print(str("{:.2%}".format(n1counter / len(uniqs))))
  print("\n")

  return


def clean(japanesetext):
    skip = "\n A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z ぁ あ ぃ い ぅ う ぇ え ぉ お か が き ぎ く ぐ け げ こ ご さ ざ し じ す ず せ ぜ そ ぞ た だ ち ぢ っ つ づ て で と ど な に ぬ ね の は ば ぱ ひ び ぴ ふ ぶ ぷ へ べ ぺ ほ ぼ ぽ ま み む め も ゃ や ゅ ゆ ょ よ ら り る れ ろ ゎ わ ゐ ゑ を ん ゔ ゕ ゖ ァ ア ィ イ ゥ ウ ェ エ ォ オ カ ガ キ ギ ク グ ケ ゲ コ ゴ サ ザ シ ジ ス ズ セ ゼ ソ ゾ タ ダ チ ヂ ッ ツ ヅ テ デ ト ド ナ ニ ヌ ネ ノ ハ バ パ ヒ ビ ピ フ ブ プ ヘ ベ ペ ホ ボ ポ マ ミ ム メ モ ャ ヤ ュ ユ ョ ヨ ラ リ ル レ ロ ヮ ワ ヰ ヱ ヲ ン ヴ ヵ ヶ ヷ ヸ ヹ ヺ ・ ー ヽ ヾ 「 」、。1 2 3 4 5 6 7 8 9 0 （ ） 　 ％ ？ ― １ 　 ２ ３ ４ ５ ６ ７ ８ ９ ０ ！ ※ …"


    source = open(argument, "r", encoding="utf8")
    dest = open("cleaned_" + argument, "w", encoding="utf8")

    # replace characters and write into dest file
    stripped = ""

    for line in source:
        takeline = line
        for character in skip:
            if character in takeline:
                takeline = takeline.replace(character, "")          
        stripped += takeline

    dest.write(stripped.replace(" ", ""))
    return stripped.replace(" ", "")


text = clean(argument)
print()
calculate(text)