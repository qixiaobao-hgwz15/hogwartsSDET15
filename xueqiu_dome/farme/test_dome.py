from xueqiu_dome.farme.mainPage import MainPage


class TestMain:
    def test_main(self):
        main=MainPage().goto_market().goto_serach().search()
        # main.