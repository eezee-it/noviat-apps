odoo.define('dynamic_column_listview.ViewManager', function (require) {
"use strict";

var core = require('web.core');
var ListView = require('web.ListView');
var SearchView = require('web.SearchView');
var ViewManager = require('web.ViewManager');
var QWeb = core.qweb;


ViewManager.include({
    setup_search_view: function () {
        var view_list = this && this.views && this.views.list;
        var list = view_list && view_list.fields_view;
        var fields = list && list.fields;
        list = list &&  list.fieldsInfo && list.fieldsInfo.list;

        if (list) {
            this.search_fields_view.view_list = view_list;
            this.search_fields_view.columns = _.sortBy(
                _.map(list || [], function (item) {
                    return {
                        'name': item.name,
                        'string': fields[item.name].string,
                        'invisible': item.invisible,
                    }
                }), 'string'
            );
        }
        return this._super.apply(this, arguments);
    }
});
});
