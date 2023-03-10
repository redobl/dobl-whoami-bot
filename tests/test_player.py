import unittest
import os
import sys


# prepare sys.path for importing modules from parent directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import mapparser
import player
import command_help


class TestPlayer(unittest.TestCase):
    gameMap = mapparser.Map(os.path.join(current, "test.tmx"))

    def test_format_inventory_list(self):
        self.maxDiff = None
        self.assertEqual(self.gameMap.get_player("test_player5", 5).inventory, [""])
        self.assertEqual(player.Player.format_inventory_list(
            [
                "27ж",
                "1э. test item 1 {???, ???hidden} (1/1)",
                "2. test item 2 {???, shown???hidden, ???(hidden)shown, full} (1/10)",
                "3э. test item 3 (real item name) {something, ???} (2/10)",
                "4. test item 4 {shown, shown2, ???(hidden)shown} (20/20)"
            ]),
            [
                "[33m27ж[0m",
                "[32m1э[0m. test item 1 {[35m???[0m, [35m???[0m} (1/1)",
                "2. test item 2 {[35m???[0m, shown?, ?shown, full} [31m(1/10)[0m",
                "[32m3э[0m. test item 3 {something, [35m???[0m} [31m(2/10)[0m",
                "4. test item 4 {shown, shown2, ?shown} (20/20)"
            ]
        )

        self.assertEqual(player.Player.format_inventory_list(
            [
                "387ж",
                "1. item1 (aitem1+1) {???prop, ???prop} (30/30) за 66ж",
                "2. item2+1 {???prop, ???prop} (20/20) за 66ж",
                "3. item3 (aitem3) {???prop, ???prop, ???prop} (5/20) за 55ж"
            ]),
            [
                "[33m387ж[0m",
                "1. item1 {[35m???[0m, [35m???[0m} (30/30) за [33m66ж[0m",
                "2. item2+1 {[35m???[0m, [35m???[0m} (20/20) за [33m66ж[0m",
                "3. item3 {[35m???[0m, [35m???[0m, [35m???[0m} [31m(5/20)[0m за [33m55ж[0m"
            ]
        )

    def test_format_stats(self):
        self.assertEqual(self.gameMap.get_player("test_player9", 9).format_HP(), "100/100.0 (100)")
        self.assertEqual(self.gameMap.get_player("test_player11", 11).format_HP(), "127/151.3 (154)")
        self.assertEqual(self.gameMap.get_player("test_player11", 11).format_MP(), "47/47.0 (47)")

    def test_list_inventory_commands(self):
        self.assertEqual(command_help.list_inventory_commands(self.gameMap.get_player("test_player11", 11)),
                         {
                            "карта": 0
                         })
        self.assertEqual(command_help.list_inventory_commands(self.gameMap.get_player("test_player12", 12)),
                         {
                            "карта": 2
                         })

if __name__ == '__main__':
    unittest.main()
