# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.pool import Pool
from . import work
from . import invoice
from . import purchase


def register():
    Pool.register(
        work.Work,
        invoice.InvoiceLine,
        purchase.PurchaseLine,
        module='project_revenue', type_='model')
