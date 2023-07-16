# Rest_Api_Service
Rest Api service for for calculating the cost of insurance depending on the type of cargo and the declared value

Clone the project repository to your local computer:

git clone https://github.com/snail911/Rest_Api_Service.git

Run the docker build command to build  container:

docker build -t <your_image_name> .     

Run the docker run command to build  container:

docker run -d --name <your_container_name> -p 5555:5555 <your_image_name>

After the container is successfully launched, your application will be available at the following address:

http://localhost:5555
