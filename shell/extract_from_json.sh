function parse_json()
{
    echo $1 | \
    sed -e 's/[{}]/''/g' | \
    sed -e 's/", "/'\",\"'/g' | \
    sed -e 's/" ,"/'\",\"'/g' | \
    sed -e 's/" , "/'\",\"'/g' | \
    sed -e 's/","/'\"---SEPERATOR---\"'/g' | \
    awk -F=':' -v RS='---SEPERATOR---' "\$1~/\"$2\"/ {print}" | \
    sed -e "s/\"$2\"://" | \
    tr -d "\n\t" | \
    sed -e 's/\\"/"/g' | \
    sed -e 's/\\\\/\\/g' | \
    sed -e 's/^[ \t]*//g' | \
    sed -e 's/^"//'  -e 's/"$//'
}


#parse_json '{"username":"john, doe","email":"john@doe.com"}' username
#parse_json '{"username":"john doe","email":"john@doe.com"}' email

#--- outputs ---

#john, doe
#johh@doe.com


#Illustration, keyword is username

# remove '{' and '}' character
#    sed -e 's/[{}]/''/g' | \
#    
# output : "username":"john, doe","email":"john@doe.com"
#
# remove space around ','    
#    sed -e 's/", "/'\",\"'/g' | \
#    sed -e 's/" ,"/'\",\"'/g' | \
#    sed -e 's/" , "/'\",\"'/g' | \
#
# output : "username":"john, doe","email":"john@doe.com"
#
# convert ',' to "---SEPERATOR---"
#    sed -e 's/","/'\"---SEPERATOR---\"'/g' | \
#
# output : "username":"john, doe"---SEPERATOR---"email":"john@doe.com"
#
# select the row including the keyword
#    awk -F=':' -v RS='---SEPERATOR---' "\$1 ~ /\"$2\"/ {print}" | \
#    -F=':' means the source is stdin
#    RS='---SEPERATOR---' means row separator
#    "\$1 ~ /\"$2\"/ {print}" means a filter and an action, 
#                \$1 means an escape, ~ is a regex match, /\"$2\"/ will be replaced with the keyword. {print} is an action
#
# output : "username":"john, doe"
#
# remove the keyword from a row
#    sed -e "s/\"$2\"://" | \
#
# output : "john, doe" ( without newline )
#
# remove the surrounding "
#    sed -e 's/\\"/"/g' | \
#    sed -e 's/\\\\/\\/g' | \
#    sed -e 's/^[ \t]*//g' | \
#    sed -e 's/^"//'  -e 's/"$//'
#
# output : jone, doe
#

