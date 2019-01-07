odoo.define('dynamic_column_listview.view_dialogs', function (require) {
"use strict";

var ViewDialogs = require('web.view_dialogs').SelectCreateDialog;

function create_child (name) {
    return {
        attrs: {
            modifiers: {
                readonly: true,
                invisible: true,
                column_invisible: true,
            },
            name: name,
            invisible: true,
        },
        children: [],
        tag: "field",
    }
}

ViewDialogs.include({
    setup: function (search_defaults, fields_views) {
        /*
        This code is kept commented if some developper want to try to make dyanmic_column_view
        Work with searchview

        var self = this;
        var list = fields_views.list;
        var fields = list.fields;
        var arch_children = [];
        list = list && fields_views.list.fieldsInfo && fields_views.list.fieldsInfo.list;

        if (list && fields && fields_views.search) {
            fields_views.search.columns = _.map(fields || [], function (item) {
                return {
                    'name': item.name,
                    'string': item.string,
                    'invisible': !list[item.name],
                }
            });
        }
        */
        var res = this._super.apply(this, arguments);
        /*
        This code is kept commented if some developper want to try to make dyanmic_column_view
        Work with searchview

        res.then(function (args) {
            fields_views.search.view_list.controller = self.list_controller;
            var children = self.list_controller.renderer.arch.children
            if (fields) {
                var exists = _.map(children, function (c) {
                    return c.attrs.name;
                });
                _.each(fields, function (field, key) {
                    if (!_.contains(exists, key)) {
                        children.push(create_child(key));
                    }
                });
            }
        });
        */
        return res;
    }
});
});