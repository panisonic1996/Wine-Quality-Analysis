### Wine-Quality-Analysis

### This is a project to explore the various characteristics and quality of wine. Data for analysis has been taken from the site “https://winestatistics.com/”.

  *“WineStatistics is a wine tasting community, meant to describe modern wine by quantifying its subjective qualities (visual aspect, nose and palate) into comparable data indexes, so that the end result is a easy-to-read and 100% comparable wine rating system.  Our goal is to provide you, the reader, with a flexible tool, that will allow you to compare wines side by side. For example, you will be able to compare a wine that you have tasted, to a wine you only intend to taste or buy”.*
  
  Wines are evaluated according to the following indicators:
   color, aroma, flavor, sweetness, alcohol, acidity, tannin, balance, finish, aftertaste.
  Wine rating has following structure:
  - 93 – 100 (great) - a wine that has all the traits to become legendary
  - 91 – 92 (fine) - a wine of premium quality with good potential
  - 89 – 90 (nice) - a well made wine that lacks elegance and finesse
  - 75 – 88 (fair) - a decent wine that lacks character and structure
  
### Project steps:

  1). The parser went from the dynamic page to a separate page for each wine, collected data, downloaded images, processed and extracted data from them and put everything to a csv document(for scraping Beautiful Soup и easyocr were used).
folder ‘creating dataset’

  2). Created dataset was cleaned, additional characteristics and columns were created, the data was standardized.
folder ‘cleaning dataset’

  3). Cleaned dataset was visualized(using matplotlib and seaborn).
folder ‘visualization’

  4). For wine rating prediction was built Linear Regression Model
((R^2): 0.95, (MSE): 0.14)

  5). For wine classification were build:
- Multi-Class Classifier(Tensorflow and Keras)
      -loss: 0.1911 accuracy: 0.9425 on test dataset
- SVM Model
      -Test accuracy: 0.948
folder ‘building models’



 *saved and trained models are stored in ‘models’ folder*
 
 *raw and processed dataset  - ‘Data’*
 
 *link to scraped images -* 
 https://drive.google.com/drive/folders/1R7DmelV4sfMLO1SKdMcLgzABnOUQIYKr?usp=sharing
