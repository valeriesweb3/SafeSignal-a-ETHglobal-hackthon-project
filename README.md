# ETHglobal hackthon project: SafeSignal

![Screen Shot 2023-11-19 at 09.13.25.png](ETHglobal%20hackthon%20project%20SafeSignal%206ecc6b05d65f44bcb34ee5ec8ea2eeb5/Screen_Shot_2023-11-19_at_09.13.25.png)

### **Crypto Safety: Preventing Bank Runs and Liquidity Crises in CEX, withdraw or not for users when possible FTX rugs**

![DALL·E 2023-11-19 04.11.05 - Illustration of a centralized cryptocurrency exchange with a sign 'Assets Frozen'. Include text 'SafeSignal', 'Bank Runs', 'Liquidity Crises', and 'CE.png](ETHglobal%20hackthon%20project%20SafeSignal%206ecc6b05d65f44bcb34ee5ec8ea2eeb5/DALLE_2023-11-19_04.11.05_-_Illustration_of_a_centralized_cryptocurrency_exchange_with_a_sign_Assets_Frozen._Include_text_SafeSignal_Bank_Runs_Liquidity_Crises_and_CE.png)

### Introduction

The recent incident where Binance froze accounts linked to Hamas at the request of the Israeli government, transferring funds to the Israeli state treasury. Or the average crypto user who lost their assets in the FTX coin withdrawal run crisis.

![Screen Shot 2023-11-19 at 04.20.59.png](ETHglobal%20hackthon%20project%20SafeSignal%206ecc6b05d65f44bcb34ee5ec8ea2eeb5/Screen_Shot_2023-11-19_at_04.20.59.png)

These have raised significant concerns among CEX users. The apprehension revolves around the potential for their accounts to be similarly frozen or seized, especially in the context of future conflicts or geopolitical tensions.

### Problem Statement

In an era where digital assets are increasingly intersecting with global politics, the security and autonomy of users' assets on centralized exchanges have come under scrutiny. The incident with Binance & FTX highlights a crucial vulnerability: users’ assets on these platforms can be compromised or seized based on political and economical interventions, or it could be a purely black swan event. This undermines trust in CEX and poses a risk to the individual financial autonomy of users, especially in regions prone to conflict or political instability.

![DALL·E 2023-11-19 05.43.51 - Illustration for the theme 'Helping Users Avoid Bank Runs and Liquidity Crises in CEX, Protecting Asset Safety'. Depict a centralized exchange (CEX) w.png](ETHglobal%20hackthon%20project%20SafeSignal%206ecc6b05d65f44bcb34ee5ec8ea2eeb5/DALLE_2023-11-19_05.43.51_-_Illustration_for_the_theme_Helping_Users_Avoid_Bank_Runs_and_Liquidity_Crises_in_CEX_Protecting_Asset_Safety._Depict_a_centralized_exchange_(CEX)_w.png)

### Proposed Solution

The proposed solution aims to enhance transparency and predictability for users of centralized exchanges, focusing on two key strategies:

1. **Development of a Context Builder for Asset Pricing:**
    - **Objective:** To create a predictive tool that helps users understand the potential risks associated with their assets on centralized exchanges.
    - **Methodology:** This tool will integrate diverse data sets, including macroeconomic indicators, investor sentiment, political and geopolitical developments, and specific characteristics of the crypto industry.
    - **Implementation:** By encouraging user participation through incentives for honest feedback, the tool will be able to quantify user honesty. This data will be used to refine the model, leading to a more accurate and reliable prediction oracle.

<aside>
💡 **DMI modeling:**

In the past, some studies have successfully designed so-called "multi-task peer prediction mechanisms" in which honest answers are always better than other strategies, which is called "dominant truthfulness". The problem is that these mechanisms require an infinite number of tasks to work, which is not feasible in practice.

Suppose we are running a survey that includes a series of yes/no questions, such as:

Do you like coffee? Yes/No
Do you like tea? Yes/No
Do you like getting up early? Yes/No
In this survey, we wanted to encourage participants to answer the questions honestly, but we had no way of directly verifying that their answers were true. This is where we need to design a "peer prediction mechanism".

![Screen Shot 2023-11-19 at 08.15.52.png](ETHglobal%20hackthon%20project%20SafeSignal%206ecc6b05d65f44bcb34ee5ec8ea2eeb5/Screen_Shot_2023-11-19_at_08.15.52.png)

pic source: [https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.95/LIPIcs.ITCS.2022.95.pdf](https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.95/LIPIcs.ITCS.2022.95.pdf)

In the past, some studies have successfully designed so-called "multi-task peer prediction mechanisms" in which honest answers are always better than other strategies, which is called "dominant truthfulness". The problem is that these mechanisms require an infinite number of tasks to work, which is not feasible in practice.

Suppose we are running a survey that includes a series of yes/no questions, such as:

Do you like coffee? Yes/No
Do you like tea? Yes/No
Do you like getting up early? Yes/No
In this survey, we wanted to encourage participants to answer the questions honestly, but we had no way of directly verifying that their answers were true. This is where we need to design a "peer prediction mechanism".

Recently, a new study has proposed the first multitasking peer prediction mechanism that is both optimally true and applicable to a limited number of tasks, called the Decisive Mutual Information **(DMI)** mechanism. This is a practical step forward. However, it is still an open question whether there are other practical, optimally realistic multitasking peer prediction mechanisms.

This work answers this question by providing a new measure of information, Volumetric Mutual Information (VMI), in which DMI is only a special case of VMI. It also proposes a series of practical, predominantly true multitasking peer prediction mechanisms based on VMI, i.e., VMI mechanisms.

To illustrate the importance of VMI mechanisms, the study also proposes an easy-to-handle effort incentive optimisation objective. It is shown that while DMI mechanisms may not be optimal, we can construct a series of near-optimal VMI mechanisms.

The main technical highlight of this paper is a new measure of geometric information, volumetric mutual information. It is based on a simple idea: we can measure the amount of information in an object A by comparing the amount of information in A with the number of those objects that are less informative than A. The information in A can be measured by comparing the number of objects that are less informative than A with the number of objects that are less informative. Different object densities lead to different measures of information. This also provides a simple geometric explanation for deterministic mutual information.

![Screen Shot 2023-11-19 at 08.14.30.png](ETHglobal%20hackthon%20project%20SafeSignal%206ecc6b05d65f44bcb34ee5ec8ea2eeb5/Screen_Shot_2023-11-19_at_08.14.30.png)

pic source: [https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.95/LIPIcs.ITCS.2022.95.pdf](https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.95/LIPIcs.ITCS.2022.95.pdf)

</aside>

1. **Integration of Context Builder with Market Data:**
    - **Focus:** Primarily on Binance, given its centrality in the recent incident.
    - **Data Analysis:** The tool will analyze **the flow of USDT and USDC within Binance-controlled hot wallets on the Ethereum blockchain**, focusing on the most **recent 500 blocks (approximately 100 minutes).** This analysis will provide real-time insights into capital flows and market sentiment
    
    <aside>
    💡 data source: [https://www.binance.com/en/blog/community/our-commitment-to-transparency-2895840147147652626](https://www.binance.com/en/blog/community/our-commitment-to-transparency-2895840147147652626)
    
    </aside>
    
    <aside>
    💡 indexing realtime onchain data collected in online form using API by : [https://docs.google.com/spreadsheets/d/1QnmWPVeIS7ZGpWpLCuqg1f4-ryUlF4WPn7-oNOUjxPM/edit#gid=0](https://docs.google.com/spreadsheets/d/1QnmWPVeIS7ZGpWpLCuqg1f4-ryUlF4WPn7-oNOUjxPM/edit#gid=0)
    
    </aside>
    
    ![Screen Shot 2023-11-19 at 08.34.08.png](ETHglobal%20hackthon%20project%20SafeSignal%206ecc6b05d65f44bcb34ee5ec8ea2eeb5/Screen_Shot_2023-11-19_at_08.34.08.png)
    
    ![Screen Shot 2023-11-19 at 08.33.54.png](ETHglobal%20hackthon%20project%20SafeSignal%206ecc6b05d65f44bcb34ee5ec8ea2eeb5/Screen_Shot_2023-11-19_at_08.33.54.png)
    
    - **Outcome:** The integrated database, combining the context builder and market data, will provide users with clear conclusions regarding their asset security. In events similar to the Binance incident, users will be able to make informed decisions about whether to move their funds to mitigate potential risks.
    
    <aside>
    💡 CMA = F(CD, MD)
    
    Where:
    CD = G(TDA, ORD)
    MD = H(BWF, EBA)
    
    TDA = Analyze_Twitter(Tweets) -> {Sentiment_Score, Theme_Vector, Keyword_Frequency}
    BWF = Observe_Binance_Wallets(Last_500_Blocks) -> {USDT_Flow, USDC_Flow}
    EBA = Ethereum_Blockchain_Analysis(Last_500_Blocks)
    
    F: Composite Analysis Function
    G: Context Data Processing Function
    H: Market Data Processing Function
    Analyze_Twitter: Twitter Data Analysis Function
    Observe_Binance_Wallets: Binance Wallet Observation Function
    Ethereum_Blockchain_Analysis: Ethereum Blockchain Analysis Function
    
    ### **Explanation of the Formula**
    
    - **CMA (Contextual Market Analysis)**: This is the final analytical output, a composite based on Context Data (CD) and Market Data (MD).
    - **CD (Context Data)**: Context data, composed of Twitter Data Analysis (TDA) and Other Relevant Data (ORD).
    - **MD (Market Data)**: Market data, consisting of observations of Binance Wallet Flows (BWF) and Ethereum Blockchain Analysis (EBA).
    - **TDA (Twitter Data Analysis)**: Analysis of Twitter data, outputting sentiment scores, thematic vectors, and keyword frequencies.
    - **BWF (Binance Wallet Flows)**: Observations of USDT and USDC flows in Binance wallets over the most recent 500 blocks.
    - **EBA (Ethereum Blockchain Analysis)**: Analysis of Ethereum blockchain data for the most recent 500 blocks.
    
    This formula expresses different data sources and analytical steps in the form of mathematical functions, providing a structured approach to integrate and analyze data. In practical application, the implementation of each function would involve data processing, statistical analysis, and possibly machine learning algorithms.
    
    </aside>
    
    If the final result shows that any type of data indicates market panic, then a very clear conclusion YES or NO supporting user withdrawals should be displayed. If the same news event occurs, such as Binance or another superpower once again blocking a major figure's account, ordinary crypto users should consider immediately transferring their funds to avoid potential risks.
    

### Expected Benefits

- **Enhanced User Trust:** By providing transparent and data-driven insights, the solution aims to rebuild trust among users of centralized exchanges.
- **Risk Mitigation:** Users will be better equipped to make timely decisions to protect their assets in the face of potential political interventions.
- **Market Stability:** Improved predictability and transparency can contribute to greater overall stability in the cryptocurrency market.

Webpage:

[https://safesignal.framer.ai/](https://safesignal.framer.ai/)

### Conclusion

This proposal presents a proactive approach to addressing the vulnerabilities exposed by the Binance incident. By leveraging data analysis and user feedback, it aims to enhance the security and autonomy of users’ digital assets, thereby fostering a more resilient and trustworthy cryptocurrency ecosystem.
