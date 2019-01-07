odoo.define('web.DynamicColumnMenu', function (require) {
"use strict";

var Widget = require('web.Widget');
var core = require('web.core');
var data_manager = require('web.data_manager');
var search_inputs = require('web.search_inputs');

var QWeb = core.qweb;

return Widget.extend({

    template: 'SearchView.DynamicColumnMenu',

    events: {
        'click': function (event) {
            var $t = $(event.target);
            var $p = $t.closest('#dynamic_dropdown_menu');

            var is_input = $t.is('#dynamic_column_dropdown input');
            var is_button = $t.is('#dynamic_column_dropdown button');

            if (is_input || is_button) {
                event.stopPropagation();
            }
        },
        'click #select_all_columns': function (event) {
            var $t = $(event.currentTarget);
            var $p = $t.closest('#dynamic_dropdown_menu');
            $p.find('input.column_checkbox[type=checkbox]').prop('checked', true);
        },
        'click #unselect_all_columns': function (event) {
            var $t = $(event.currentTarget);
            var $p = $t.closest('#dynamic_dropdown_menu');
            $p.find('input.column_checkbox[type=checkbox]').prop('checked', false);
        },
        'click #reset_dynamic_columns': function (event) {
            this.search_view.view_list.controller.saveColumns([], false, true);
        },
        'click #save_dynamic_columns': function (event) {
            var $t = $(event.currentTarget);
            var $p = $t.closest('#dynamic_dropdown_menu');
            var is_all_users = $p.find('#save_for_all_users').is(':checked');
            var is_save_order = $p.find('#save_column_order').is(':checked');
            var $cols = $p.find('input.column_checkbox[type=checkbox]:checked');
            var col = _.map($cols, function (elem) {
                return $(elem).data('id');
            });
            this.search_view.view_list.controller.saveColumns(col, is_all_users, is_save_order);
        },
        'shown.bs.dropdown': function (event) {
            console.log('shown.bs.dropdown');
        },
        'hidden.bs.dropdown': function () {
            console.log('hidden dropdown')
        },
    },

    _get_column_selector: function (id, name, checked) {
        var dom = "<li class='dynamic_column_checkbox'>";
        dom += "<input type='checkbox' name='cb' class='column_checkbox' data-id='" + id + "' " + (checked ? "checked='checked'" : "") + " />";
        dom += "<span> " + name + "</span>";
        dom += "</li>";
        return dom;
    },

    init: function (parent, fields, allusers) {
        this._super(parent);
        this.search_view = parent;
        this.fields = fields;
        this.all_users = allusers;
    },

    start: function () {

        var self = this;

        this.$button = this.$('#select_columns');
        this.$menu = this.$('#dynamic_dropdown_menu');
        this.$fields = this.$menu.find('#showcb');

        this.$save_all_users = this.$menu.find('#save_for_all_users');
        this.$save_column_order = this.$menu.find('#save_column_order');

        if (!this.all_users) {
            this.$('#apply_for_all').detach();
        }

        this.$fields.empty();
        this.$save_all_users.prop('checked', false);
        this.$save_column_order.prop('checked', false);

        var columnList = '';
        _.each(this.fields, function (field) {
            columnList += self._get_column_selector(field.name, field.string, !field.invisible);
        });
        if (!columnList) {
            columnList = '<strong>No columns found on this view</strong>';
        }
        $(columnList).appendTo(this.$fields);
    }
});
});