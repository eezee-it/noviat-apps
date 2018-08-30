Eezee-It Platinum
=================

In this File we will add a description of each module
Please don't add the description anywhere.
Use this logic

-Your module is present in an epl subfolder, it is the first title under wich it must be present
- If your module is under Account folder, place the description under the title "Account"
- If there is no title yet, add it but respect the alphabetical order

-The subtitle is Module name - technical_name
- Use Alphabetical order too

# Account

## Accounting Prorata Taxes - account_prorata_taxes

Add a wizard to allow you to create pro rata taxes.

Definition: A pro rata taxe is a taxe that only a percentage is deductible

- The pop up will create an accounting period.
- The taxe use for pro rata must be define before the pop up launch.
- The taxe generate by the pop up will have a boolean checked to make a difference with the other

Point of Attention:

- Work only for purchase taxe, normally should work for sales too but it was never tested

## Account Refund Reason - account_refund_reason

Allow you to configure the reason of a refund.
This reason will be selected in the refund popup instead of a free text.

## Refund Invoice Journal - refund_invoice_journal

Allow you to select a specifi journal when you make refund.
By default, odoo use the same journal than the one of the invoice

## VAT Report Eezee-it - vat_report_eze

Add a new vat report in the accounting view.
This report is much more accurate

# CRM

## Only Postal - only_postal

Show an error user if you try to send an email to a partner that doesn't want it.

Works only for sale and invoice

To know if the customer want email or not, there is a boolean in the view form.
This boolean can be filled from the partner tag

# Event

## Event Settings - event_config_settings

Add a check box in settings to allow you to active tags in EPL inscriptions:

- Show sub-menu Event Tags under configuration.
- Show tags in attendees view form.

## Event mass registration - event_mass_registration

## Event email filter - event_registration_mail_filter

## Event Tags - event_registration_tags

Allow you to add new categories tags:

- Add sub-menu Event Tags under configuration.
- Add tags in attendees view form.

# Mass Mailing

## Mailing List: Mass-Selection - mailing_list_mass_selection

## E-mailing base - mass_mailing_base

## Mass mailing event - mass_mailing_event

## Preference center - mass_mailing_preference_center

# Project

## Project Details View - project_details_view

Open project's form view when clicking on its kanban card.
By default, it open the task

# Tools

## Partner Token - partner_token

Add a field token in the partner view visible only in debug mode.
This field is filled/updated when the write date of the partner is update

## Whats my IP - whats_my_ip

Allow you to have the IP of the person that join your odoo

## Automatic update analytic account in invoices force_update_analytic_invoice

Force the change of the analytic account after confirmation of the invoice.
wizard allows you to modify the analytical accounts of the invoice if it is
validated

# Web

# Website

## Portal Form - portal_form