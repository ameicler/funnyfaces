# Funny faces 👀

This repository contains the code for the Googly Eyes service of Funny Faces Inc.

![](src/images/friends_result.png)

## Usage

### A/ Setup

In order to install and use the application, you can simply build it using Docker 🐳 :

``` bash
docker build . -t funnydocker
```

Or you can also install it locally if you have conda and Pip installed 🐍 :
``` bash
conda update -n base conda \
  && conda create -y --name funnyenv python=3.6 \
  && activate funnyenv \
  && conda install -c conda-forge rdkit
pip install -r requirements.txt
python main.py
```

The Flask server should be now be running properly.

### B/ Submitting requests to the server

Once you have successfully built the docker image, you can run the Flask server while exposing the port 5000:

``` bash
docker run -p 5000:5000 funnydocker
```

The Flask server will then be running and you should be able to POST a request to the `funny` route. For example:

``` bash
$ curl -X POST -F image=@friends.jpg 'http://localhost:5000/funny'`
```

Or by running the `simple_requests.py` script that will send an image and save the result on the client side.

``` sh
python simple_request.py
```