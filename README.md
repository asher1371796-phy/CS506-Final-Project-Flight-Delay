# CS506-Final-Project-Flight-Delay
CS506 final project: Predicting flight delays ahead using historical flight and weather data at Boston Logan Airport.

## 1. Group Members
Mengkai Li

Yilin Lyu

Zhen Zheng

## 2. Project Description

Air travel is typically used for journeys or missions where timeliness is critical; consequently, delays or cancellations often entail significant costs. This project will investigate whether information available at booking time can be used to predict if a domestic flight departing from Boston Logan International Airport will arrive late. By comparing several prediction methods and examining when errors occur, we aim to provide passengers with data-driven, booking time on-time performance predictions, enabling them to plan their onward travel accordingly and minimize potential disruptions. Given the multitude of factors contributing to flight delays, our initial efforts will focus on flight route information such as destination, departure time and historical climate conditions at Boston Logan International Airport (BOS). Subsequently, we will evaluate the model's predictive performance and consider incorporating additional influencing factors in later stage of the project.

We plan to complete the main analysis over eight weeks, followed by preparation of the final report and presentation.

- **Weeks 1–2:** Download BTS flight records and IEM weather observations. Check data availability, field definitions, and the proportion of canceled flights.
- **Weeks 3–4:** Clean the data, prepare separate delay and cancellation datasets, and construct historical weather features. 
- **Weeks 5–6:** Train logistic regression and decision tree models using 2020–2024 data. Use 2025 data for validation and parameter selection. 
- **Weeks 7–8:** Refit the selected models using 2020–2025 data and evaluate them on 2026/1-7 flights. Analyze errors and look for reasons.
- **Early December:** Finalize the reproducible code, README report, visualizations, tests, and recorded presentation for submission by December 9.

Potential challenges include missing data, unequal numbers of delayed and non-delayed flights, and changes in flight patterns across years. Flights during the COVID-19 pandemic may differ from those in later years, which could affect predictions on the test set. Historical climate summaries also cannot capture unexpected weather events. We will consider these limitations when interpreting model performance and discussing how useful the predictions may be for passengers.

## 3. Project Goals

The primary goal of this project is to develop a binary classification model that predicts whether a domestic flight departing from Logan Airport will arrive at its destination at least 15 minutes late or cancelled, using only information that would reasonably be available at booking time.

Specifically, we aim to:

1. Predict flight delays: Use airline, destination, scheduled departure time, day of week, month, flight distance, and historical climate information to predict the `ArrDel15` label.

2. Compare prediction methods: Train and compare multiple classification methods, initially including logistic regression and decision trees, to determine how different modeling approaches perform on the flight-delay prediction task.

3. Evaluate predictive performance: Evaluate the models on held-out future flight data using metrics such as precision, recall, F1-score, ROC-AUC, and accuracy. Because delayed and non-delayed flights may not occur equally often, we will pay particular attention to F1-score and ROC-AUC rather than relying only on accuracy.

4. Identify important predictors: Examine which booking-time features are most strongly associated with flight delays and analyze situations in which the models make incorrect predictions.

## 4. Data Collection Plan 
### 4.1 BTS Flight data
We plan to use the U.S. Department of Transportation’s Bureau of Transportation Statistics (BTS) “Reporting Carrier On-Time Performance” dataset for domestic flights departing from Boston Logan International Airport. We will collect records from 2020–2025 for model training and validation and January–July 2026 for testing. The dataset includes flight dates, airlines, destinations, scheduled and actual times, flight distance, arrival delays, cancellation indicators, and diversion indicators.

We will download monthly CSV files, combine them using Python, and filter for flights with Boston Logan (BOS) as the origin airport. We will retain scheduled flight information for input features and use `ArrDel15` and `Cancelled` as labels for the separate delay and cancellation prediction tasks. Actual times and other information unavailable at booking will not be used as input features.
Data source: [BTS Reporting Carrier On-Time Performance — Field Definitions]

The prediction target is whether a flight arrives at least 15 minutes late or cancel. We will use the BTS  “ArrDel1” and “Cancelled” indicator as two binary labels. For the delay label, 1 indicates an arrival delay of at least 15 minutes, 0 indicates a delay of less than 15 minutes, including early arrivals, and cancelled flights will be marked as missing. For the cancelation label, 1 indicates a cancel flight and 0 indicates a not cancel flight including both on time and delay flights. Flights with missing target labels will be excluded during cleaning. 

### 4.2 Historical Weather data
We plan to obtain historical weather observations for Boston Logan International Airport from January 1, 2020, through December 31, 2025, using the Iowa Environmental Mesonet (IEM) ASOS/AWOS archive. We will select the BOS station, listed as BOSTON/LOGAN INTL in the Massachusetts ASOS network, and download routine hourly reports in CSV format. Candidate variables include temperature, wind speed, visibility, and cloud cover. We will check missing values and field availability before selecting the final weather variables.

Because our goal is to predict flight delays at booking time, we will use these observations to construct historical weather summaries by month and hour of day, rather than use actual weather on the flight date. These summaries may include average temperature, average wind speed, and the frequency of low-visibility conditions. We will match them to flights using the scheduled departure month and departure hour. We will match climate data from 2020–2024 with corresponding flight information in the train set to link weather conditions to flight delays and generate feature values, while also using weather data from 2000–2024 to forecast the weather for future flight dates.

We will initially exclude destination-airport and en-route weather to keep the project manageable. The historical summaries represent typical weather patterns and cannot capture unexpected conditions on a particular flight date.
Data source: IEM ASOS/AWOS Weather Data Download

### Data Cleaning & Preparation
We will remove duplicate records and prepare separate datasets for delay and cancellation prediction. For delay prediction, we will exclude canceled and diverted flights and records with missing arrival-delay labels. For cancellation prediction, we will retain canceled and non-canceled flights with valid cancellation labels. We will handle missing input values, convert dates and scheduled times into usable features, and encode categorical variables. Preprocessing will be fitted on the training set and applied to the validation and test sets. 

The input features will consist only of information that would be available at booking time. These features will include:

 - Airline
 - Destination airport
 - Scheduled departure time, including day of week and month
 - Day of the week
 - Flight distance
 - Historical climate information at Boston Logan International Airport, such as typical temperature, wind, and cloud conditions for the corresponding time of year and hour
