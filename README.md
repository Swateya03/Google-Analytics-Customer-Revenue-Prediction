# Google Analytics Customer Revenue Prediction
The principle known as the 80/20 rule, or the Pareto principle, has demonstrated its validity across a multitude of businesses. According to this rule, approximately 80% of a company's revenue originates from the purchases made by a mere 20% of its customers. 
## Introduction
- Google has published a Merchandise customer dataset (2016-2019), which includes online/referral customer information as well as the number of transactions gathered per customer.
- We have created a predictive model utilizing the Gstore Customer Dataset to anticipate total revenue per customer, allowing us to make better use of marketing budget.
- In this study , we have also interpreted the most influential factors on Total Revenure projection using several models.
## Business Problem
1. Marketing teams need to invest bugdet appropriately in promotional strategies to attract potential customers.
2. Many firms have a small percentage of consumers that generate most of their revenue.
3. The most difficult component is predicting these small percentage of customers and the quantity of income that can be earned from these customers in the future.
## Understanding the data
(download link -> https://www.kaggle.com/competitions/ga-customer-revenue-prediction/data )
The total files in the link provided are :
- sample_submission.csv
- sample_submission_v2.csv
- test.csv
- test_v2.csv
- train.csv
- train_v2.csv
### About the dataset 
- 2.1 million total observations.
- A total of 12 features (some are JSON collection set).
- There are two dates , four numerical IDs, and seven categorical features.
- The four categorical attributes (device, geoNetwork, totals, and trafficSource) are stored in a JSON set and can be split up into different attributes for analyis.
- The TransactionRevenue numbers in the Totals JSON field will be the predictive attribute.
### Feature Description
- fullVisitorId(string): The unique ID provided to visitor.
- channelGrouping(string) : channels are broad categories that show how visitors reached your website.
- date(string): The session's date in YYYYMMDD format.
- visitId(integer) : A session identifier specific to the visitor.
- visitNumber(integer) : The visitor's unique session number.For the initial Visit by the visitor, it will be set to 1.
- device.browser(string) : The visitor's device browser.
- device.operatingSystem(string) : Visitor Operating System
- device.isMobile(boolean) : If the device is mobile
- device.deviceCategory(string) : Device type mobile or tablet or desktop
- geoNetwork.continent(string) : Depending on IP address, the continent from which sessions started.
- geoNetwork.subContinent(string) : Based on IP address, the subcontinent from where sessions started.
- geoNetwork.country(string) : The IP adress-based nation from which sessions started.
- geoNetwork.region(string) : The area where sessions start, as determined by IP addresses. In the US, a region is equivalent to a state, like New York
- geoNetwork.metro(string) : The origin of traffic is identified by the three-digit Designated Market Area (DMA) code, which is derived from visitor's IP addresses or Geographical IDs.
- geoNetwork.city(string) : Visitor's City
- geoNetwork.networkDomain(string) : The visitor's service provider's domain name
- total.hits(integer) : A hit is a request for a file from a web server as a result of visitor action. As a result, it can be used as a measure of visitor activity. Here is number of hits overall for thw session.
- totals.pageviews(integer) : Amount of pages viewed overall during the session.
- totals.transactionRevenue(integer) : Total Revenue made during that specific Session.
- trafficSource.campaign(string) : An advertising campaign is a collection of commercials with a single message.
- trafficSource.source(string) : The source of the flow of traffic.Possibly the referring hostname, the search engine's name, or the utm source URL parameter value.
- trafficSource.medium(string) : The source's medium traffic. It can be 'organic' , 'cpc', 'refferal' or the utm medium URL query parameter value.
- trafficSource.keyword(string) : The traffic source's keyword is typically set when the trafficSource.medium value is 'organic' or 'cpc'.
- trafficSource.refferalPath(string) : If trafficSource.medium is 'referral', then this is setting to the path of the refferer. (TrafficSource.source contains the referrer's host name)

