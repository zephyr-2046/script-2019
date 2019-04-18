[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
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
        
def util_group_nonzero_number( input_data, zero_threshold, two_parts_threshold ):

    nonzero_width_group = []
    connected_group_queue = []

    # type check
    if( isinstance( input_data, list ) or isinstance( input_data, tuple ) ):
    
        # initialize count
        last_item_base  = -1
        last_item_count = 0

        for index in range( 0, len(input_data) ):

            #
            if( input_data[index] >= zero_threshold ):

                if( last_item_base > -1 ):
                    last_item_count += 1
                    
                else:
                    last_item_base  = index
                    last_item_count = 1
            else:

                if( last_item_base > -1 ):

                    # push the previous one
                    nonzero_width_group.append( { 'base':last_item_base, 'count':last_item_count } )

                # record the new one
                last_item_base = -1
                last_item_count = 0

        # push the last one
        if( last_item_base > -1 ):
            nonzero_width_group.append( { 'base':last_item_base, 'count':last_item_count } )

        #console.log( "nonzero_width_group = ",  JSON.stringify(nonzero_width_group) );

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
                connected_group_queue.push( { 'base':last_item_base, 'count':last_item_count } )

                # reset condition
                last_item_base  = nonzero_width_group[index]['base']
                last_item_count = nonzero_width_group[index]['count']

        # push the last one
        connected_group_queue.append( { 'base':last_item_base, 'count':last_item_count } )

        #console.log( "connected_group_queue = ",  JSON.stringify(connected_group_queue) )

    return connected_group_queue

print( util_group_nonzero_number(input, 2, 4) )
