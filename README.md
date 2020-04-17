# IS706-SoftwareMiningProject
## Label prediction for arbitrary source code using deep network

Source code for project for Software Mining IS706 by Singapore Management University MITB/SIS/PHd Students
Andrico CAHYADI andricoc.2018@mitb.smu.edu.sg, NGUYEN Duy Tai dtnguyen.2019@phdcs.smu.edu.sg, NGUYEN Hua Gia Phuc hgpnguyen.2019@phdcs.smu.edu.sg , Joel Tay Da Yuan joel.tay.2016@sis.smu.edu.sg

### Abstract

Due to the rapid expansion of available source code in recent years, code search and comprehension have become more and more difficult. It is problematic for the programmer to label their own code. Current tools lack a way to label arbitrary code at scale while maintaining up-to-date with new programming languages, libraries, and functionalities that appear continuously. The key to the problem is to have an automatic comprehensive labeling of source code that will help the user to search for documents of interest more easily and have high-level understanding of their contents. To achieve the above goal, Stack Overflow
code snippets and their tags have been collected to train a neural network to automatically predict semantic labels for source code documents. The result obtained shows that this is a promising method to understand the functionalities of arbitrary source code documents.

In this repository, we present a novel framework for generating labels for source code of arbitrary language, length, and domain. 
By capturing the wealth of SO, a forum that provides a constantly growing source of code snippets, that are user-labeled with programming languages, tool sets, and functionalities, using machine learning method, we create a multilabel classification model for source code documents. To sum up, our approach utilizes SO’s code snippets to simultaneously model thousands of concepts and predict
on previously unseen source code.

### Data
The Stackoverflow data is obtained from [StackExchange](https://archive.org/download/stackexchange), which is available publicly. 
Download the latest meta.stackoverflow.com.7z 

Run the SQL file to convert into a raw input CSV for further processing

Otherwise, Raw/ Processed / Final Datasets can be found [here](https://drive.google.com/drive/folders/1h3QIiPm0d8Yo7fSmupoxE-cKQ3KfZ5uS?usp=sharing) Accessible with SMU Email


### Model
1. Basic CNN Model
2. Deep CNN Model
3. Stacked CNN Model [1]

Save your selected model as a .h5 to run the UI application

### Run basic UI application
> Run python user_interface.py 

Dependencies can be found in requirements.txt file

### Reference 
[1] Ben Gelman, Bryan Hoyle, Jessica Moore, Joshua Saxe, and David Slater. 2018. A language-agnostic model for semantic source code labeling. In Proceedings of the 1st International Workshop on Machine Learning and Software Engineering in Symbiosis (MASES 2018). Association for Computing Machinery, New York, NY, USA, 36–44
