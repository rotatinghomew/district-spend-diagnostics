import unittest

from inspect_inputs import read_tables


class SourceRecords(unittest.TestCase):
    def test_sale_and_refund_candidates(self):
        tables = read_tables()
        lines = {row['line'] for row in tables['sales']}
        for row in tables['payment']:
            self.assertIn(row['line'],lines)
        for row in tables['refunds']:
            self.assertTrue(row['line'] or row['choices'])
            self.assertTrue(set(part for part in (row['line'] or row['choices']).split('+') if part) <= lines)

    def test_requested_previous_releases_exist(self):
        tables = read_tables()
        requests = {row['request']:row for row in tables['bulletins']}
        for row in requests.values():
            if row['previous']:
                former = requests[row['previous']]
                self.assertEqual('delivered',former['state'])
                self.assertLess(former['edition'],row['edition'])
        self.assertEqual(len({row['audience'] for row in requests.values()}),2)
        recoveries = {row['record']:row for row in tables['recoveries']}
        restored = recoveries['U3']
        planned = recoveries[restored['ref']]
        self.assertEqual(restored['terminal'],planned['terminal'])
        self.assertLess(restored['to'],planned['to'])
        self.assertEqual(restored['record'],recoveries['U6']['ref'])
        moves = [row for row in tables['terminals'] if row['merchant']=='Basil']
        self.assertEqual(moves[0]['active_to'],moves[1]['active_from'])
        self.assertGreater(int(restored['to'][11:13]),int(moves[0]['active_from'][11:13])-5)
        self.assertGreater(len({row['claim'] for row in tables['bulletins'] if row['request']=='N1'}),1)
