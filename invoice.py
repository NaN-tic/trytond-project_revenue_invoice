# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval

__all__ = ['InvoiceLine']


class InvoiceLine:
    __metaclass__ = PoolMeta
    __name__ = 'account.invoice.line'
    purchase_work = fields.Many2One('project.work', 'Purchase Work Effort',
        states={
            'invisible': (Eval('_parent_invoice', {}).get('type') != 'in'),
        }, domain=[
            ('company', '=', Eval('_parent_invoice', {}).get('company', -1)),
        ])
