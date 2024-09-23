from POM.Homepage import Homepage


def homepage_ecm(driver):
    homepage = Homepage(driver)
    driver.refresh()
    text=homepage.verify_explore().text
    assert "Explore" in text
    print(text)
    # text1=homepage.verify_consent().text
    # assert "Consent" in text1
    # print(text1)
    print(homepage.click_machines().text)

