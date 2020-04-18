#!/bin/sh

usage() 
{
  cat << EOF
Translate between Mandarin Chinese and Singlish.
    Mandarin Chinese to Singlish: translate.sh <sentence> [-c]
    Singlish to Mandarin Chinese: translate.sh <sentence> [-s]
EOF
  exit 1
}

if [ $# -ne 2 ]; then
   usage;
fi

if [ "$2" = "-c" ] ; then
  echo "$1" | ace -g Mandarin-Chinese-Grammar/cmn.dat -Tf1 | python Mandarin-Chinese-Grammar/zh2sg.py | ace -g qsg/qsg.dat -e --disable-subsumption-test
elif [ "$2" = "-s" ] ; then
  echo "$1" | ace -g qsg/qsg.dat -Tf1 | python qsg/sg2zh.py | ace -g Mandarin-Chinese-Grammar/cmn.dat -e --disable-subsumption-test
else
  usage;
fi