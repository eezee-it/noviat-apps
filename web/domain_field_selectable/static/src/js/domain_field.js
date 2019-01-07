odoo.define('domain_field_selectable.domain_field', function (require) {
"use strict";

    var core = require('web.core');   
    var basic_fields = require('web.basic_fields');
    var view_dialogs = require('web.view_dialogs');
    var _t = core._t;

    basic_fields.FieldDomain.include({
        _onShowSelectionButtonClick: function (e) {
            /*
            Override the standard Method, if option selectable, thus
            Permit to select items.
             */
            e.preventDefault();
            if (!this.nodeOptions.selectable) {
                this._super.apply(this, arguments);
                return;
            }
            var domain_selector = this.domainSelector;

            new view_dialogs.SelectCreateDialog(this, {
                title: _t("Selected records"),
                res_model: this._domainModel,
                domain: this.value || "[]",
                no_create: false,
                readonly: false,
                disable_multiple_selection: false,
                on_selected: function(selected_items) {
                    var current_domain = domain_selector.getDomain();
                    var new_domain = ["&"];
                    
                    $(current_domain).each(function(index, value) {
                        if (!Array.isArray(value) || !value.includes('id')) {
                            new_domain.push(value);
                        }
                    });
                    selected_items = $(selected_items);
                    selected_items.each(function(index, value) {
                        var $this = $(this);
                        if($this[0] !== selected_items.last()[0]) {
                            new_domain.push("|");
                        }
                        new_domain.push(["id", "=", value.id]);
                    });
                    domain_selector.setDomain(new_domain);
                    domain_selector.trigger_up("domain_changed", {child: this});
                },
            }).open();

        },

    });

});

