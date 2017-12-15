# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import fields
from trytond.pyson import Eval
from trytond.pool import PoolMeta

__all__ = ['Work']


class Work:
    __metaclass__ = PoolMeta
    __name__ = 'project.work'
    invoice_lines = fields.One2Many('account.invoice.line',
        'purchase_work', 'Invoice Lines', domain=[
            ('invoice.company', '=', Eval('company', -1)),
            ],
        depends=['company'])

    @classmethod
    def get_amounts(cls, works, names):
        res = super(Work, cls).get_amounts(works, names)
        # sum added invoices lines in current project or childs
        if 'invoiced_cost' in names:
            for work in works:
                for line in work.invoice_lines:
                    if line.type == 'line':
                        res['invoiced_cost'][work.id] += line.amount
        return res
