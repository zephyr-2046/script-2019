#!/bin/sh

# Copyright (C) 2019 zephyr-2046
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

usage() { echo "Usage: $0 [-s <45|90>] [-p <string>]" 1>&2; exit 1; }

input="49015420323751"

echo "The input string is $input,"

_input_len=`expr length $input`

echo ${_input_len}
sum=0

# add up the special digits
for (( i=${_input_len}-1; i >= 0; i-=2 )); do

#    echo "loop${i} ${input:${i}:1}"
#    echo "double should be " $(expr ${input:${i}:1} + ${input:${i}:1})

    double=$(expr ${input:${i}:1} + ${input:${i}:1} )

    if [ $double -ge 10 ]
    then
        sum=$(( double + sum - 9 ))
    else
        sum=$(( double + sum ))
    fi

#    echo "sub sum is ${sum}"

done

# add up the normal digits
for (( i=${_input_len}-2; i >= 0; i-=2 )); do

#    echo "loop${i} ${input:${i}:1}"
#    echo "single should be " $(expr ${input:${i}:1} + 0)

    single=$(expr ${input:${i}:1} + 0 )

    sum=$(( single + sum ))

#    echo "sub sum is ${sum}"

done

# get the check result
while [ $sum -gt 10 ]
do
    sum=$(( sum - 10 ))

    echo "minus 10"
done
sum=$(( 10 - sum ))


# show the result
echo "sum is ${sum}"
