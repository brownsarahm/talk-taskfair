```{slide} Assessing Machine Learning Problems for Fairness Before Fitting
:class: title

### Sarah M Brown
#### University of Rhode Island
*joint work with Surbhi Rathore*

```



````{slide} Why Fairness in Machine Learning?

```{figure} img/gendershades.png
Boulamwini and Gebru 2018

```
````



````{slide} Why Fairness in Machine Learning?
:class: overlay

<!-- ![two defendents from the ProPublica COMPAS article](img/machine_bias.jpg) -->
```{figure} img/machine_bias.jpg
:class: fill

Angwin et al 2016
```
````


````{slide} Why Fairness in Machine Learning?


```{figure} img/obermyerscience.png

Obermyer et al 2019
```

````


```{slide} Algorithmic Fairness Interventions
:class: build

- blame the data, not my problem 

- repair the data (preprocessing) 

- alter the learning (inprocessing) 

- change how the model is used  (postprocessing) 


```

````{slide} An Alternative Proposal 

> reformulate the problems that we apply AI to so that they are better suited to producing socially acceptable outcomes

```{note}
Passi et al 2019
Chen et al
```
````


````{slide} More on Obermyer's result

![obermyer overall](img/obermyer_target.jpg)

<!-- ```{image} img/obermyer_target.jpg
``` -->

````


````{slide} The disparity was larger on detailed measures
![obermyer_disparity](img/obermyer_disparity.jpg)
````


````{slide} Potential Impact of Reformulation
![obermyer fix](img/obermyer_reformulated.jpg)

````


````{slide} How do we know when to reformulate?

```{admonition} Proposal
computationally efficient information theoretic quantities for evaluating problem setups
```

````


````{slide} Agenda:

1. Information Theory
<!-- (background) -->
2. AI Task Formalization
<!-- (setup) -->
3. Information theoretic task fairness
<!-- (main contribution) -->
4. Experimental Results
<!-- (validation) -->

````


````{slide} Why Information Theory

````


````{slide} Information Theory

![MI_X](img/MI_X.jpg)

````


````{slide} Information Theory

![MI_Y](img/MI_Y.jpg)

````


````{slide} Information Theory

![MI_X](img/MI_highlight.jpg)

````


````{slide} Information Theory

![MI_X](img/MI_ML.jpg)

````


````{slide} Formally

$$\operatorname{I}(X;Y) =  \sum_{x,y} p(x,y) \log \frac{p(x,y)}{p(x)p(y)} $$

$$\operatorname{I}(X;Y) = \operatorname{D_{KL}}(p(X,Y) || p(X)p(Y) ) $$

````


````{slide}  Conditional MI

$$\operatorname{I}(X;Y|Z) &=\sum_z p(z)  \sum_{x,y} p(x,y|z) \log \frac{p(x,y|z)}{p(x|z)p(y|z)} $$


<!-- Independence: $\operatorname{I}(X;Y) =  0$ -->



````


````{slide}  Tasks in AI  and ML
:class: section

```{note}
- typically hoc
- hard to apply a formal technique
- lets formalize
```

````


````{slide} Let's predict concept $Z$ !


*idealized task*: a prediciton target concept, $Z$

````


````{slide}  Can we even do that theoretically?


an idealized task is plausible if there exist some set of features $X^*$ that can be used to for prediction

$$ \operatorname{I}(X^*; Z) = 1- \epsilon$$

````


````{slide} But can we *really* do that?

a *realized* task include measurable features $X$ and a measurable proxy target $Y$

````

````{slide} Example: Obermyer
:class: build


- $Z$ is who needs managed care 
- $X^*$ is a full picture of health and possibly some SES
- $X$ is the electronic health record
- $Y$ the datascientists chose health care expenditures

````


````{slide} ML Tasks

- Idealized task: predict $Z$ (latent)
- Plausible Task: predict $Z$ from $X^*$ (possibly immeasurable or expensive)
- Realized task: predict $Y$ (observed) from $X$ (observed), interpret as $\hat(Y)$ as $Z$


> realized task is somethign we can **choose** and manipulate, but most 
ML research considers the dataset (and therefore the task) fixed
````




````{slide} Information Theoretic Task Fairness
:class: section

````


````{slide} Classical Fairness Criteria

- Independence: $\operatorname{I}(A;\hat{Y}) = 0$
- Separation: $\operatorname{I}(A;\hat{Y}|Y) = 0$
- Sufficiency: $\operatorname{I}(A;Y|\hat{Y}) = 0$

````


````{slide} Classical Fairness Criteria in Realized Tasks

- Feature Independence: $\operatorname{I}(A;X) = 0$
- Proxy Independence: $\operatorname{I}(A;Y) = 0$
- Separation: $\operatorname{I}(A;X|Y) = 0$
- Sufficiency: $\operatorname{I}(A;Y|X) = 0$

````


````{slide} Approximations

#### Informative Beyond Demographics

$$ \operatorname{I}(Y;X) > \operatorname{I}(A;X )$$

### Group-wise Uniformly Informative Beyond Demographics

$$ \operatorname{I}(Y;X|A=a) > \operatorname{I}(A;X ) \forall a \in A$$

````


````{slide} Equality of Information

$$ \operatorname{I}(Y;X|A=a_1) - \operatorname{I}(Y;X|A=a_2) < \epsilon $$


````





````{slide} Estimating Distributions


- tabular data, histogram estimates of density make MI easy to calculate.
- Number of bins does not impact the information theory **comparisons**

*in nondegenerate cases*

````

````{slide} Practical Application

- determine idealized task
- collect data for a candidate realized task or several
- build histograms
- calculate MIs
- check for acceptability
- proceed, reformulate, or do not build

````


````{slide} Obermeyer


Information gap (black vs white) is larger for costs than for Number of chronic illnesses


````


````{slide} Adult Reconstruction

- Ding et al reconstructed the Adult dataset from source
- many features about 70k people
- continuous valued income instead of >50k binary
- they found that different binary prediction problems have different fairness

````


````{slide} Informative beyond Demographics?

![thresh](img/mi_by_thresh_ar.png)

````


````{slide} Equality of Information?

![eq](img/mi_by_thresh_xya.png)

````


````{slide} Separation ?


![sep](img/mi_by_thresh_xay.png)

````

````{slide} Conclusion 

For modestly sized tabular datasets, we have a computationally efficient technique to assess if a problem is well specified enough to admit fairness
```



````{slide} Questions?
:class: section

brownsarahm@uri.edu
````



<!-- extra -->





<!-- 

`````{slide} Emphasize Evaluation
:class: strategy

```{panels}
in Instruction
^^^
- Frame evaluation as competing goals
````


````{slide} 
in Assignments
^^^
- Always require more than one metric
- Disaggregate by group in social data

```

```{note}

Evaluation allows students to think about problems more deeply.

Fairness issues "discovered" in ML through eval

It helps monitor, considering broader impact
```

````` -->