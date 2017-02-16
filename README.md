[![coverage report](https://gitlab.com/eezee-it/epl/badges/9.0/coverage.svg)](https://gitlab.com/eezee-it/epl/commits/9.0) [![build status](https://gitlab.com/eezee-it/epl/badges/9.0/build.svg)](https://gitlab.com/eezee-it/epl/commits/9.0)

Eezee-It Platinum
==================

CONFIGURATION TO INSTALL THE EPL l10n_be MODULE:

The --addons-path parameter's order must be different when we want to
install the EPL l10n_be module.
The first directory for related project should be the epl/account location,
to have the correct l10n_be module installed and to avoid data errors with CoA.
Thus, because we want to install the l10n_be created for EPL instead
the standard odoo one, but we need to use the same name to avoid errors
with standard odoo reports.

So, the addons-path should be like:
--addons-path="epl/account,odoo/enterprise/,odoo/community/addons/"

