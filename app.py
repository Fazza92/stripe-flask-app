from flask import Flask, render_template,request,redirect,url_for
import stripe

app = Flask(__name__)

public_key = "pk_test_TYooMQauvdEDq54NiTphI7jx SECRET_KEY=sk_test_4eC39HqLyjWDarjtT1zdp7dc"

stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"