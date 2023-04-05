Customer Churn Case Study Summary
This project aims to analyze customer churn in a telecom industry company that provides home phone and internet services to 7,043 customers across Southern California, specifically in the San Diego area. The company has faced customer churn due to the entry of a new competitor, and to retain its existing customers, the company has decided to investigate the reasons behind the customer churn.

The objectives of this project are to identify the services that are not performing well and require improvements, the variables that affect customer churn, the services that are popular among customers and can attract new ones, and high-value customers who can be given a premium membership to retain them for longer.

The project starts by reading five CSV files using pandas and analyzing their data types and missing values. Afterward, a MySQL database is created, and tables are created in it using SQLalchemy. All five CSV files are joined into one table named churn_all, and data inconsistencies are checked.

In the second part of the project, the customer's lifetime value (LTV) is calculated by examining the TotalCharges feature for those customers who unsubscribed from the service, along with the duration of their stay with the company. The LTV is important as it helps increase the value of existing customers and drive growth by retaining them for as long as possible.

Finally, the project ends by visualizing the findings using various charts and graphs such as the distribution of total charges, the correlation matrix, and the heatmap. The analysis revealed that the customers who unsubscribed from the company's services had an average LTV of $1,462, and the average duration of their stay was 19 months. Additionally, it was found that the most significant factor affecting customer churn was the tenure of the customers, followed by the type of services subscribed to.

The project's results can help the company understand its customers better and improve the quality of its services, which can lead to a reduction in customer churn and the attraction of new customers.