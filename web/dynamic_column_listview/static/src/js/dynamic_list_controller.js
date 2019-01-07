odoo.define('dynamic_column_listview.ListController', function (require) {
"use strict";

var ListController = require('web.ListController');

function contains (list, elem) {
    return list.indexOf(elem) > -1;
};

ListController.include({

    custom_events: _.extend({}, ListController.prototype.custom_events, {
        toggleColumnSetup: '_onToggleColumnSetup',
        memoriseColumnOrder: '_memoriseColumnOrder',

    }),

    _onToggleColumnSetup: function (menu) {
        var $dropdownMenu = $("#dynamic_dropdown_menu");
        if (!menu.$.is(':visible')) {
            return;
        }
    },

    init: function (parent, model, renderer, params) {
        window.lctrl = this;
        var res = this._super.apply(this, arguments);
        if (!parent.views) {
            return res;
        }
        this.view_id = params.view_id;
        this.column_order = [];
        this.refreshColumns();
        return res;
    },

    _memoriseColumnOrder: function (event) {
        this.column_order = event.data.columns;
        this.saveColumns(this.column_order, false, true);
    },

    saveColumns: function (columns, all_users, order) {
        var self = this;
        var diff = _.difference(columns, this.column_order);
        var inter = _.intersection(this.column_order, columns);
        var col_order = _.union(inter, diff);

        var args = [
            this.view_id,
            this.modelName,
            col_order,
            false,
            true,
            col_order
        ];
        this._rpc({
            model: 'dynamic.column.listview',
            method: 'save_visible_columns',
            args: args,
        }).then(function (data) {
            self.refreshColumns();
        });
    },

    refreshColumns: function (view_id) {
        var self = this;
        this._rpc({
            model: 'dynamic.column.listview',
            method: 'get_visible_columns',
            args: [view_id || this.view_id],
        }).then(function (data) {
            var columns = data[0] || [];
            self.changeColumns(columns);
        });
    },

    changeColumns: function (columns) {

        var self = this;
        var state = this.model.get(this.handle);
        var invisible = [];
        var visible = new Array(columns.length);
        var child;

        if (!columns.length) {
            _.each(self.renderer.arch.children, function (child) {
                if (child){
                    child.attrs.modifiers.column_invisible = child.attrs.invisible;
                }
            });
            this.renderer.updateState(state, {});
            return;
        }

        while (child = self.renderer.arch.children.shift()) {
            if (child){
                var name = child.attrs.name;
                var pos = columns.indexOf(name);
                if (pos > -1) {
                    child.attrs.modifiers.column_invisible = undefined;
                    visible[pos] = child;
                }
                else {
                    child.attrs.modifiers.column_invisible = true;
                    invisible.push(child);
                }
            }
        }
        _.each(columns, function (col) {
            $('[data-id='+col+']').prop('checked', true);
        });

        self.renderer.arch.children = _.union(visible, invisible);
        this.renderer.updateState(state, {});
    }
});
});
