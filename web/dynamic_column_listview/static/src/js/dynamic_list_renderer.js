odoo.define('dynamic_column_listview.ListRenderer', function (require) {
"use strict";

var ListRenderer = require('web.ListRenderer');

ListRenderer.include({

    init: function (parent) {
        var res = this._super.apply(this, arguments);
        this.drag_enabled = !!parent.views;
        return res;
    },

    _renderHeaderCell: function (node) {

        var $col = this._super.apply(this, arguments);
        if (!this.drag_enabled) {
            return $col;
        }

        var name = node.attrs.name;
        var field = this.state.orderedBy;
        $col.addClass('dragable');
        $col.data('field', name);
        $col.prepend('<span class="column_handle fa fa-arrows"/>');
        return $col;

    },

    _renderView: function () {
        var self = this;
        var res = this._super.apply(this, arguments);
        self.enableDrag();
        return res;
    },

    enableDrag: function () {
        var self = this;
        var $table = this.$el.find('.o_list_view');

        $table.dragtable({
            dragaccept:'.dragable',
            dragHandle:'.column_handle',
            persistState: function(table) {
                var columns = _.compact(_.map(table.el.find('th'), function (elem) {
                    var $elem = $(elem);
                    return $elem.data('field');
                }));
                console.log(columns);
                self.trigger_up('memoriseColumnOrder', {columns:columns});
            },
            restoreState: function () {},
        });
    },
});
});
