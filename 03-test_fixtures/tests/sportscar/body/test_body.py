from pytest import mark


@mark.smoke
@mark.body
class BodyTest:
    @mark.ui
    def test_can_navigate_to_body_pages(self, chrome_browser):
        chrome_browser.get("https://www.motortrend.com/")
        assert True

    def test_bumper(self):
        assert False

    def test_windshield(self):
        assert True
