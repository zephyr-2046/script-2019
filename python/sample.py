import doctest
import json
import pprint

    
def util_group_nonzero_number( input_data, zero_threshold, two_parts_threshold ):

    """group vertical non-zero number into sub groups.

    >>> pprint.pprint( util_group_nonzero_number( [20, 30, 70], 2, 4 ) )
    [{'base': 0, 'count': 3}]
    
    >>> pprint.pprint( util_group_nonzero_number( \
    [   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, \
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, \
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, \
        0,  2,  5,  6,  2,  2,  4,  5,  2,  4,  5,  5,  4,  2,  3,  4,  5, \
        2,  4,  6,  5,  3,  5,  3,  6,  2,  0,  0,  0,  0,  0,  0,  2,  1, \
        7,  2,  2,  4,  5,  2,  4,  5,  5,  4,  2,  5,  6,  5,  6,  5,  4, \
        0,  0,  0,  0,  0,  1,  2,  4, 10,  4,  4,  5,  3,  3,  5,  2,  3, \
        5,  2,  2,  6,  3,  2,  4,  5,  7,  2,  3,  7,  2,  2,  5,  3,  3, \
        5,  2,  3,  4,  3,  9,  3,  0,  0,  0,  0,  0,  0,  5,  4,  1,  2, \
        6,  4,  5,  4,  2,  4,  5,  4,  2,  8,  7,  4,  2,  5,  3,  3,  5, \
        2,  2,  4,  1,  6,  6,  4,  6,  2,  0,  0,  0,  0,  0,  0,  1,  1, \
        7,  2,  2,  5,  3,  3,  5,  2,  3,  4,  5,  2,  2,  6,  6,  4,  6, \
        6,  4,  5,  4,  2,  3,  7,  4,  3,  2,  2,  0,  0,  0,  0,  0,  1, \
        2,  4, 10,  4,  4,  5,  3,  3,  5,  2,  3,  5,  2,  2,  6,  3,  2, \
        4,  5,  7,  2,  3,  7,  2,  2,  5,  3,  3,  5,  2,  5,  7,  7,  2, \
        2,  2,  5,  4,  4,  7,  2,  2,  5,  3,  3,  5,  2,  5,  3,  3,  5, \
        2,  3,  2,  5,  7,  5,  7,  4,  0,  0,  0,  0,  0,  0,  2,  4,  2, \
        3,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2,  4,  4,  6, \
        3,  3,  2,  0,  0,  2,  2,  6,  3,  2,  6,  5,  2,  5,  3,  3,  5, \
        2,  2,  4,  3,  4,  5,  2,  2,  4,  1,  6,  5,  5,  6,  2,  0,  0, \
        2,  4,  4,  6,  4,  4,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, \
        0,  0,  0,  0,  0,  0,  4,  5,  1,  1,  3,  4,  5,  2,  2,  4,  3, \
        4,  5,  2,  7,  6,  5,  6,  4,  4,  0,  0,  0,  0,  0,  2,  2,  6, \
        3,  2,  6,  5,  2,  4,  5,  2,  4,  5,  5,  4,  2,  3,  4,  5,  2, \
        3,  5,  5,  2,  4,  5,  2,  4,  5,  2,  2,  5,  2,  2,  5,  6,  5, \
        6,  5,  4,  0,  0,  0,  0,  0,  2,  4,  6,  4,  2,  4,  5,  2,  6, \
        6,  4,  6,  6,  4,  5,  4,  2,  4,  5,  5,  3,  6,  2,  4,  5,  2, \
        3,  4,  3,  9,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 2, 4 ) ) 
    [{'base': 52, 'count': 25},
     {'base': 83, 'count': 19},
     {'base': 107, 'count': 36},
     {'base': 149, 'count': 30},
     {'base': 185, 'count': 30},
     {'base': 220, 'count': 60},
     {'base': 286, 'count': 5},
     {'base': 302, 'count': 45},
     {'base': 363, 'count': 20},
     {'base': 388, 'count': 40},
     {'base': 433, 'count': 31}]
    """

    nonzero_width_group = []
    connected_group_queue = []

    # type check
    if( isinstance( input_data, list ) or isinstance( input_data, tuple ) ):

        # initialize count
        last_item_base  = -1
        last_item_count = 0

        for index in range( 0, len(input_data) ):

            # the zero_threshold is the threshold for one horizontal line counting
            if( input_data[index] >= zero_threshold ):

                if( last_item_base > -1 ):
                    last_item_count += 1

                else:
                    last_item_base  = index
                    last_item_count = 1

            # case 2: zero 
            elif input_data[index] == 0:

                if( last_item_base > -1 ):

                    # push the previous one
                    nonzero_width_group.append( { 'base':last_item_base, 'count':last_item_count } )

                # record the new one
                last_item_base = -1
                last_item_count = 0

            # case 3: 0 < input_data[index] < zero_threshold    
            else:

                if last_item_base > -1 :

                    if index + 1 < len(input_data):

                        # not tjson.dumps(mydict, indent=4, sort_keys=True)erminate the string if the next is not zero
                        if input_data[index + 1] > 0 :

                            last_item_count += 1

                        else:
                        
                            # the next one is zero, treate as a terminate

                            # the last one, treat as a terminate
                            last_item_count += 1

                            # append the existing one
                            nonzero_width_group.append( { 'base':last_item_base, 'count':last_item_count } )

                            # record the new one
                            last_item_base = -1
                            last_item_count = 0
                            json.dumps(mydict, indent=4, sort_keys=True)
                    else:
                        # the last one, treat as a terminate
                        last_item_count += 1

                        # append the existing one
                        nonzero_width_group.append( { 'base':last_item_base, 'count':last_item_count } )

                        # record the new one
                        last_item_base = -1
                        last_item_count = 0
                
                else:

                    # check whether start a new one 
                    # whether in a square box
                    item_is_not_alone = True
                    for peek_offset in range( 1, zero_threshold ):
                        if ( index + peek_offset < len(input_data) ) and ( input_data[index] == 0 ) :
                            item_is_not_alone = False
                            break

                    if item_is_not_alone :

                        last_item_base  = index
                        last_item_count = 1

                    else:

                        # record the new one
                        last_item_base = -1
                        last_item_count = 0

        # push the last one
        if( last_item_base > -1 ):
            nonzero_width_group.append( { 'base':last_item_base, 'count':last_item_count } )

        #print( "nonzero_width_group = ",  nonzero_width_group )

        # initialize count
        last_item_base  = nonzero_width_group[0]['base']
        last_item_count = nonzero_width_group[0]['count']

        for index in range( 1,  len(nonzero_width_group) ):

            # check the interval
            a = last_item_base + last_item_count + two_parts_threshold
            b = nonzero_width_group[index]['base']

            if( last_item_base + last_item_count + two_parts_threshold > nonzero_width_group[index]['base'] ):

                # very close, update condition
                last_item_base = last_item_base
                last_item_count = nonzero_width_group[index]['base'] - last_item_base + nonzero_width_group[index]['count']

            else:
                # push the previous one
                connected_group_queue.append( { 'base':last_item_base, 'count':last_item_count } )

                # reset condition
                last_item_base  = nonzero_width_group[index]['base']
                last_item_count = nonzero_width_group[index]['count']

        # push the last one
        connected_group_queue.append( { 'base':last_item_base, 'count':last_item_count } )

        #print("")
        #print( "connected_group_queue = ",  connected_group_queue )

    return connected_group_queue

