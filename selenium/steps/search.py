# -*- coding: utf-8 -*-
# pylint: disable=not-callable
"""
System Test example using Behavior-Driven Development (BDD) with Behave (Gherkin)
and Selenium, adapted to use undetected-chromedriver to avoid CAPTCHA issues.
"""

import time

import undetected_chromedriver as uc  # pylint: disable=import-error
from behave import given, then, when
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@given("I am on the Google homepage")
def open_browser(context):
    """Opens Google in Chrome (using undetected-chromedriver)."""
    # Configuración del navegador
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    # Inicia el navegador
    context.driver = uc.Chrome(options=options)
    context.driver.get("https://www.google.com")

    # Maneja el banner de cookies si aparece
    try:
        consent_button = WebDriverWait(context.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "L2AGLb"))
        )
        consent_button.click()
    except TimeoutException:
        pass  # Si no aparece, continuar


@when('I search for "{query}"')
def search(context, query):
    """Searches something in Google."""
    # Espera a que aparezca la barra de búsqueda
    search_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Escribe el texto y presiona Enter
    search_box.send_keys(query)
    time.sleep(1)  # Pausa natural
    search_box.send_keys(Keys.RETURN)

    # Espera a que carguen los resultados
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#search"))
    )


@then('the results page title should start with "{query}"')
def verify_results(context, query):
    """Checks that the search results page title starts with the query."""
    WebDriverWait(context.driver, 10).until(EC.title_contains(query))
    title = context.driver.title

    try:
        assert title.lower().startswith(query.lower())
        print(f"✅ Test passed. Title: {title}")
    finally:
        context.driver.quit()
