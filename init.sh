#!/bin/sh
for i in `seq 162`
do
  zero_padding=`printf %03d $i`
  mkdir ./recents/ABC_${zero_padding} && touch ./recents/ABC_${zero_padding}/{A,B,C,D,E,F}.py
done