input = [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  2,  5,  6,  2,  2,  4,  5,  2,  4,  5,  5,  4,  2,  3,  4,  5,
        2,  4,  6,  5,  3,  5,  3,  6,  2,  0,  0,  0,  0,  0,  0,  2,  1,
        7,  2,  2,  4,  5,  2,  4,  5,  5,  4,  2,  5,  6,  5,  6,  5,  4,
        0,  0,  0,  0,  0,  1,  2,  4, 10,  4,  4,  5,  3,  3,  5,  2,  3,
        5,  2,  2,  6,  3,  2,  4,  5,  7,  2,  3,  7,  2,  2,  5,  3,  3,
        5,  2,  3,  4,  3,  9,  3,  0,  0,  0,  0,  0,  0,  5,  4,  1,  2,
        6,  4,  5,  4,  2,  4,  5,  4,  2,  8,  7,  4,  2,  5,  3,  3,  5,
        2,  2,  4,  1,  6,  6,  4,  6,  2,  0,  0,  0,  0,  0,  0,  1,  1,
        7,  2,  2,  5,  3,  3,  5,  2,  3,  4,  5,  2,  2,  6,  6,  4,  6,
        6,  4,  5,  4,  2,  3,  7,  4,  3,  2,  2,  0,  0,  0,  0,  0,  1,
        2,  4, 10,  4,  4,  5,  3,  3,  5,  2,  3,  5,  2,  2,  6,  3,  2,
        4,  5,  7,  2,  3,  7,  2,  2,  5,  3,  3,  5,  2,  5,  7,  7,  2,
        2,  2,  5,  4,  4,  7,  2,  2,  5,  3,  3,  5,  2,  5,  3,  3,  5,
        2,  3,  2,  5,  7,  5,  7,  4,  0,  0,  0,  0,  0,  0,  2,  4,  2,
        3,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2,  4,  4,  6,
        3,  3,  2,  0,  0,  2,  2,  6,  3,  2,  6,  5,  2,  5,  3,  3,  5,
        2,  2,  4,  3,  4,  5,  2,  2,  4,  1,  6,  5,  5,  6,  2,  0,  0,
        2,  4,  4,  6,  4,  4,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  4,  5,  1,  1,  3,  4,  5,  2,  2,  4,  3,
        4,  5,  2,  7,  6,  5,  6,  4,  4,  0,  0,  0,  0,  0,  2,  2,  6,
        3,  2,  6,  5,  2,  4,  5,  2,  4,  5,  5,  4,  2,  3,  4,  5,  2,
        3,  5,  5,  2,  4,  5,  2,  4,  5,  2,  2,  5,  2,  2,  5,  6,  5,
        6,  5,  4,  0,  0,  0,  0,  0,  2,  4,  6,  4,  2,  4,  5,  2,  6,
        6,  4,  6,  6,  4,  5,  4,  2,  4,  5,  5,  3,  6,  2,  4,  5,  2,
        3,  4,  3,  9,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]

print(" ")

#result = util_group_nonzero_number( [20, 30, 70], 2, 4 )

#result = util_group_nonzero_number( input, 2, 4 )

#result = util_group_nonzero_nujson.dumps(mydict, indent=4, sort_keys=True)mber( [20, 30, 70], 2, 4 )

#print(" ")

result = util_group_nonzero_number_old( input, 2, 4 )

doctest.testmod()

#print( json.dumps(result, indent=4, sort_keys=True) )

#pprint.pprint( result )
