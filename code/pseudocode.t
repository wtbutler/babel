add hex to tile
    set shape of tile to hex
        set options to empty
    update barriers of tile to hex barriers
        also check hex's requirements (such as minimum stairs or minimum walls)
    remove tile from frontier
    add tile to update queue
    


process item from update queue
    pull item out of update queue
    backtrack initiating neighbor
    get valid options that can be next to that neighbor
    intersection that with item's options
    update new barriers of item
        also check each possible hex's requirements (such as minimum stairs or minimum walls)
    if option list or barrier list has changed, add neighbors


update barriers
    if option space hasn't collapsed, just get collation of all option's barrier options

    get current collapsed barriers
        i.e. for each neighbor, get the barriers *that neighbor* has towards this tile
    initiate progress as empty

    if shape is defined
        get that shape's barrier options
        intersect that with current collapsed barriers
        feed that into the shape's requirements
        for each direction
            union that with progress
    otherwise
        for option
            get that option's barrier options
            intersect that with current collapsed barriers
            feed that into that option's requirements
            for each direction
                union that with progress
