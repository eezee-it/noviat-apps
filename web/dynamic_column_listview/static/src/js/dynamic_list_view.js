odoo.define('dynamic_column_listview.ListView', function (require) {
"use strict";

var ListView = require('web.ListView');

ListView.include({
    init: function (params, ViewManager) {
        this.view_id = params.view_id;
        window.lview = this;
        var res = this._super.apply(this, arguments);
        this.controllerParams.view_id = params.view_id;
    }
});
});