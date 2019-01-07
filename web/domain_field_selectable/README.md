# Domain Field Selectable

On Odoo 11.0 we can't select record on a char field with the widget "domain", with this module if you added the option "'selectable': 1" to the widget, you can select records to add to the filter.

## Exemple of use 

```xml
<field name="mailing_domain" widget="domain" attrs="{'invisible': [('mailing_model_name', '=', 'mail.mass_mailing.list')]}" options="{'model': 'mailing_model_real', 'selectable':1}" context="{'search_default_not_opt_out':1}"/>
```

## Improvement

* On Odoo 10.0 and before if you make a search on the domain pop-up, the "domain" field received this domain, whith this module each ids of search is added to the domain.
