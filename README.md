# SENet (Keras implementation)

Naive implementation of SENet models in Keras.
- Transplanting https://github.com/taki0112/SENet-Tensorflow to Keras.
- Only SE-ResNext at this stage.

## Prerequisites
- nvidia-docker environment

## Environment constuction
- Build a docker image (on the root directory of the repository)
  ```
  $ docker build -t [tag name] -f docker/Dockerfile .
  ```
- Create a container using the image
  ```
  $ nvidia-docker run -it -v $PWD:/work [tag name]
  ```

## Train a model
- Train a model with cifar10 data.
  ```
  (in the container) $ pwd
  /work
  (in the container) $ python train-cifar10.py
  ```
  Note that this script is written in an insufficient way; use data generator in consideration of expansion to general image data). The training speed is slow.


## Evaluate the model
- Launch a jupyter notebook.
  ```
  (in the container) $ bash launch_notebook.sh
  ```
- Execute `evaluate-cifar10.ipynb` notebook.
