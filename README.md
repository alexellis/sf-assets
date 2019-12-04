SF Asset browser
===================

This project is a quick example to show how to take a publicly available dataset and to create a single-page mobile-friendly HTML app for exploring it in combination with location services.

Use-case: This use case comes from Robert Malmstein at Holberton School. According to Robert "sustainability is not just a trend, being green improves our environment and quality of live." - this dataset provides the geo-location of every publicly managed trash-can in San Francisco. Robert explained "Sometimes you just can't find a trash-can and that results in people littering, this app is a mash-up of public data from an SF survey of assets in 2016 - I want to make it accessible to everyone so they don't end up littering."

Robert's idea can be adapted to present any data-set to users in combination with Open Street Maps. It can be easily extended to allow crowd-sourcing and voting of new assets such as public benches for wellness breaks in a crowded city, or even for collecting evidence of potholes or other problems in public infrastructure.

## OpenFaaS Functions

* render - produces static HTML

The render function will make a call to the assets function for a certain asset like "Trash Cans", this matches up with a field called "Map Label" in the dataset.

* assets - queries built-in CSV data-set

This function parses the CSV file and applies optional filtering depending on the query-string passed in via the `?map_label=` querystring.

## Instructions

* Deploy to OpenFaaS Cloud

Add the OpenFaaS Cloud GitHub app to your account and push some code, that's it. HTTPS is built-in so location services will function as expected.

* Working locally

In order to use location services you will need to work over HTTPS, so either set up a reverse proxy or use ngrok to front your API Gateway.

## Acknowledgements

Inspiration - idea from Robert Malmstein - Holberton School.

Dataset - from [SF Data](https://data.sfgov.org/Culture-and-Recreation/Assets-Maintained-by-the-Recreation-and-Parks-Depa/ays8-rxxc)


