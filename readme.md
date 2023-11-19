# Scraping Apartments for rent

![GitHub repo size](https://img.shields.io/github/repo-size/ahmedemad2002/Scrape-Bayut)
![GitHub contributors](https://img.shields.io/github/contributors/ahmedemad2002/Scrape-Bayut)
![GitHub stars](https://img.shields.io/github/stars/ahmedemad2002/Scrape-Bayut?style=social)
![GitHub forks](https://img.shields.io/github/forks/ahmedemad2002/Scrape-Bayut?style=social)

## Scraping data from [Bayut](https://www.bayut.eg/en)

This project aims to scrape data about apartments for rent in Egypt from bayut page of [Residential Properties for rent in Egypt](https://www.bayut.eg/en/egypt/properties-for-rent/?rent_frequency=any&gclid=Cj0KCQjwtJKqBhCaARIsAN_yS_lRWVDi4h180vpcPoYjpw3noFLpp2pKjA1Kr1C5YDJ5oWeknb9kaRwaAtjnEALw_wcB)

## Table of Contents

- [Introduction](#introduction)
- [File Descriptions](#file-descriptions)
- [Results](#results)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to scrape data about apartments for rent in Egypt from bayut page of [Residential Properties for rent in Egypt](https://www.bayut.eg/en/egypt/properties-for-rent/?rent_frequency=any&gclid=Cj0KCQjwtJKqBhCaARIsAN_yS_lRWVDi4h180vpcPoYjpw3noFLpp2pKjA1Kr1C5YDJ5oWeknb9kaRwaAtjnEALw_wcB) to use this data to analyze it and see the trends in this data.
**Scrapy** is the main tool used in this project.

## File Descriptions

-bayut: The main file which contains the Scrapy project files like the settings file and the spiders directory.
-data: The directory containing the scraped data and data sample.

## Results

Scraped about 4400 property succesfully in the **Full_data.json** file.
created a data sample file to make the output format available without downloading the full data.

## Usage

Explain how to use your code and reproduce the results. Include any dependencies and installation steps.

```bash
# Clone the repository
git clone https://github.com/ahmedemad2002/Scrape-Bayut.git

# Navigate to the project folder
cd Scrape-Bayut

# Install dependencies (if any)
pip install -r requirements.txt

# Run the code
python main.py
