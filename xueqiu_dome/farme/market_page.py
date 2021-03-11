from xueqiu_dome.farme.basepage import BasePage
from xueqiu_dome.farme.search import Search


class Market(BasePage):

    def goto_serach(self):

        return Search(self.driver)

