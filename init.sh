#!/bin/sh
for i in `seq 164`
do
  zero_padding=`printf %03d $i`
  mkdir ./recents/ABC_${zero_padding}
  if [ $i -gt 126 ]; then
    touch ./recents/ABC_${zero_padding}/{A,B,C,D,E,F}.py
  else
    touch ./recents/ABC_${zero_padding}/{A,B,C,D}.py
  fi
done
