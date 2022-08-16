![GeoIQ Automl package](https://geoiq.io/_next/image?url=%2Fimages%2Flogo.svg&w=256&q=75)

# GeoIQ-automl-python

[GeoIQ’s](https://geoiq.io/) ML python package makes it easy for data scientists and machine learning engineers to train your machine learning models at scale, evaluate your trained model, and use the model to make predictions and gain a better understanding of your data.

This package also helps geoiq data users to enrich the points (i.e. latitude/longitude pairs), census boundaries, and zipcodes in their data with geoiq features using Python.

Use this package to prepare datasets and build models as well as deploy, monitor and manage your models in production. 

## Getting started

1. **Installation** 

    Install via pip:

    ```bash
    pip install git+https://github.com/geoiq-io/geoiq_automl.git
    ```
    
    ```bash
    import geoiq_automl
    #### AutoML object
    result = geoiq_automl.automl('API KEY')
    ```
    
   
    
2. **Data Upload** <p align="left">
<img src="https://automl.geoiq.io/static/media/add-dataset.1bde6b66.svg" 
     width="80" 
     height="80"></p>

    User data upload:


    ****2.1 Without geocoding required****
    ```bash
    
    dataset_id = result.create_dataset(df, dataset_name ='test_dataset' ,dv_col = 'dv_90', dv_positive = '1',latitude_col = "geo_latitude" ,
          longitude_col = "geo_longitude",unique_col = 'geoiq_identifier_col',geocoding = 'F',
          address_col = '\'\'', pincode_col = '\'\'' , additional_vars = '[]')
    ```
    ****2.2 Geocoding required****
    ```bash
    
    dataset_id = result.create_dataset(df, dataset_name ='test_dataset' ,dv_col = 'dv_90', dv_positive = '1',latitude_col = "" ,
          longitude_col = "",unique_col = 'geoiq_identifier_col',geocoding = 'T',
          address_col = 'complete_address', pincode_col = 'pin_code_name' , additional_vars = '[]')
    ```

3. **Data Enrichment!**<p align="left">
<img src="https://cdn-icons-png.flaticon.com/512/300/300864.png" 
     width="60" 
     height="60"></p>

    The easiest way to enrich a file like this (with *all* the available GeoIQ features) is by running:

    ```bash
    result.data_enrichment(dataset_id,['p_retail_es_pt_500','mat_wall_mud_unbrnt_brck_perc_500','p_health_hp_np_1000'])
    ```

    S3 bucket link will be returned, in which you have your un-compressed GeoIQ data.
    
4. **Exploratory Data Analysis**<p align="left">
<img src="https://automl.geoiq.io/static/media/compare.4f516f22.svg" 
     width="80" 
     height="80"></p>

    This repo contains a (very small) sample csv file with the locations of twenty four 7-11 stores in Pinellas County, FL. It has `latitude` and `longitude` columns specifying the location of each store and a few additional attributes. The easiest way to enrich a file like this (with *all* the available Iggy features) is by running:

    ```bash
    python -m iggyenrich.iggy_enrich -f ./sample_data/pinellas_711s.csv --iggy_base_loc <iggy_base_loc> --iggy_version_id <iggy_version_id> --latitude_col latitude --longitude_col longitude
    ```
    
5. **Train a model**<p align="left">
<img src="https://automl.geoiq.io/static/media/train.6fddcfa4.svg" 
     width="80" 
     height="80"></p>

    This repo contains a (very small) sample csv file with the locations of twenty four 7-11 stores in Pinellas County, FL. It has `latitude` and `longitude` columns specifying the location of each store and a few additional attributes. The easiest way to enrich a file like this (with *all* the available Iggy features) is by running:

    ```bash
    python -m iggyenrich.iggy_enrich -f ./sample_data/pinellas_711s.csv --iggy_base_loc <iggy_base_loc> --iggy_version_id <iggy_version_id> --latitude_col latitude --longitude_col longitude
    ```

6. **Evaluate a model**<p align="left">
<img src="https://automl.geoiq.io/static/media/evaluate.dbfee37d.svg" 
     width="80" 
     height="80"></p>

    This repo contains a (very small) sample csv file with the locations of twenty four 7-11 stores in Pinellas County, FL. It has `latitude` and `longitude` columns specifying the location of each store and a few additional attributes. The easiest way to enrich a file like this (with *all* the available Iggy features) is by running:

    ```bash
    python -m iggyenrich.iggy_enrich -f ./sample_data/pinellas_711s.csv --iggy_base_loc <iggy_base_loc> --iggy_version_id <iggy_version_id> --latitude_col latitude --longitude_col longitude
    ```
7. **Prediction from a model**<p align="left">
<img src="https://cdn-icons-png.flaticon.com/512/300/300834.png" 
     width="60" 
     height="60"></p>

    This repo contains a (very small) sample csv file with the locations of twenty four 7-11 stores in Pinellas County, FL. It has `latitude` and `longitude` columns specifying the location of each store and a few additional attributes. The easiest way to enrich a file like this (with *all* the available Iggy features) is by running:

    ```bash
    python -m iggyenrich.iggy_enrich -f ./sample_data/pinellas_711s.csv --iggy_base_loc <iggy_base_loc> --iggy_version_id <iggy_version_id> --latitude_col latitude --longitude_col longitude


# Example


 





## See [demo.ipynb](https://github.com/jingtt/varclushi/blob/master/demo.ipynb) for more details.


```python
import pandas as pd
from varclushi import VarClusHi
```

Create a VarClusHi object and pass the dataframe (df) to be analyzed as a parameter, you can also specify 
- a feature list (feat_list, default all columns of df)
- max second eigenvalue (maxeigval2, default 1)
- max clusters (maxclus, default None)

Then call method varclus(), which performs hierachical variable clustering algorithm

```python
demo1_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
demo1_df.drop('quality',axis=1,inplace=True)
demo1_vc = VarClusHi(demo1_df,maxeigval2=1,maxclus=None)
demo1_vc.varclus()
```
```
<varclushi.varclushi.VarClusHi at 0x15f96e35e10>
```
Call info, you can get the number of clusters, number of variables in each cluster (N_vars), variance explained by each cluster (Eigval1), etc.

```python
demo1_vc.info
```
```python
  Cluster N_Vars   Eigval1   Eigval2   VarProp
0       0      3  2.141357  0.658413  0.713786
1       1      3  1.766885  0.900991  0.588962
2       2      2  1.371260  0.628740  0.685630
3       3      2  1.552496  0.447504  0.776248
4       4      1  1.000000  0.000000  1.000000
```

Call rsquare, you can get the (1 - rsquare) ratio of each variable

```python
demo1_vc.rsquare
```

```python
   Cluster              Variable    RS_Own     RS_NC  RS_Ratio
0        0         fixed acidity  0.882210  0.277256  0.162976
1        0               density  0.622070  0.246194  0.501362
2        0                    pH  0.637076  0.194359  0.450478
3        1   free sulfur dioxide  0.777796  0.010358  0.224530
4        1  total sulfur dioxide  0.786660  0.042294  0.222761
5        1        residual sugar  0.202428  0.045424  0.835525
6        2             sulphates  0.685630  0.106022  0.351653
7        2             chlorides  0.685630  0.048903  0.330534
8        3           citric acid  0.776248  0.398208  0.371810
9        3      volatile acidity  0.776248  0.040920  0.233299
10       4               alcohol  1.000000  0.082055  0.000000
```



## More resources

    You can find our Data Catalogue [here](https://catalog.geoiq.io/in).


## Contact us

For questions or issues with using this code, please [add a New Issue](https://github.com/geoiq-io/geoiq_automl/issues/new) and we'll respond as quickly as possible.

To get access to GeoIQ sample data please contact us [here](https://www.geoiq.io/contact)!

If you cannot find an answer to a question in here or at any of those links, please do not hesitate to reach out to GeoIQ Support (support@geoiq.io).
