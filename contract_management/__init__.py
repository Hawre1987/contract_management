# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe.utils import (today, flt, cint, fmt_money, formatdate,
	getdate, add_days, add_months, get_last_day, nowdate, get_link_to_form)

__version__ = '0.0.1'


def sample():
	# doc = frappe.get_single("Accounts Settings")
	# doc = frappe.db.get_single_value("Accounts Settings", "show_inclusive_tax_in_print")
	# print(doc.__dict__)
	is_inclusive = cint(frappe.get_single("Accounts Settings").show_inclusive_tax_in_print)
	print(is_inclusive)
