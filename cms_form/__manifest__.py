# Copyright 2017 Simone Orsi
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "CMS Form",
    "summary": """
        Basic content type form""",
    "version": "15.0.1.0.0",
    "license": "LGPL-3",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "mainainers": ["simahawk"],
    "depends": ["website", "cms_info", "cms_status_message"],
    "data": [
        "security/cms_form.xml",
        "templates/form.xml",
        "templates/widgets.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "cms_form/static/src/scss/cms_form.scss",
            "cms_form/static/src/scss/progressbar.scss",
            "cms_form/static/src/js/ajax.js",
            "cms_form/static/src/js/date_widget.js",
            "cms_form/static/src/js/lock_copy_paste.js",
            "cms_form/static/src/js/master_slave.js",
            "cms_form/static/src/js/select2widgets.js",
            "cms_form/static/src/js/textarea_widget.js",
        ]
    },
    "installable": True,
}
