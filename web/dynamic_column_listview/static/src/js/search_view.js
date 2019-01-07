odoo.define('dynamic_column_listview.SearchView', function (require) {
"use strict";

var rpc = require('web.rpc')
var core = require('web.core');
var SearchView = require('web.SearchView');
var FavoriteMenu = require('web.FavoriteMenu');
var FilterMenu = require('web.FilterMenu');
var GroupByMenu = require('web.GroupByMenu');
var DynamicColumnMenu = require('web.DynamicColumnMenu');

var QWeb = core.qweb;

SearchView.include({
    defaults: _.extend({}, SearchView.prototype.defaults, {
       disable_dynamic_column_listview: false
    }),
    init: function(ViewManager, Dataset, SearchManager) {
        var res = this._super.apply(this, arguments);
        var self = this;
        this.dynamic_column_menu = undefined;
        this.columns = SearchManager.columns || [];
        this.view_list = SearchManager.view_list;
        return res;
    },

    start: function () {
        var self = this;
        var supp = this._super.apply(this, arguments);
        var access = this.getSession().user_has_group('base.group_system');

        access.then(function(data) {
            self.all_users = data;
        });

        return $.when(supp, access).then(this.proxy('show_dynamic_columns_menu'));
    },

    show_dynamic_columns_menu: function() {
        if (!this.view_list) {
            return;
        }

        var menu_defs = []
        if (this.$buttons && !this.options.disable_dynamic_column_listview) {
            this.dynamic_column_menu = new DynamicColumnMenu(this, this.columns, this.all_users);
            menu_defs.push(this.dynamic_column_menu.appendTo(this.$buttons));
        }
        return $.when.apply($, menu_defs);
    }
});
});
