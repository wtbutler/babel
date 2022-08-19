# TODO

## 8-18-22 morning
* Determine useful properties of hex tiles
    * Neighbors
    * Sprite coordinate
    * Have a Valid Neighbors function
        * Work out if it needs some requirement filled
            * at least one stairway connection for hallways
            * at least one hallway connection for bookshelf rooms
        * Otherwise match openings of the same type
            * Can't put a circle room over a stairway or a blank
    * Unsure if I want "generic" types of rooms, or specific instances yet
        * generic types that are given to hex spaces?
        * i.e. each tile type is a static class, and there's a class for hex spaces?
        * That sounds like it makes the most sense and fits best with WFC
        * Add tags to tile types so that making connection rules is easier?
            * "open top"
            * "opening north"
            * "opening south east"
            * "stairs up"
            * "stairs down"
    * Figure out how to make the infinite shafts. Just pick a few coordinates to function as infinite shafts?
    * How do I want the grid to work?
        * I can't store it in a 3d array, that's just infeasible
        * Just keep track of neighbors and use some BFS algorithm to see nearby rooms?
        * Use a 'chunk' system?
            * Chunks with vertical slices as well?
            * Just slices, not vertical chunks?
            * triangular or rhomboid?
                * rhomboid tiles cleanly, but triangular loads less
