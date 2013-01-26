dojo.provide("hb.Cell");
dojo.require("dijit._Widget");
dojo.declare("hb.Cell", dijit._Widget, {
    starting_health: 50,
    constructor: function(health){
        if(health == undefined){
            this._health = this.starting_health;
        } else {
            this._health = health;
        }
        this._direction = null;
    },
    get_health: function(){
        return this._health;
    },
    get_location: function(){
        return {x:this._x, y:this._y};
    },
    fight: function(cell){
        if(cell.get_health() > this._health){
            cell.lose_health(this._health);
            this.die();
        } else if (cell.get_health() < this._health){
            this.lose_health(cell._health);
            cell.die();
        } else {
            cell.die();
            this.die();
        }
    },
    load: function(cell_data){
        this._direction = cell_data.d;
        this._x = cell_data.x;
        this._y = cell_data.y;
        this._h = cell_data.h;
    },
    lose_health: function(health){
        this._health -= health;
    },
    serialize: function(){
        return {
            d: this._direction,
            x: this._x,
            y: this._y,
            h: this._health
        };
    },
    set_direction: function(direction){
        this._direction = direction;
    },
    set_location: function(x, y){
        this._x = x;
        this._y = y;
    }
});
