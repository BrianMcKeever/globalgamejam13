dojo.provide("hb.Board");
dojo.require("hb.Cell");
dojo.require("dijit._Widget");
dojo.declare("hb.Board", dijit._Widget, {
    _size: 15,
    add_cell: function(cell, x, y){
        if(this._grid[x][y] !== null) throw "Spot Taken";
        this._grid[x][y] = cell;
        cell.set_location(x, y);
    },
    constructor: function(){
        this._grid = [];
        for(var i = 0; i < this._size; i++){
            var a = [];
            this._grid.push(a);
            for(var j = 0; j < this._size; j++){
                a.push(null);
            }
        }
    },
    load: function(board_data){
        this._grid = board_data;
        for(var x = 0; x < this._size; x++){
            for(var y = 0; y < this._size; y++){
                if(this._grid[x][y] !== null){
                    var data = this._grid[x][y];
                    this._grid[x][y] = hb.Cell();
                    this._grid[x][y].load(data);
                }
            }
        }
    },
    move_cell: function(cell, x, y){
        //TODO: animation/whatever
        this.remove_cell(cell);
        this.add_cell(cell, x, y);
    },
    remove_cell: function(cell){
        var loc = cell.get_location();
        if(this._grid[loc.x][loc.y] !== cell) throw "cell not there";
        this._grid[loc.x][loc.y] = null;
    },
    serialize: function(){
        var serialized = [];
        for(var x = 0; x < this._size; x++){
            var a = [];
            serialized.push(a);
            for(var y = 0; y < this._size; y++){
                if(this._grid[x][y] === null){
                    a.push(null);
                } else {
                    a.push(this._grid[x][y].serialize());
                }
            }
        }
        return serialized;
    }
});
