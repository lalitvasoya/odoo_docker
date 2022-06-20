from odoo.tests import common


class TestTodoModel(common.TransactionCase):

    def test_create_action_first(self):
        task = "abc"
        record = self.env['todo'].create({'task': task})
        self.assertEqual(record.task, task)

    def test_create_action_second(self):
        task = "abc"
        record = self.env['todo'].create({'task': task})
        task = "updated todo"
        record = self.env['todo'].search([], order='id desc')[0]
        id_updated = record.write({'task': task})
        self.assertEqual(id_updated, True)
        self.assertEqual(record.task, task)
