from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    url = "seleniumbase.io/apps/form_turnstile"
    sb.driver.uc_open_with_reconnect(url, 2)
    sb.press_keys("#name", "SeleniumBase")
    sb.press_keys("#email", "test@test.test")
    sb.press_keys("#phone", "1-555-555-5555")
    sb.click('[for="date"]')
    sb.click("td.is-today button")
    sb.click('div[class="select-wrapper"] input')
    sb.click('span:contains("9:00 PM")')
    sb.highlight_click('input[value="AR"] + span')
    sb.click('input[value="cc"] + span')
    sb.switch_to_frame("iframe")
    sb.driver.uc_click("span")
    sb.highlight("img#captcha-success", timeout=3)
    sb.highlight_click('button:contains("Request & Pay")')
    sb.highlight("img#submit-success")
    sb.highlight('button:contains("Success!")')
