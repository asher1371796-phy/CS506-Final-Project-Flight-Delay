# CS506-Final-Project-Flight-Delay
CS506 final project: Predicting flight delays ahead using historical flight and weather data.

### 1. Group Members
Mengkai Li
//Yilin Lyu
//Zheng Zhen

### 2. Project Description

> Air travel is typically used for journeys or missions where timeliness is critical; consequently, delays or cancellations often entail significant costs. This project will investigate whether information available at booking time can be used to predict if a domestic flight departing from Boston Logan International Airport will arrive late. By comparing several prediction methods and examining when errors occur, we aim to provide passengers with data-driven, booking time on-time performance predictions, enabling them to plan their onward travel accordingly and minimize potential disruptions. Given the multitude of factors contributing to flight delays, our initial efforts will focus on flight route information such as destination, departure time and historical climate conditions at Logan Airport. Subsequently, we will evaluate the model's predictive performance and consider incorporating additional influencing factors in later stage of the project.

We plan to complete the main analysis over eight weeks, followed by preparation of the final report and presentation.

- **Weeks 1–2:** Download BTS flight records and IEM weather observations. Check data availability, field definitions, and the proportion of canceled flights.
- **Weeks 3–4:** Clean the data, prepare separate delay and cancellation datasets, and construct historical weather features. 
- **Weeks 5–6:** Train logistic regression and decision tree models using 2020–2024 data. Use 2025 data for validation and parameter selection. 
- **Weeks 7–8:** Refit the selected models using 2020–2025 data and evaluate them on 2026/1-7 flights. Analyze errors and look for reasons.
- **Early December:** Finalize the reproducible code, README report, visualizations, tests, and recorded presentation for submission by December 9.

Potential challenges include missing data, unequal numbers of delayed and non-delayed flights, and changes in flight patterns across years. Flights during the COVID-19 pandemic may differ from those in later years, which could affect predictions on the test set. Historical climate summaries also cannot capture unexpected weather events. We will consider these limitations when interpreting model performance and discussing how useful the predictions may be for passengers.
