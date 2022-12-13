from lesson14_page_object.page_objects.MainPage import MainPage
from lesson14_page_object.page_objects.UserPage import UserPage
from lesson14_page_object.page_objects.ProductPage import ProductPage
from lesson14_page_object.page_objects.ComparisonPage import ComparisonPage
from lesson14_page_object.page_objects.CartPage import CartPage
from lesson14_page_object.page_objects.elements.SuccessAlert import SuccessAlert


def test_add_to_wish_list(browser):
    product_name = MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_wish_list()
    SuccessAlert(browser).click_login()
    UserPage(browser) \
        .login_with("test2@mail.ru", "test") \
        .click_link('Wish List') \
        .verify_product_link(product_name)


def test_add_to_cart(browser):
    product_name = MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_cart()
    SuccessAlert(browser).click_shopping_cart()
    CartPage(browser) \
        .verify_product(product_name) \
        .go_to_checkout()
    UserPage(browser) \
        .login_with("test2@mail.ru", "test") \
        .verify_pay_form()


def test_add_to_cart_from_comparison(browser):
    product_name = MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_comparison()
    SuccessAlert(browser).click_product_comparison()
    ComparisonPage(browser) \
        .verify_product_link(product_name) \
        .add_to_cart()
    SuccessAlert(browser).click_shopping_cart()
    CartPage(browser) \
        .verify_product(product_name) \
        .go_to_checkout()
    UserPage(browser) \
        .login_with("test2@mail.ru", "test") \
        .verify_pay_form()
