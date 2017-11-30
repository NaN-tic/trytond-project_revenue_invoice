# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['PurchaseLine']


class PurchaseLine:
    __metaclass__ = PoolMeta
    __name__ = 'purchase.line'

    def get_invoice_line(self):
        lines = super(PurchaseLine, self).get_invoice_line()
        for line in lines:
            line.purchase_work = self.work if self.work else None
        return lines
