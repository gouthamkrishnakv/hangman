#!/usr/bin/python3

#   This program is authored by Goutham Krishna K V (gauthamkrishna9991@live.com).

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import linecache, random
arr = [False]*26

def showSentence(sentence):
    s = ""
    for i in range(len(sentence)):
        if sentence[i] == " ":
            s += " "
        elif sentence[i] == "\n":
            break
        elif(arr[ord(sentence.upper()[i]) - 65]):
            s += sentence[i]
        else:
            s += "-"
    return s

def toggleVals(ch):
    arr[ord(ch.upper()[0]) - 65] = True

def isin(sentence, ch):
    for i in range(len(sentence)):
        if ch.upper() == sentence.upper()[i]:
            return True
    return False

def isFilled(sentence):
    sen = sentence.upper()
    for i in range(len(sen)):
        if ord(sen[i]) >= ord('A') and ord(sen[i]) <= ord('Z'):
            if arr[ord(sen[i]) - 65] == False:
                return False
    return True


def isValuePresent(sentence, ch):
    if isin(sentence, ch):
        if not arr[ord(ch.upper()[0]) - 65]:
            arr[ord(ch.upper()[0]) - 65] = True
        return True
    else:
        return False

def showValues():
    vals = ""
    for i in range(26):
        if not (arr[i]):
            vals += chr(65 + i) + " "
        else:
            vals += "# "
    return vals

x = linecache.getline("examples.txt",random.randint(1,sum(1 for line in open('examples.txt'))))
n = 10
while(n > 0):
    print(showSentence(x))
    print(showValues())
    ch = input("Enter a character : ")
    if not isValuePresent(x,ch):
        n -= 1
    if isFilled(x):
        print("Congrats! You win!")
        print("The word is " + x[:-1])
        exit()
    print("You've got " + str(n) + " times remaining.")
print("HANGMAN!")
print("The word was " + x[:-1])
print("Sorry, You lose :(")
