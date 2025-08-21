import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.letskodeit.com/practice"

@pytest.fixture(autouse=True)
def open_practice_page(driver):
    driver.get(URL)
    yield


def test_title(driver):
    assert "Practice" in driver.title


# Radio Button Example
def test_element_buttons(driver):
    # Locate by ID, XPath, or CSS
    bmw_radio = driver.find_element(By.XPATH, "//input[@id='bmwradio']")
    bmw_radio.click()
    assert bmw_radio.is_selected()


# Checkbox Example
def test_element_checkbox(driver):
    bmw_checkbox = driver.find_element(By.XPATH, "//input[@id='bmwcheck']")
    bmw_checkbox.click()
    assert bmw_checkbox.is_selected()


#Switch Window Example
def test_element_window(driver):
    bmw_window = driver.find_element(By.XPATH, "//button[@id='openwindow']")
    bmw_window.click()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    original_window = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    assert "All Courses" in driver.title

    driver.close()
    driver.switch_to.window(original_window)


#Switch Tab Example
def test_element_tab(driver):
    bmw_tab = driver.find_element(By.XPATH, "//a[@id='opentab']")
    bmw_tab.click()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    original_window = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    assert "All Courses" in driver.title

    driver.close()
    driver.switch_to.window(original_window)


# Select Class Example
def test_element_select(driver):
    bmw_select = driver.find_element(By.XPATH, "//select[@id='carselect']")
    dropdown = Select(bmw_select)
    dropdown.select_by_visible_text("Benz")
    assert dropdown.first_selected_option.text == "Benz"


#Multiple Select Example
def test_element_options(driver):
    multi_select_element = driver.find_element(By.XPATH, "//select[@id='multiple-select-example']")
    multi_select = Select(multi_select_element)
    assert multi_select.is_multiple
    multi_select.select_by_visible_text("Apple")
    multi_select.select_by_visible_text("Orange")
    multi_select.deselect_by_visible_text("Apple")
    assert multi_select.first_selected_option.text == "Orange"


#Auto Suggest Example
def test_element_auto_input(driver):
    auto_input = driver.find_element(By.XPATH, "//input[@id='autosuggest']")
    auto_input.click()
    auto_input.send_keys("au")

    wait = WebDriverWait(driver, 10)
    suggestion_list = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.ui-autocomplete")))
    suggestions = suggestion_list.find_elements(By.TAG_NAME, "li")

    for suggestion in suggestions:
        if "Mobile App Automation" in suggestion.text:
            suggestion.click()
            break

        assert auto_input.get_attribute("value") == "Mobile App Automation"

#Enabled/Disabled Example
def test_element_enabledDisabled(driver):
    disable_button = driver.find_element(By.XPATH, "//input[@id='disabled-button']")
    enable_button = driver.find_element(By.XPATH, "//input[@id='enabled-button']")
    input_field = driver.find_element(By.ID, "enabled-example-input")

    # First, ensure the field is enabled and can accept text
    enable_button.click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='enabled-example-input']"))
    )
    input_field.clear()
    input_field.send_keys("Subhadip")
    time.sleep(1)
    assert input_field.get_attribute("value") == "Subhadip"

    # Now disable the field and check it is disabled
    disable_button.click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "enabled-example-input"))
    )
    assert not input_field.is_enabled(), "Input field should be disabled"

#Element Displayed Example
def test_element_displayed_showHide(driver):
    hide_button = driver.find_element(By.XPATH, "//input[@id='hide-textbox']")
    show_button = driver.find_element(By.XPATH, "//input[@id='show-textbox']")
    displayed_text = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

    hide_button.click()
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located((By.XPATH, "//input[@id='displayed-text']"))
    )
    assert not displayed_text.is_displayed(), "Textbox should be hidden"

    show_button.click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='displayed-text']"))
    )
    assert displayed_text.is_displayed(), "Textbox should be visible"

#Switch To Alert Example
def test_element_alert(driver):
    alert_button = driver.find_element(By.XPATH, "//input[@id='alertbtn']")
    confirm_button = driver.find_element(By.XPATH, "//input[@id='confirmbtn']")
    input_field = driver.find_element(By.XPATH, "//div[@id='alert-example-div']//input[@id='name']")

    input_field.send_keys("Subhadip")
    time.sleep(2)

    alert_button.click()

    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    confirm_button.click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    confirm_alert = driver.switch_to.alert
    confirm_alert.dismiss()


#Mouse Hover Example
def test_element_mouseHover(driver):
    # Locate the Mouse Hover button and the hidden menu options
    mouse_hover_button = driver.find_element(By.XPATH, "//button[@id='mousehover']")
    top_option = (By.XPATH, "//a[normalize-space()='Top']")
    reload_option = (By.XPATH, "//a[normalize-space()='Reload']")

    actions = ActionChains(driver)
    actions.move_to_element(mouse_hover_button).perform()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(top_option))


    driver.find_element(*top_option).click()

    actions.move_to_element(driver.find_element(By.XPATH, "//button[@id='mousehover']")).perform()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(reload_option))
    driver.find_element(*reload_option).click()
