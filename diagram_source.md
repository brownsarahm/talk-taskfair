```{mermaid}
flowchart LR
    subgraph L[Training]
    direction TB
    D[(training data <br> x,y )] --> |input to| A[learning algorithm]
    A --> |outputs| th[parameters]
    end
    subgraph T[Testing]
    direction LR
    Dt[(test data <br> x*)] --> |input to | P(prediction aglorithm) 
    P--> |output| yhat[(prediction <br> y*)] 
    end 
    th --o | specify| P
```
