# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import (doctest_setup, doctest_teardown,
    doctest_checker)

class ProjectRevenueInvoiceTestCase(ModuleTestCase):
    'Test Project Revenue Invoice module'
    module = 'project_revenue_invoice'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProjectRevenueInvoiceTestCase))
    suite.addTests(doctest.DocFileSuite('scenario_project_revenue_invoice.rst',
            setUp=doctest_setup, tearDown=doctest_teardown, encoding='UTF-8',
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE,
            checker=doctest_checker))
    return suite
