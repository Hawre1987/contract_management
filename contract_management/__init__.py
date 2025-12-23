from __future__ import unicode_literals

# REMOVE the top-level frappe.utils import from here

__version__ = '0.0.1'

def sample():
    # Move the imports INSIDE the function
    import frappe
    from frappe.utils import cint
    
    # Now it only tries to find frappe when sample() is actually called,
    # not when the app is being installed.
    is_inclusive = cint(frappe.get_single("Accounts Settings").show_inclusive_tax_in_print)
    print(is_inclusive)
