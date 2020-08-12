# autowork
This is a small project using technologies like React as frontend , Django restapi , Lime for model interpretation canvas.js for graphs

# Machine Learning Part.
In this project We will use Machine Learning technique to predict What is best Price you can get for your car.
Here we use boosting algorithm called Xgboost to predict the price.
We first preprocess and clean the data which is in intial.ipynb file .
We Select two car make that is maruti and hyundai.
We again preprocess before giving it model seperately in two files i.e., Maruti.ipynb and Hyundai.ipynb.
We will devide the whole data into two parts based on car's orginal price and give it two seperate model.
Here we use Lime to Interpret the model this will give us how each feature effected the overall result (positively or Negetively).

# RestApi Part.
Here We use django and python3.8 virtual environment check out requirements.txt file for dependacies.
We dump every model in json file and put it in backend/models directory
We dump each lime model using dill in backend/lime directory
We create 2 seperate Apps in django for Maruti and Hyundai.
We take features from request and convert them to required type.
We then take output from both model and lime and send the response as json according to request

# Frontend (React) Part.
In the front component we give brief overview and ask users make of thier car.
Seperate components are given for seperate makes and then user have to fill out the details,
After filling out and hitting submit Axios will make request rest api endpoint.
Axios is react package for making request and collecting data from a api endpoint.
The result is taken and show to user.
We use canvas.js package for producing graph out of lime interpretated data.
